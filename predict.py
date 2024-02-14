from ultralytics import YOLO
from PIL import Image

# model = YOLO(f'models/sunxds_0.2.9.6.pt', task='detect')

# # Load a model
model = YOLO('model/yolov8n-pose.pt', task='pose')  # pretrained YOLOv8n model

# # Run inference on 'bus.jpg' with arguments
# model.predict(
#     source = 'data/bus.jpg', 
#     conf=0.5,
#     iou = 0.7,
#     imgsz = 640,
#     visualize = True,
#     class = [],
#     imgsz=640,
#     show = True,
#     save = True,
#     save_frames = True,
#     save_txt = True,
#     save_crop = True,
#     show_labels = True,
#     show_boxes = True
#     )

# Run inference on 'bus.jpg'
results = model('data/validate/test1.png', imgsz=640)  # results list

# View results
for r in results:
    print(r.probs)
    boxes_array = r.keypoints.xy
    target = boxes_array[0, :, :].cpu().numpy()
    print(target[0])
    print(target[0][0])


# for r in results:
#     r.save_txt(txt_file ='data/results/prediction.txt' , save_conf=False)
#     r.save_crop(save_dir='data/results', file_name='im')
#     im_array = r.plot(kpt_radius=1)  # plot a BGR numpy array of predictions
#     im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
#     im.show()  # show image
#     im.save('data/results/test1.png')  # save image