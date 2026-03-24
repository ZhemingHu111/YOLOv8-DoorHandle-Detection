# Door Handle Detection using YOLOv8

This project implements a deep learning model to detect door handles using the YOLOv8 architecture. The model was trained and validated on a custom dataset.

## Project Status: Completed
- **Training Environment**: Local machine with **NVIDIA GeForce RTX 4060 Ti**.
- **Epochs**: 50
- **Framework**: Ultralytics YOLOv8

## Repository Structure
- `main.py`: Entry point for the training pipeline.
- `args.py`: Configuration file for paths and hyperparameters.
- `dataset.py`: Script for generating `data.yaml` and handling dataset metadata.
- `trainer.py`: Logic for model initialization and training execution.
- `results/`: Contains performance metrics and visual predictions.

## Training Results
The model achieved high precision and recall within 50 epochs. Detailed metrics (F1 Curve, Precision-Recall Curve, and Loss Plots) are available in the `results/` folder.

- **Learning Curve**: See `results/results.png` for training and validation loss.
- **Sample Prediction**: See `results/val_batch0_pred.jpg` for model inference on the validation set.

## Note on Dataset
Due to the file size and GitHub upload constraints for large image batches, the raw dataset (**images** and **label .txt files**) is not included in this repository. 

**However, the full training process, dataset structure, and successful execution have been demonstrated and submitted via the required screen recording on the school portal.**
