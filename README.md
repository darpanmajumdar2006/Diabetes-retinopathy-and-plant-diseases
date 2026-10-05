# Diabetes Retinopathy and Plant Disease Detection

This repository contains two independent deep learning projects:

- `plant_disease/`: plant disease classification and explainability pipeline
- `diabetic_retinopathy/`: diabetic retinopathy detection and explainability pipeline

## Project structure

```text
.
├── plant_disease/
│   ├── data/
│   ├── notebooks/
│   │   └── plant_disease.ipynb
│   ├── models/
│   │   └── plant_model.pth
│   ├── xai/
│   │   └── gradcam.py
│   └── results/
│       ├── confusion_matrix.png
│       ├── training_curve.png
│       └── gradcam/
├── diabetic_retinopathy/
│   ├── data/
│   ├── notebooks/
│   │   └── diabetic_retinopathy.ipynb
│   ├── models/
│   │   └── dr_model.pth
│   ├── xai/
│   │   └── gradcam.py
│   └── results/
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup

```bash
pip install -r requirements.txt
```

## Notes

- `data/` stores raw or processed datasets
- `notebooks/` contains experiment notebooks
- `models/` stores trained weights
- `xai/` contains explainability scripts such as Grad-CAM
- `results/` stores evaluation metrics, plots, and saliency outputs

## Suggested stack

- Python
- PyTorch
- OpenCV
- Matplotlib
- NumPy
- scikit-learn
- TorchVision
