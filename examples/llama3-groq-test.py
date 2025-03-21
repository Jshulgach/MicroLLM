import os
import json
import ssl
import board
import socketpool
import wifi
import adafruit_requests

# Load API key from settings.toml
groq_api_key = os.getenv("GROQ_API_KEY")
if groq_api_key is None:
    print("Error: Please set GROQ_API_KEY in settings.toml")
    while True:
        pass  # Halt execution

# Connect to WiFi
print("Connecting to WiFi...")
wifi.radio.connect(os.getenv("WIFI_SSID"), os.getenv("WIFI_PASSWORD"))
print("Connected!")

# Create request session
requests = adafruit_requests.Session(socketpool.SocketPool(wifi.radio), ssl.create_default_context())

# Define the question
question = "Tell me a story about a robot"
messages = [{"role": "user", "content": question}]

# Send request to Groq's API
print("Asking:", question)
response = requests.post(
    "https://api.groq.com/openai/v1/chat/completions",
    json={"model": "llama3-8b-8192", "messages": messages},
    headers={"Authorization": f"Bearer {groq_api_key}", "Content-Type": "application/json"},
)

# Print the response
if response.status_code == 200:
    answer = response.json()["choices"][0]["message"]["content"]
    print("Response:", answer)
else:
    print(f"Error {response.status_code}: {response.reason}")
