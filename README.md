# Elemantra

Elemantra: An End-to-End Automated Framework Empowered with AI and IoT for Tackling Human-Elephant Conflict in Elephant-Range Countries

By [Nuwan Bandara](https://sites.google.com/view/nuwan-bandara/) and [Dilshan Bandara](https://www.linkedin.com/in/dilshan--bandara/)

#### [Paper Link](https://arxiv.org/abs/2310.15012) | [Project Page](https://nuwansribandara.github.io/Elemantra/) | [EleThermal Dataset](https://github.com/NuwanSriBandara/Elemantra/tree/main/data/Thermal_Elephant_Dataset)

## Citation

If you find our work, this repository, or novel algorithms or annotated datasets useful, please consider giving a star ⭐ and citing our [paper](https://arxiv.org/abs/2310.15012).
```bibtex
@misc{bandara2023elemantra,
      title={Elemantra: An End-to-End Automated Framework Empowered with AI and IoT for Tackling Human-Elephant Conflict in Elephant-Range Countries}, 
      author={Nuwan Sriyantha Bandara and Dilshan Pramudith Bandara},
      year={2023},
      eprint={2310.15012},
      archivePrefix={arXiv},
      primaryClass={eess.SY}
}
```

# :rocket: News

<!---
 * **(Mar 25, 2023)**

# * An implementation supporting PyTorchDistributedDataParallel (DDP) is available [here](https://github.com/auniquesun/CrossPoint-DDP). Thanks to [Jerry Sun](https://auniquesun.github.io/)

# * **(Mar 2, 2022)**

#  * Paper accepted at CVPR 2022 :tada: your comment goes here
and here
-->

* **(Nov 13, 2024)** 
  * Our paper is accepted at [APSCON 2025](https://2025.ieee-apscon.org/)

* **(Nov 1, 2023)** 
  * Infrared Elephant Image Annotated Dataset ('[EleThermal](https://github.com/NuwanSriBandara/Elemantra/tree/main/data/Thermal_Elephant_Dataset)' dataset) is released.

* **(Oct 24, 2023)** 
  * Base Python codes for the novel algorithms in [Elemantra](https://arxiv.org/abs/2310.15012) are released.

## Dependencies

Refer `requirements.txt` for the required essential packages.

```
pip install -r requirements.txt
```

## Data

Configure the datapaths in config.yaml for each task (i.e. seismic-based elephant detection, modified bee sound-based elephant repelling and infrared signature-based elephant detection) as in the folder structure of this repository after adding more data points, especially for seismic-based elephant detection and modified bee sound-based elephant repelling, as required. 

Note: The sample data for bee sound processing and seismic signal processing are in sample_bee_sounds (retrieved from [here](https://zenodo.org/record/1321278)) and sample_seismic_data folders (retrieved from [here](https://zenodo.org/record/4642565)) respectively. The annotated dataset for infrared image-based elephant detection is in the dataset: elephant_detection (the respective images are collected from [here](https://github.com/arribada/human-wildlife-conflict) and annotated by this project). Therefore, if you use, by any means, data and/or proposed algorithms, please cite the above sources accordingly, along with our work. 

## Usage

Execute the tasks
```
# execute entire pipeline with default task: seismic-based elephant detection
python3 main.py
```
Other forms of execution
```
# execute entire pipeline for the task: modified bee sound-based elephant repelling. Note that the spectrogram correlation calculations usually takes a considerable time to execute
python3 main.py --task=bee-modify
```

## Results

### 1. Infrared signature-based elephant detection

Elephant detection instances in test infrared set using tflite model

 with high confidence      |  one retrieved from [here](https://github.com/arribada/human-wildlife-conflict)          |   one which failed to detect multiple elephants
:-------------------------:|:-------------------------:|:-------------------------:
![](https://github.com/NuwanSriBandara/Elemantra/blob/main/Figures/detection_results_3.jpg)  |  ![](https://github.com/NuwanSriBandara/Elemantra/blob/main/Figures/detection_results.png) |  ![](https://github.com/NuwanSriBandara/Elemantra/blob/main/Figures/detection_results_2.png)

### 2. Seismic-based elephant detection

Elephant detection instance using seismic recordings

 frequency distribution             |  detection in STFT plot         |  detection using proposed method
:-------------------------:|:-------------------------:|:-------------------------:
![](https://github.com/NuwanSriBandara/Elemantra/blob/main/Figures/fft_analysis.png)  |  ![](https://github.com/NuwanSriBandara/Elemantra/blob/main/Figures/spectrogram_figure.png) |  ![](https://github.com/NuwanSriBandara/Elemantra/blob/main/Figures/recorded_signal_figure.png)
 

### 3. Repelling system

STFT spectrogram plots of one:

 original bee sound segment of 4𝑠         |  corresponding modified bee sounds through randomly changing the FR         |  corresponding modified bee sounds through randomly adding an overlay of pink noise
:-------------------------:|:-------------------------:|:-------------------------:
![](https://github.com/NuwanSriBandara/Elemantra/blob/main/Figures/spectro_original_audio.png)  |  ![](https://github.com/NuwanSriBandara/Elemantra/blob/main/Figures/spectro_modified_audio_method_1.png) |  ![](https://github.com/NuwanSriBandara/Elemantra/blob/main/Figures/spectro_modified_audio_method_2.png)

## Acknowledgements
Authors would like to extend their gratitude to Dr. [Mukunthan Tharmakulasingam](https://scholar.google.com/citations?user=EKVOAysAAAAJ&hl=en) from the University of Surrey, United Kingdom, Dr. [Chamira Edussooriya](https://scholar.google.com/citations?hl=en&user=qe5byo4AAAAJ), Ms. Anjalie Kalansooriya and Mr. Derek Nanayakkara from the University of Moratuwa, Sri Lanka for their valuable suggestions.

