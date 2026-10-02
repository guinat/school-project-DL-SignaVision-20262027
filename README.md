# SignaVision

Traffic sign recognition with neural networks (GTSRB dataset, 43 classes).
Deep Learning project, CY Tech 2026-2027: Nathan GUIHOT, Elyes DOS SANTOS.

## Structure

```
src/
├── signavision/        # shared code imported by the notebooks
│   ├── config.py       # paths and constants
│   ├── classes.py      # names and families of the 43 classes
│   ├── data.py         # dataset loading
│   └── viz.py          # plot style, figure export
└── 01_data.ipynb       # Part 1: dataset description
report/                 # LaTeX report, in French (notebooks export their figures here)
docs/                   # project subject
data/                   # dataset (not versioned)
```

## Setup

```bash
uv sync
```

Download the dataset from [Kaggle](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign) and extract it into `data/`.
If `data/` does not exist (on Colab for instance), it is downloaded automatically with `kagglehub`.

## Colab

Each notebook clones the repository on startup to access the `signavision` package.

## Report

```bash
cd report && make
```
