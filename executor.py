from modifying_bee_sound import *
from compute_spectra_corr import *
from seismic_utils import *

def executor(task, datapath):
  if(task == 'seismic'):
    print('Executing the proposed algorithm on sample seismic data')
    retrieve_output_seismic(datapath) #'./data/sample_seismic_data/data.csv'
    print('Done!')

  elif(task =='bee-modify'):
    print('Executing the proposed algorithms on sample bee sound data')
    audio1 = retrieve_input(datapath) # "./data/sample_bee_sounds/bee_sound_1.mp3"
    audio2 = retrieve_output(datapath) # "./data/sample_bee_sounds/bee_sound_1.mp3"
    D1, D2 = generate_spectra(audio1, audio2)
    # max_corr, _ = compute_corr(D1, D2) # note that this step will take a considerable time to execute for large audio files
    print('Done!')

if __name__ == "__main__":
  executor()

