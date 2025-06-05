import numpy as np
import wave
import os

def generate_beep(filename, duration_ms, frequency=1000, volume=0.5, sample_rate=44100):
    n_samples = int(sample_rate * (duration_ms / 1000.0))
    t = np.linspace(0, duration_ms / 1000.0, n_samples, False)
    tone = np.sin(frequency * 2 * np.pi * t) * volume
    tone = (tone * 32767).astype(np.int16)

    with wave.open(filename, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 2 bytes per sample
        wf.setframerate(sample_rate)
        wf.writeframes(tone.tobytes())

# Make the sounds directory
os.makedirs("sounds", exist_ok=True)

# Generate dot.wav (short beep)
generate_beep("sounds/dot.wav", duration_ms=150)

# Generate dash.wav (long beep)
generate_beep("sounds/dash.wav", duration_ms=400)

print("✅ dot.wav and dash.wav created in the 'sounds' folder.")
