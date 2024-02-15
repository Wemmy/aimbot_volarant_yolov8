from ultralytics import YOLO
from logic.config_watcher import Config
cfg = Config()

# Load a model
model = YOLO(cfg.pertrained_model_path)  # pretrained YOLOv8n model

# Train the model
results = model.train(
    data=cfg.train_data_path, 
    epochs=cfg.num_epoch, 
    imgsz=640,
    save = cfg.save_checkpoint,
    project = cfg.train_output_path,
    optimizer = cfg.optimizer,
    verbose = cfg.verbose,
    exist_ok = True,
    single_cls = True,
    cos_lr= cfg.cosine_lr,
    freeze = cfg.freeze_layer,
    lr0 = cfg.learning_rate,
    momentum = cfg.momentum,
    pose = cfg.pose_loss_weight,
    kobj = cfg.keypoint_objectness_loss_weight
    )

