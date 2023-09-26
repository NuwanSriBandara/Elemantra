import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate2d

def generate_spectra(audio_file1, audio_file2):
  # Load audio data and sample rate
  y1, sr1 = librosa.load(audio_file1)
  y2, sr2 = librosa.load(audio_file2)

  # Compute spectrograms
  D1 = librosa.amplitude_to_db(np.abs(librosa.stft(y1)), ref=np.max)
  D2 = librosa.amplitude_to_db(np.abs(librosa.stft(y2)), ref=np.max)

  # Visualize the spectrograms
  plt.ioff()
  plt.figure(figsize=(12, 8))
  #plt.subplot(2, 1, 1)
  librosa.display.specshow(D1, sr=sr1, x_axis='time', y_axis='log')
  plt.colorbar(format='%+2.0f dB')
  plt.title('Log-frequency Spectrogram of Original Bee Sound')
  plt.tight_layout()
  plt.savefig("1.png")
  plt.ion()
  # plt.show()

  plt.ioff()
  plt.figure(figsize=(12, 8))
  librosa.display.specshow(D2, sr=sr2, x_axis='time', y_axis='log')
  plt.colorbar(format='%+2.0f dB')
  plt.title('Log-frequency Spectrogram of Modified Bee Sound')
  plt.tight_layout()
  plt.savefig("2.png")
  plt.ion()
  # plt.show()

  return D1,D2

# Compare cross-correlation
def compute_corr(D1, D2):
  # Perform cross-correlation between the two spectrograms
  correlation = correlate2d(D1, D2, boundary='symm', mode='same')

  # Find the maximum correlation value and its corresponding time lag
  max_corr = np.max(correlation)
  lag = np.argmax(correlation)

  # print(f"Maximum Correlation: {max_corr}")
  # print(f"Time Lag (in frames): {lag}")

  return max_corr, lag

# Load the two audio files
# audio_file1 = "/content/output_sound_1.mp3"
# audio_file2 = "/content/output_sound_3.mp3"

# D1,D2 = generate_spectra(audio_file1, audio_file2)
# max_corr, log = compute_corr(D1, D2)
