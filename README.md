# Elemantra

Elemantra: An End-to-End Automated Framework Empowered with AI and IoT for Tackling Human-Elephant Conflict in Elephant-Range Countries

#### [Paper Link]() | [Project Page](https://nuwansribandara.github.io/elemantra/) 

## Citation

If you find our work, this repository, or novel algorithms or annotated datasets useful, please consider giving a star ⭐ and citing our [paper]().
```bibtex
@InProceedings{Bandara_2024_APSCON,
    author    = {Bandara, Nuwan Sriyantha and Bandara, Dilshan Pramudith},
    title     = {Elemantra: An End-to-End Automated Framework Empowered with AI and IoT for Tackling Human-Elephant Conflict in Elephant-Range Countries},
    booktitle = {IEEE Sensors Letters},
    month     = {},
    year      = {2024},
    pages     = {}
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
* **(Oct 2, 2023)** 
  * Base python codes for the novel algorithms in [Elemantra](), along with annotated datasets, are released.

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

Solarized dark             |  Solarized Ocean          |  Solarized Ocean
:-------------------------:|:-------------------------:|:-------------------------:
![](https://github.com/NuwanSriBandara/Elemantra/blob/main/Figures/detection_results_3.jpg)  |  ![](https://github.com/NuwanSriBandara/Elemantra/blob/main/Figures/detection_results.png) |  ![](https://github.com/NuwanSriBandara/Elemantra/blob/main/Figures/detection_results_2.png)

### 2. Seismic-based elephant detection


### 3. Hardware design


### 4. Repelling system


<!--- ## Acknowledgements
Our code borrows heavily from [DGCNN](https://github.com/WangYueFt/dgcnn) repository. We thank the authors of DGCNN for releasing their code. If you use our model, please consider citing them as well. -->

