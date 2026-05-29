
import pyaudio
import wave
import numpy as np

# print("Seconds to record:")
# timer = int(input())

# Recording parameters
FORMAT = pyaudio.paInt16  # 16-bit resolution
CHANNELS = 1              # Mono audio
RATE = 44100              # Sample rate (44.1 kHz)
CHUNK = 1024              # Frames per buffer
RECORD_SECONDS = 5
OUTPUT_FILENAME = "output.wav"

def record_audio():
    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Open stream
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    print("Recording...")

    frames = []
    # Capture data in chunks
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        da = np.frombuffer(data,dtype=np.int16)
        daFourier = np.fft.rfft(da)
        frequencies = np.fft.fftfreq(len(da),1/RATE)
        frames.append(data)
        print(frequencies)

    print("Finished recording.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded data as a WAV file
    waveFile = wave.open(OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    print(f"Audio saved to {OUTPUT_FILENAME}")
    return

if __name__ == '__main__':
    record_audio()