import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import correlate as c1d
from scipy.fft import fft, fftfreq

import obspy
from scipy.signal import spectrogram as spectro

def plot_temporal_graph(x, y, i):
  # plt.ioff()
  plt.plot(x, y)
  plt.savefig(f'temporal_variation_{i}.png')
  plt.show()
  # plt.ion()

def plot_freq_graph(data, sample_rate, i):
  fft_signal = fft(data)
  freq = fftfreq(len(data), 1 / sample_rate)

  # plt.ioff()
  plt.plot(freq, np.abs(fft_signal))
  plt.savefig(f'frequency_variation_{i}.png')
  plt.show()
  # plt.ion()


def calculate_plot_spectro(data, sample_rate, freq_range, time_range, name):
  frequencies, times, spectrogram_data = spectro(
            data, fs=sample_rate, nperseg=400, noverlap=200, nfft=800
        )
  pattern_detected = []
  for i in range(len(times)):
      if times[i] >= time_range[0] and times[i] <= time_range[1]:
          frequency_slice = spectrogram_data[:, i]
          max_freq_index = np.argmax(frequency_slice)
          max_frequency = frequencies[max_freq_index]
          if max_frequency >= freq_range[0] and max_frequency <= freq_range[1]:
              pattern_detected.append(i)

  # Plot the spectrogram and detected patterns
  # plt.ioff()
  plt.figure(figsize=(10, 6))
  plt.pcolormesh(times, frequencies, 10 * np.log10(spectrogram_data), shading='gouraud')
  plt.colorbar(label='Power Spectral Density (dB/Hz)')
  plt.xlabel('Time (seconds)')
  plt.ylabel('Frequency (Hz)')
  plt.title('Spectrogram of Recorded Signal')
  plt.plot(np.array(times)[pattern_detected], frequencies[np.argmax(spectrogram_data[:, pattern_detected], axis=0)], 'ro', markersize=6, label='Detected Patterns')
  plt.legend()
  plt.ylim(freq_range)
  plt.xlim(time_range)
  plt.savefig(f'detected_patterns_spectra_{name}.png')
  # plt.ion()
  plt.show()

def calculate_plot_fft(data, sample_rate, x_values, fm_start, fm_end, duration, name):
  fft_signal = fft(data)
  freq = fftfreq(len(data), 1 / sample_rate)

  # Detect signals with characteristic frequency modulation
  detected_indices = []
  window_size = int(duration * sample_rate)

  for i in range(0, len(data), window_size):
      segment = fft_signal[i:i + window_size]
      segment_freq = freq[i:i+window_size]
      max_freq_idx = np.argmax(np.abs(segment))
      max_freq = segment_freq[max_freq_idx]
      if max_freq >= fm_start and max_freq <= fm_end:
          detected_indices.append(i)

  # plt.ioff()
  plt.figure(figsize=(10, 6))
  plt.plot(x_values, data, label='Recorded Signal')
  plt.plot(np.array(detected_indices) / sample_rate, data[detected_indices], 'ro', markersize=6, label='Detected Patterns')
  plt.xlabel('Time (seconds)')
  plt.ylabel('Amplitude')
  plt.title('Recorded Signal and Detected Patterns')
  plt.legend()
  plt.grid()
  plt.savefig(f'detected_patterns_fft_{name}.png')
  plt.show()
  # plt.ion()

def retrieve_output_seismic(filepath):
  df = pd.read_csv(filepath)

  for j,row in df.iterrows():

      event_num = row['event_num']
      stationlist = [row['station0_seis'],row['station1_seis'],row['station2_seis'],row['station3_seis']]

      for i,station in enumerate(stationlist):

          file = str(event_num)+'_'+station+'_seismic.mseed'
          try:
            seis = obspy.read('./data/sample_seismic_data/sample_data/'+file, format="MSEED", dtype=np.float32)
            data_seis = np.array([tr.data for tr in seis]).transpose()

            x_values = np.arange(len(data_seis))
            sample_rate = 200  # Sample rate in Hz

            # Find the characteristic frequency modulation pattern
            frequency_range = (20, 40)  # Frequency range in Hz
            time_range = (3, 5)  # Duration range in seconds

            plot_temporal_graph(x_values, data_seis[:, 0], file)
            plot_freq_graph(data_seis[:, 0], sample_rate, file)

            # Detect patterns using spectrogram
            calculate_plot_spectro(data = data_seis[:, 0], sample_rate = sample_rate, freq_range = frequency_range, time_range = time_range, name= file)
            # calculate_plot_spectro(data = data_seis[:, 1], sample_rate = sample_rate, freq_range = frequency_range, time_range = time_range)
            # calculate_plot_spectro(data = data_seis[:, 2], sample_rate = sample_rate, freq_range = frequency_range, time_range = time_range)

            # Define frequency modulation characteristics
            fm_start = 20  # Starting frequency in Hz
            fm_end = 40  # Ending frequency in Hz
            duration = 5  # Duration in seconds

            # Detect patterns using fft-based algorithm
            calculate_plot_fft(data = data_seis[:, 0], sample_rate = sample_rate, x_values = x_values, fm_start = fm_start, fm_end = fm_end, duration = duration, name = file)
            # calculate_plot_fft(data = data_seis[:, 1], sample_rate = sample_rate, fm_start = fm_start, fm_end = fm_end, duration = duration)
            # calculate_plot_fft(data = data_seis[:, 2], sample_rate = sample_rate, fm_start = fm_start, fm_end = fm_end, duration = duration)
          except:
            continue

      print(f'{j}_th sample done')

      # break

