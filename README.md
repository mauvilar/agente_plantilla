# 🤖 Agent Template con Anthropic API (Claude 3.5)

¡Bienvenido a **Agent Template**! 🚀

Esta es una plantilla en Python diseñada como punto de partida para construir agentes de inteligencia artificial avanzados y autónomos, impulsados por la API de Anthropic (Claude 3.5 Sonnet). 

Esta plantilla va más allá de un simple chat: dota a Claude de capacidades reales sobre el sistema de archivos local mediante el uso de herramientas (*Tool Use* / *Function Calling*).

## ✨ Plantillas Disponibles

Este repositorio incluye múltiples plantillas de agentes como punto de partida, dependiendo del caso de uso.

### 1. 📄 Agente de Documentos (`agent.py`)

El agente original que se comporta como un **asistente de gestión de documentos**. Puede analizar, razonar, generar y modificar archivos físicos en un solo flujo de trabajo ininterrumpido.

Viene con dos herramientas pre-integradas:
- 📖 `read_document`: Leer cualquier documento de texto o código en tu computadora.
- ✍️ `write_document`: Redactar, guardar y sobrescribir archivos con nueva información.

**Casos de uso:** Refactorización de código, corrección de estilo, y extracción o formateo de datos a Markdown.

### 2. 🎙️ Agente Conversacional de Voz y Texto (`voice_text_agent.py`)

Una variante orientada a la interacción con el usuario de manera directa y dinámica, simulando un asistente amigable usando respuestas activas tanto en texto como sintetizadas en audio.

Viene con una herramienta pre-integrada:
- 🔊 `text_to_speech`: Ejecuta síntesis de voz en el equipo físico (usando el comando macOS `say` por defecto) para que el asistente pueda "hablar" los resultados al usuario en tiempo real.

**Casos de uso:** Asistentes interactivos de escritorio, simulación de atención por voz, o desarrollo de un chatbot amigable con síntesis vocal.

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
