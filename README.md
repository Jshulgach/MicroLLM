<div align=center>

<p align="center">
<img src="./assets/dancing-llama.gif" width="720">
</p>

</div>

# About MicroLLM

The world's first real-time voice assistant that runs entirely on a Raspberry Pi Pico W, powered by Groq’s LLaMA API and ElevenLabs for high-quality, with natural-sounding speech—played through a DAC via I2S audio output.

## ✨ Features 
- 🤖 Contextual LLM Responses powered by Groq's blazing-fast LLaMA API
- 🔊 Real-Time natural Text-to-Speech using ElevenLabs' pcm_24000 audio stream output via I2S DAC
- 📶 Wi-Fi Connectivity with CircuitPython for true IoT integration
- 🧠 Fully embedded experience — no need for a PC or Raspberry Pi OS!

## 🛠️ Setup

### Hardware Requirements 
- Raspberry Pi Pico W
- MAX98357A I2S DAC
- 4-to-8 Ohm Speaker (connected to the DAC)
- Optional: Breadboard, jumpers, 5V USB power

### Wiring

| Pico Pin	| MAX98357A Pin |
| --------- | ------------- |
| GP1	| BCLK |
| GP0	 | LRCK |
| GP9	| DIN |
| GND	| GND |
| 3V3	| VDD |

Make sure the speaker is connected to + and - on the DAC.

### Software

1. Choose Pico firmware

    We have provided CircuitPython firmware for both the Pico and Pico2! Choose the right uf2 file for your Pico version, or download the [CircuitPython](https://circuitpython.org/) latest firmware for the [Pico](https://circuitpython.org/board/raspberry_pi_pico/) or [Pico 2](https://circuitpython.org/board/raspberry_pi_pico_2/). 

2. Move/drag the uf2 file to the Pico drive.
   - When you plug in the Pico for the first time, you should see a new drive appear on your computer with the Poci in bootloader mode. You can always access this by pressing the BOOTSEL button while plugging in the Pico.
   ![](assets/pico_first_time.PNG)
   - Move/drag the uf2 file to the Pico drive. The Pico will automatically reboot and the LED will turn green to indicate successful flashing.

3. Replace the contents of the `code.py` and `lib` folder to the Pico drive.

4. Update the `settings.toml` file on the pico with your API keys:
   ```
   CIRCUITPY_WIFI_SSID = "YourWiFiNetwork"
   CIRCUITPY_WIFI_PASSWORD = "YourPassword"
   ELEVENLABS_API_KEY = "your-elevenlabs-api-key"
   GROQ_API_KEY = "your-groq-api-key"
   ```


## Demo
The script contained in the `code.py` file will send a "Hello World!" message to the Eleven Labs API which should play if everything is working!

You can check out the other scripts in the `examples` folder to play with the LLM functionality


## 🙌 Acknowledgements

[Adafruit CircuitPython](https://circuitpython.org/)

[ElevenLabs](https://elevenlabs.io/docs/overview)

[Groq Cloud Inference](https://groq.com/)
