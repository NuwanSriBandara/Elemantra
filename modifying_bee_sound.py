import random
from pydub import AudioSegment
import numpy as np
import time

def time_domain(audio):
  speed_factor = random.uniform(0.8, 1.2)
  pitch_shift = random.uniform(0.95, 1.05)

  #stretched = audio.speedup(playback_speed=speed_factor)
  manipulated_audio = audio.set_frame_rate(int(audio.frame_rate * pitch_shift))

  return manipulated_audio

def freq_domain(bee_sound):
  pink_noise = np.random.normal(0, 0.1, len(bee_sound))
  manipulated_audio = bee_sound.overlay(AudioSegment(pink_noise.tobytes(), frame_rate=bee_sound.frame_rate, sample_width=bee_sound.sample_width, channels=1))

  return manipulated_audio

def modify(audio):
  num_list = [1,2,3]
  # start_time = time.time() # time complexity
  random_num = random.choice(num_list)

  if(random_num==1):
    manipulated = time_domain(audio)
    mod_audio = manipulated.export(f"output_sound_{random_num}.mp3", format="mp3")

  elif(random_num==2):
    manipulated = freq_domain(audio)
    mod_audio = manipulated.export(f"output_sound_{random_num}.mp3", format="mp3")

  elif(random_num==3):
    manipulated = randomized(audio)
    mod_audio = manipulated.export(f"output_sound_{random_num}.mp3", format="mp3")

  # print("--- %s seconds ---" % (time.time() - start_time))

  return mod_audio

def randomized(bee_sound):
  silence_duration = 100  # in milliseconds
  #gap_count = 2
  #varied_sounds = []
  gap_length = random.randint(1, 3) * silence_duration
  gap = AudioSegment.silent(duration=gap_length)
  manipulated_audio = bee_sound.overlay(gap)

  return manipulated_audio

def retrieve_input(filepath):
  audio = AudioSegment.from_file(filepath)
  audio = audio.export(format="mp3")
  return audio

def retrieve_output(filepath):
  audio = retrieve_input(filepath)
  audio = AudioSegment.from_file(audio)
  if(len(audio)<4000):
    audio = modify(audio)
  else:
    audio = audio[:4000]
    audio = modify(audio)

  return audio

# audio = AudioSegment.from_file("/content/drive/MyDrive/bee sound/data/CF003 - Active - Day - (214).wav")

# audio = retrieve_output("/content/drive/MyDrive/bee sound/data/CF003 - Active - Day - (214).wav")
