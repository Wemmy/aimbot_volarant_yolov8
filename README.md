<div align="center">
  <p>
      <img width="75%" src="https://github.com/Wemmy/yolov8_aimbot-main/blob/main/media/test.gif"></a>
  </p>
</div>

## Overview

This work is a fine-tuned version of [yolov8_aimbot](https://github.com/SunOner/yolov8_aimbot/tree/main). The main features include:
  1. add training stages to existing pipline. 
  2. Transfer learning to detect Volarant characters. 
  3. Add pose estimation model to imporve accuracy on head shot.

## Installation

For installation please follow guide in [yolov8_aimbot](https://github.com/SunOner/yolov8_aimbot/tree/main)

## Tested Environment

### Below is my testing environment

<table>
  <thead><tr><th>GPU:</th><td>NVIDIA GeForce GTX 1660 Ti</td></tr></thead>
  <thead><tr><th>Windows</th><td>11</td></thead>
  <thead><tr><th>NVIDIA CUDA:</th><td>12.3</td></tr></thead>
  <thead><tr><th>NVIDIA cuDNN:</th><td>8.7.0</td></thead>
  <thead><tr><th>TensorRT:</th><td>8.6.1</td></tr></thead>
  <thead><tr><th>Python:</th><td>3.11.0</td></tr></thead>
  <thead><tr><th>PyTorch:</th><td>2.1.2+cu121</td></tr></thead>
  <thead><tr><th>Ultralytics:</th><td>8.1.9</td></tr></thead>
  <thead><tr><th>OpenCV:</th><td>4.9.0.80</td></tr></thead>
  <thead><tr><th>NumPy:</th><td>1.26.0</td></tr></thead>
</table>

## To use the framework

Prepare training dataset:

- take screenshot of different agents in various postions
- crop the image to size 640
- label pose location following this [link](https://docs.ultralytics.com/datasets/pose/#ultralytics-yolo-format)

Train the model.

```cmd
python train.py
```

Using the model

```cmd
python run.py
```

## trainng parameter settings

- pertrained_model_path `str` : start with a pretrained pose model for a better result
- train_data_path `str` : traning data path (need to set up dataset based on this [site](https://docs.ultralytics.com/datasets/pose/))
- optimizer `str`: play with adaptvie optimizer for pose estimation
- cosine_lr `bool`: cosine decay may heep with training
- freeze_layer `int`: transfer leaning, freeze weight of backbone
