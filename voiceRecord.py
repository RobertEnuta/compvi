
import pyaudio
import wave
import numpy as np
from scipy.io.wavfile import write

# print("Seconds to record:")
# timer = int(input())

# Recording parameters
FORMAT = pyaudio.paInt16  # 16-bit resolution
CHANNELS = 1              # Mono audio
RATE = 44100              # Sample rate (44.1 kHz)
LOWER_RATE = 30870             # Lower sample rate 
CHUNK = 4096 #1024              # Frames per buffer
RECORD_SECONDS = 5
OUTPUT_FILENAME = "output.wav"

def record_audio():
    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Open stream
    streamIn = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    print("Recording...")

    streamOut = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=LOWER_RATE, input=True,
                        frames_per_buffer=CHUNK)
    frames = []
    frames2 = []
    # Capture data in chunks
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = streamIn.read(CHUNK)
        data2 = streamOut.read(CHUNK)

        frames.append(data)
        frames2.append(data2)
        

    print("Finished recording.")

    # Stop and close the stream
    streamIn.stop_stream()
    streamIn.close()
    streamOut.stop_stream()
    streamOut.close()
    audio.terminate()

    # Save the recorded data as a WAV file
    waveFile = wave.open(OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    waveFile = wave.open("output2.wav", 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames2))
    waveFile.close()

    print(f"Audio saved to {OUTPUT_FILENAME}")
    return

if __name__ == '__main__':
    record_audio()