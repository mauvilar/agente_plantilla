import os
import json
from dotenv import load_dotenv
import anthropic
import subprocess

# Cargar variables de entorno (para API key)
load_dotenv()

# Inicializar cliente de Anthropic
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

def text_to_speech(text):
    """Convierte texto a voz (en macOS usa 'say')."""
    try:
        print(f"🔊 Reproduciendo audio: '{text}'")
        # En MacOS podemos usar el comando nativo 'say'
        # En Windows/Linux, se podría sustituir por librerías como pyttsx3 o APIs de TTS
        subprocess.run(["say", text])
        return "Audio reproducido con éxito al usuario."
    except FileNotFoundError:
        print(f"🔊 [TEXTO-A-VOZ SIMULADO]: '{text}'")
        return "Audio simulado con éxito (comando 'say' no encontrado)."
    except Exception as e:
        return f"Error al reproducir audio: {str(e)}"

# Definición de herramientas (Tools)
tools = [
    {
        "name": "text_to_speech",
        "description": "Convierte el texto en voz para que el usuario pueda escucharlo en tiempo real. Utiliza esta herramienta SIEMPRE que quieras que el usuario escuche tu respuesta de forma hablada.",
        "input_schema": {
            "type": "object",
            "properties": {
                "text": {
                    "type": "string",
                    "description": "El texto que será dictado y convertido en voz."
                }
            },
            "required": ["text"]
        }
    }
]

def process_tool_call(tool_name, tool_input):
    if tool_name == "text_to_speech":
        return text_to_speech(tool_input["text"])
    else:
        return f"Herramienta no reconocida: {tool_name}"

def run_conversational_agent():
    print("🎙️ Iniciando Agente Conversacional de Voz y Texto con Claude 4.6...")
    print("Escribe tus mensajes. Escribe 'salir' para terminar la conversación.\n")
    
    messages = []
    
    system_prompt = """Eres un asistente conversacional amigable, útil y muy conciso.
Estás diseñado para interacciones que pueden ser tanto en texto como en voz. Tus respuestas deben ser breves, naturales y directas.
Si deseas hablar verbalmente con el usuario, DEBES usar tu herramienta 'text_to_speech' pasándole lo que quieres decir.
Asegúrate de ser empático y mantener el tono de una charla agradable."""

    while True:
        user_input = input("\n👤 Tú: ")
        
        if user_input.lower() in ['salir', 'exit', 'quit']:
            print("Hasta luego. ¡Proceso terminado! 👋")
            break
            
        if not user_input.strip():
            continue
            
        messages.append({"role": "user", "content": user_input})
        
        try:
            response = client.messages.create(
                model="claude-4-6-sonnet-latest",
                max_tokens=1024,
                system=system_prompt,
                tools=tools,
                messages=messages
            )
        except Exception as e:
            print(f"\n❌ Se produjo un error al contactar la API de Anthropic: {e}")
            break
            
        messages.append({
            "role": "assistant",
            "content": response.content
        })
        
        # Imprimir respuesta en texto
        for block in response.content:
            if block.type == "text":
                print(f"\n🤖 [Claude - Texto]: {block.text}")
        
        # Procesar herramientas
        if response.stop_reason == "tool_use":
            tool_outputs = []
            
            for block in response.content:
                if block.type == "tool_use":
                    tool_result = process_tool_call(block.name, block.input)
                    
                    tool_outputs.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": str(tool_result)
                    })
            
            messages.append({
                "role": "user",
                "content": tool_outputs
            })
            
            # Segunda llamada de confirmación si usó herramientas
            try:
                final_response = client.messages.create(
                    model="claude-4-6-sonnet-latest",
                    max_tokens=1024,
                    system=system_prompt,
                    tools=tools,
                    messages=messages
                )
                messages.append({
                    "role": "assistant",
                    "content": final_response.content
                })
                
                for block in final_response.content:
                    if block.type == "text":
                        print(f"\n🤖 [Claude - Texto Confirmación]: {block.text}")
            except Exception as e:
                print(f"\n❌ Error en la segunda llamada: {e}")

if __name__ == "__main__":
    run_conversational_agent()
