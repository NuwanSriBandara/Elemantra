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
[comment]: <> (* **(Mar 25, 2023)**
  * An implementation supporting PyTorchDistributedDataParallel (DDP) is available [here](https://github.com/auniquesun/CrossPoint-DDP). Thanks to [Jerry Sun](https://auniquesun.github.io/))
* **(Mar 2, 2022)**
  * Paper accepted at CVPR 2022 :tada: 
* **(Mar 2, 2022)** 
  * Training and evaluation codes for [CrossPoint](https://openaccess.thecvf.com/content/CVPR2022/html/Afham_CrossPoint_Self-Supervised_Cross-Modal_Contrastive_Learning_for_3D_Point_Cloud_Understanding_CVPR_2022_paper.html), along with pretrained models are released.

## Dependencies

Refer `requirements.txt` for the required packages.

## Pretrained Models

CrossPoint pretrained models with DGCNN feature extractor are available [here.](https://drive.google.com/drive/folders/10TVEIRUBCh3OPulKI4i2whYAcKVdSURn?usp=sharing)

## Download data

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

