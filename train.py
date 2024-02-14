from ultralytics import YOLO

# Load a model
model = YOLO('yolov8m-pose.pt')  # pretrained YOLOv8n model

# Train the model
results = model.train(
    data='volarant-pose.yaml', 
    epochs=100, 
    imgsz=640,
    name = 'Volarant',
    exist_ok = True,
    single_cls = True,
    cos_lr= True
    )

