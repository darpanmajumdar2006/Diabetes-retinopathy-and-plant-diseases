# Diabetes Retinopathy and Plant Disease Detection

This repository contains two independent deep learning projects focused on medical and agricultural image analysis:

- `plant_disease/`: plant disease classification and explainability pipeline
- `diabetic_retinopathy/`: diabetic retinopathy detection and explainability pipeline

## Repository structure

```text
.
├── plant_disease/
│   ├── __init__.py
│   ├── data/
│   │   └── .gitkeep
│   ├── notebooks/
│   │   ├── plant_disease.ipynb
│   │   └── .gitkeep
│   ├── models/
│   │   └── .gitkeep
│   ├── xai/
│   │   ├── __init__.py
│   │   └── gradcam.py
│   └── results/
│       ├── gradcam/
│       │   └── .gitkeep
│       ├── confusion_matrix.png
│       ├── training_curve.png
│       └── .gitkeep
├── diabetic_retinopathy/
│   ├── __init__.py
│   ├── data/
│   │   └── .gitkeep
│   ├── notebooks/
│   │   ├── diabetic_retinopathy.ipynb
│   │   └── .gitkeep
│   ├── models/
│   │   └── .gitkeep
│   ├── xai/
│   │   ├── __init__.py
│   │   └── gradcam.py
│   └── results/
│       ├── gradcam/
│       │   └── .gitkeep
│       ├── confusion_matrix.png
│       ├── training_curve.png
│       └── .gitkeep
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE (optional)
```

## Project goals

- Detect diabetic retinopathy from retinal fundus images
- Detect plant diseases from crop leaf images
- Use explainable AI techniques such as Grad-CAM for model interpretability
- Provide a modular and reusable training workflow for each problem domain

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# or .venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

## Data organization

- `data/`: raw or processed datasets
- `notebooks/`: exploratory notebooks and experiments
- `models/`: trained model weights
- `xai/`: explainability utilities like Grad-CAM
- `results/`: charts, confusion matrices, and saliency maps

## Suggested stack

- Python
- PyTorch
- TorchVision
- OpenCV
- NumPy
- Matplotlib
- scikit-learn
- pandas
- seaborn
