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
  * Base python codes for the novel algorithms in [Elemantra](), along with annotated datasets are released.

## Dependencies

Refer `requirements.txt` for the required essential packages.

```
pip install -r requirements.txt
```

## Data

Datasets are available [here](https://drive.google.com/drive/folders/1dAH9R3XDV0z69Bz6lBaftmJJyuckbPmR?usp=sharing). Run the command below to download all the datasets (ShapeNetRender, ModelNet40, ScanObjectNN, ShapeNetPart) to reproduce the results.

```
cd data
source download_data.sh
```

## Train CrossPoint

Refer `scripts/script.sh` for the commands to train CrossPoint.

## Downstream Tasks

### 1. 3D Object Classification 

Run `eval_ssl.ipynb` notebook to perform linear SVM object classification in both ModelNet40 and ScanObjectNN datasets.


### 2. Few-Shot Object Classification

Refer `scripts/fsl_script.sh` to perform few-shot object classification.

### 3. 3D Object Part Segmentation

Refer `scripts/script.sh` for fine-tuning experiment for part segmentation in ShapeNetPart dataset.

## Acknowledgements
Our code borrows heavily from [DGCNN](https://github.com/WangYueFt/dgcnn) repository. We thank the authors of DGCNN for releasing their code. If you use our model, please consider citing them as well.

