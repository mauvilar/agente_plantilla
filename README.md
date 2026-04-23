# 🤖 Agent Template con Anthropic API (Claude 3.5)

¡Bienvenido a **Agent Template**! 🚀

Esta es una plantilla en Python diseñada como punto de partida para construir agentes de inteligencia artificial avanzados y autónomos, impulsados por la API de Anthropic (Claude 3.5 Sonnet). 

Esta plantilla va más allá de un simple chat: dota a Claude de capacidades reales sobre el sistema de archivos local mediante el uso de herramientas (*Tool Use* / *Function Calling*).

## ✨ ¿Qué hace especial a este modelo base?

El agente base se comporta como un **asistente de gestión de documentos**. Puede analizar, razonar, generar y modificar archivos físicos en un solo flujo de trabajo ininterrumpido.

Viene con dos herramientas pre-integradas:
- 📖 `read_document`: Permite al asistente leer cualquier documento de texto, código fuente o Markdown que esté en tu computadora.
- ✍️ `write_document`: Otorga al modelo la habilidad de redactar, guardar y sobrescribir archivos con la información nueva, estructurada o revisada.

### ✅ Casos de uso ideales:
- **Refactorización de código:** Pídele que lea un archivo de Python mal estructurado y que escriba una versión limpia en la misma ruta.
- **Revisión de ortografía/estilo:** Haz que lea un texto denso y pida que reescriba el documento aplicando estilo corporativo.
- **Data extraction:** Extrae resumen o insights de un documento voluminoso y pudes pedirle que lo escriba en un bonito formato *Markdown*.

---

## ⚙️ Requisitos Previos

- [Python 3.8+](https://www.python.org/)
- Una clave de API válida de [Anthropic](https://console.anthropic.com/).

## 🚀 Instalación y Uso Rápido

**1. Clona este repositorio:**
```bash
git clone https://github.com/TU_USUARIO/agent-template-anthropic.git
cd agent-template-anthropic
```

**2. Crea tu entorno virtual e instala las dependencias:**
```bash
python -m venv venv
source venv/bin/activate  # En Windows usa: venv\Scripts\activate
pip install -r requirements.txt
```

**3. Configura tus credenciales:**
Copia la plantilla de variables de entorno incluida en el repositorio:
```bash
cp .env.example .env
```
Abre tu nuevo archivo `.env` y reemplaza el valor con tu clave privada real:
```env
ANTHROPIC_API_KEY=sk-ant-...
```

**4. ¡Pon a trabajar a tu Agente!**
Inícialo para interactuar mediante la consola interactiva:
```bash
python agent.py
```
O pásale directamente su misión mediante la línea de comandos:
```bash
python agent.py "Hola, por favor lee mi archivo notas.txt y conviértelo en un documento elegante llamado salida_final.md"
```

---

## 🛠️ Escalabilidad (Construye tu propio ecosistema)

Esta plantilla está pensada para crecer contigo. Puedes inyectar **tus propias funciones de Python**, limitadas únicamente por tu imaginación:

1. Programa una lógica en tu script. Ejemplo: `def consultar_clima(ciudad): ...`
2. Define su `input_schema` dentro del array `tools` en el código de `agent.py`.
3. Captura el llamado a la herramienta dentro de la función `process_tool_call()`.

¡De esta forma puedes diseñar agentes que interactúen con bases de datos, consulten internet, envíen correos electrónicos o dirijan motores robóticos!

---

## 📜 Licencia

Este proyecto está bajo la Licencia **MIT**. Siéntete libre de adaptarlo, llevarlo a tus propios proyectos y crear cosas increíbles, tanto personales como empresariales.
