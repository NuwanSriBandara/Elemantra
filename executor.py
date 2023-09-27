from modifying_bee_sound import *
from compute_spectra_corr import *
from seismic_utils import *

def executor(task):
  if(task == 'seismic'):
    print('Executing the proposed algorithm on sample seismic data')
    retrieve_output_seismic('./data/sample_seismic_data/data.csv')

  elif(task =='bee-modify'):
    print('Executing the proposed algorithms on sample bee sound data')
    audio1 = retrieve_input("./data/sample_bee_sounds/bee_sound_1.mp3")
    audio2 = retrieve_output("./data/sample_bee_sounds/bee_sound_1.mp3")
    D1, D2 = generate_spectra(audio1, audio2)
    max_corr, _ = compute_corr(D1, D2)

if __name__ == "__main__":
  executor()

