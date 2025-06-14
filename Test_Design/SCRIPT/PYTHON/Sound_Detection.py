import sounddevice as sd
import numpy as np
import time

# Configurações
DURATION = 2 # segundos de captura
THRESHOLD_DB = -35 # limiar em decibéis (ajuste entre -50 e -20 conforme necessário)
SAMPLE_RATE = 44100 # taxa de amostragem

def detectar_chime(audio_data):
    # RMS da amplitude
    rms = np.sqrt(np.mean(np.square(audio_data)))
    # Evita log de zero com um valor mínimo muito pequeno
    rms = max(rms, 1e-10)
    volume_db = 20 * np.log10(rms)
    
    print(f"Volume RMS: {rms:.6f} | Volume (dB): {volume_db:.2f} dB")
    
    return volume_db > THRESHOLD_DB

def capturar_audio():
    print("🎙️ Iniciando detecção de chimes (Ctrl+C para parar)...")
    try:
        while True:
            audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='float32')
            sd.wait()
            audio = np.squeeze(audio)
            if detectar_chime(audio):
                print("🔔 Chime detectado!")
            else:
                print("🔇 Nenhum chime detectado.")
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\n🛑 Encerrado pelo usuário.")

if __name__ == "__main__":
    capturar_audio()
