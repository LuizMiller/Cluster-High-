import sounddevice as sd
import numpy as np
import scipy.signal as signal
import time

# Configurações
DURATION = 2  # segundos de captura
THRESHOLD_DB = -35  # limiar em decibéis
SAMPLE_RATE = 44100  # taxa de amostragem

def filtrar_audio(audio_data):
    # Definindo as frequências de corte para o filtro passa-banda, por exemplo 700 Hz a 850 Hz
    low_freq = 700.0
    high_freq = 850.0
    # Calcula o filtro passa-banda
    b, a = signal.butter(4, [low_freq, high_freq], btype='band', fs=SAMPLE_RATE)
    # Filtra o áudio
    filtered_audio = signal.lfilter(b, a, audio_data)
    return filtered_audio

def detectar_chime(audio_data):
    # RMS da amplitude
    rms = np.sqrt(np.mean(np.square(audio_data)))
    # Evita log de zero com um valor mínimo muito pequeno
    rms = max(rms, 1e-10)
    volume_db = 20 * np.log10(rms)
    print(f"Volume RMS: {rms:.6f} | Volume (dB): {volume_db:.2f} dB")
    return volume_db > THRESHOLD_DB

def analisar_frequencia(audio_data):
    # Executa FFT no áudio
    fft_data = np.fft.fft(audio_data)
    # Frequências correspondentes
    freqs = np.fft.fftfreq(len(audio_data), 1 / SAMPLE_RATE)
    # Toma a magnitude do FFT
    magnitude = np.abs(fft_data)
    # Obtém a frequência dominante (excluindo frequências negativas)
    dominant_freq_index = np.argmax(magnitude[:len(magnitude) // 2])
    dominant_freq = abs(freqs[dominant_freq_index])
    return dominant_freq

def capturar_audio():
    print("🎙️ Iniciando detecção de chimes (Ctrl+C para parar)...")
    try:
        while True:
            audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='float32')
            sd.wait()
            audio = np.squeeze(audio)

            if detectar_chime(audio):
                filtered_audio = filtrar_audio(audio)
                freq_dominante = analisar_frequencia(filtered_audio)
                print("🔔 Chime detectado!")
                if freq_dominante > 0:
                    periodo = 1 / freq_dominante
                    print(f"📈 Frequência Dominante: {freq_dominante:.2f} Hz | Período: {periodo:.4f} segundos")
            else:
                print("🔇 Nenhum chime detectado.")

            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\n🛑 Encerrado pelo usuário.")

if __name__ == "__main__":
    capturar_audio()
