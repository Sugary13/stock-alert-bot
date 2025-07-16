# 📊 Stock Alert Bot - Tesla Tracker

Este es un proyecto de automatización que monitorea las acciones de **Tesla Inc. (TSLA)** y envía **notificaciones por SMS** si hay un cambio significativo en el precio (±5%). Si se detecta tal cambio, el programa también recupera las **últimas 3 noticias relevantes** relacionadas con la empresa.

---

## 🚀 Tecnologías utilizadas

- **Python 3**
- [Alpha Vantage API](https://www.alphavantage.co/) – para obtener datos bursátiles diarios
- [NewsAPI](https://newsapi.org/) – para obtener noticias relacionadas
- [Twilio API](https://www.twilio.com/) – para enviar mensajes SMS
- `requests`, `dotenv`, `twilio`

---

## 📦 Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/Sugary13/stock-alert-bot.git
cd stock-alert-bot
```
2. Crea un entorno virtual (opcional pero recomendado):

```
python -m venv venv
source venv/bin/activate  # en Mac/Linux
venv\Scripts\activate     # en Windows
```

3. Instala las dependencias:

```
pip install -r requirements.txt
```

4. Crea un archivo `.env` y agrega tus claves:
```
AVA_API_KEY=tu_clave_alpha_vantage
NEW_API_KEY=tu_clave_newsapi
ACCOUNT_SID=tu_account_sid_twilio
AUTH_TOKEN=tu_auth_token_twilio
MESSAGING_SERVICE_ID=tu_messaging_service_sid
PHONE_NUMBER=tu_numero_telefono_destino
```

⚙️ Cómo funciona
1. Se obtiene el precio de cierre de los últimos dos días con Alpha Vantage.

2. Se calcula el cambio porcentual entre ambos días.

3. Si el cambio es mayor a ±5%:

- Se obtienen 3 noticias relevantes de NewsAPI.

- Se envían mensajes SMS con la información y enlaces a las noticias.

4. Si no hay cambio relevante, el programa simplemente indica un cambio moderado.

🧪 Ejemplo de mensaje SMS

```
📈 Cambio: +6.21%
📰 Tesla to Launch New Model X
Tesla has announced...
https://news.com/tesla-model-x
```

📌 Consideraciones

- El script está enfocado en Tesla Inc., pero puedes cambiar la acción modificando la variable STOCK y COMPANY_NAME.

- Puedes programar este script con cron (Linux/Mac) o el Programador de tareas (Windows) para que corra automáticamente todos los días.

🧑‍💻 Autor

Carlos Esquerra Martínez

GitHub: @Sugary13

LinkedIn: linkedin.com/in/carlos-esquerra-martinez-bba147269

📄 Licencia

Este proyecto es de uso educativo. Las claves API deben mantenerse seguras en el entorno local y no deben subirse a GitHub.
