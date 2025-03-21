import board
import audiocore
import audiobusio
import time

print("Playing 10 times StreetChicken.wav")

f = open("StreetChicken.wav", "rb")
wav = audiocore.WaveFile(f)
i2s = audiobusio.I2SOut(bit_clock=board.GP1, word_select=board.GP0, data=board.GP9)
#GPIO9 to DIN (serial data)
#GPIO1 is connected to the BCK input (bit clock)
#GPIO0 to LRCK (left or right clock)


for i in range(10):
    start=time.monotonic()
    i2s.play(wav)
    while i2s.playing:
        pass
    stop = time.monotonic()
    print("Total lenght = ", stop, "-", start, "=", stop-start)