<div align="center">
  <p>
      <img width="75%" src="https://github.com/Wemmy/yolov8_aimbot-main/blob/main/media/test.gif"></a>
  </p>
</div>

## Overview

This work is a fined tune version of yolov8_aimbot(https://github.com/SunOner/yolov8_aimbot/tree/main). The main features are 1. add training features to existing pipline. 2. Fine tuned model to detect Volarant characters. 3. Add pose estimation model to imporve accuracy on head shot

## Installation

For installation please follow guide in yolov8_aimbot(https://github.com/SunOner/yolov8_aimbot/tree/main)

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

Run in console:

```cmd
python train.py
```

- `model="model_path/model_name.pt"`: Path to model.
- `format=engine`: TensorRT model format.
- `half=true`: Use Half-precision floating-point format.
- `device=0`: GPU id.
- `workspace=8`: GPU max video memory.
- `imgsz=320`: Model image size.
- `verbose=False`: Debug stuff. Convenient function, can show errors when exporting.
