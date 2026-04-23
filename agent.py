import os
import json
from dotenv import load_dotenv
import anthropic

# Cargar variables de entorno (para API key)
load_dotenv()

# Inicializar cliente de Anthropic
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

def read_document(file_path):
    """Lee el contenido de un documento."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        return f"Error al leer el archivo: {str(e)}"

def write_document(file_path, content):
    """Escribe o sobreescribe contenido en un documento."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        return f"Documento guardado exitosamente en: {file_path}"
    except Exception as e:
        return f"Error al escribir el archivo: {str(e)}"

# Definición de herramientas (Tools)
tools = [
    {
        "name": "read_document",
        "description": "Lee el contenido de un documento local. Útil para revisar, analizar y extraer información de un documento.",
        "input_schema": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "La ruta exacta al archivo que se quiere leer, por ejemplo 'documento.txt' o 'ruta/al/archivo.md'."
                }
            },
            "required": ["file_path"]
        }
    },
    {
        "name": "write_document",
        "description": "Escribe contenido en un documento local. Útil para crear nuevos documentos, o actualizar y guardar revisiones de documentos existentes.",
        "input_schema": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "La ruta al archivo donde se va a guardar el contenido."
                },
                "content": {
                    "type": "string",
                    "description": "El contenido de texto completo a escribir en el archivo."
                }
            },
            "required": ["file_path", "content"]
        }
    }
]

def process_tool_call(tool_name, tool_input):
    if tool_name == "read_document":
        return read_document(tool_input["file_path"])
    elif tool_name == "write_document":
        return write_document(tool_input["file_path"], tool_input["content"])
    else:
        return f"Herramienta no reconocida: {tool_name}"

def run_agent(user_message):
    print("🤖 Iniciando agente y procesando tu solicitud...")
    
    messages = [{"role": "user", "content": user_message}]
    
    system_prompt = """Eres un agente avanzado de inteligencia artificial enfocado en la lectura, revisión y redacción de documentos.
Tienes la habilidad de responder en formato texto, pero además cuentas con el uso de 'tools' (herramientas) para LEER y ESCRIBIR archivos del sistema local del usuario.
- Si el usuario te pide revisar un documento, usa tu herramienta para leerlo; luego haz sugerencias, o utiliza tu herramienta de escritura para crear un documento con la versión revisada y corregida.
- Si el usuario te pide escribir un documento, usa tu herramienta de escritura y luego avísale que el archivo fue creado exitosamente.
- Siempre confirma tus acciones a través de texto al usuario."""

    while True:
        try:
            response = client.messages.create(
                model="claude-4-6-sonnet-latest",
                max_tokens=4096,
                system=system_prompt,
                tools=tools,
                messages=messages
            )
        except Exception as e:
            print(f"\n❌ Se produjo un error al contactar la API de Anthropic: {e}")
            break
            
        # Añadir la respuesta de Claude al historial de mensajes
        messages.append({
            "role": "assistant",
            "content": response.content
        })
        
        # Imprimir cualquier respuesta en texto proporcionada por el asistente
        for block in response.content:
            if block.type == "text":
                print(f"\n[Claude]: {block.text}")
        
        # Verificar si Claude decidió llamar a alguna herramienta
        if response.stop_reason == "tool_use":
            tool_outputs = []
            
            for block in response.content:
                if block.type == "tool_use":
                    print(f"\n🛠️  Claude solicitó usar la herramienta: '{block.name}'")
                    print(f"   Parámetros: {json.dumps(block.input, indent=2, ensure_ascii=False)}")
                    
                    # Se ejecuta la herramienta
                    tool_result = process_tool_call(block.name, block.input)
                    print(f"   Resultado: {str(tool_result)[:150]}...\n")
                    
                    tool_outputs.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": str(tool_result)
                    })
            
            # Devolver los resultados de las herramientas a Claude
            messages.append({
                "role": "user",
                "content": tool_outputs
            })
        else:
            # Flujo terminado; Claude ya no requiere llamadas a herramientas
            print("\n✅ Proceso completado.")
            break

if __name__ == "__main__":
    import sys
    
    # Manejo básico de input desde terminal
    if len(sys.argv) > 1:
        mensaje_inicial = " ".join(sys.argv[1:])
    else:
        print("💡 Te doy la bienvenida al Agente Lector y Revisor de Documentos con Claude 4.6\n")
        mensaje_inicial = input("📝 ¿Qué necesitas que haga con los documentos?: ")
        if not mensaje_inicial.strip():
            print("Operación cancelada.")
            sys.exit(0)
            
    run_agent(mensaje_inicial)
