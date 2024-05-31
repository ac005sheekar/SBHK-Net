# YOLO/SBHK-Net: Occlusion Aware Robot Vision Neural Network with Compound Model Scaling and Re-parameterized Convolution

Robot Vision is the technique of enabling robots to process visual data from the environment by utilizing a combination of camera hardware and computer algorithms. 
Advanced deep neural networks have significantly played a vital role in indulging robots to make more sense out of complex visual data at different circumstances, 
especially in object detection and continuous tracking. In this research, we initiated a unique and cutting-edge backbone neural network for the conventional YOLO algorithm 
which we named as SBHK-Net. The network boosted up the performance of the existing YOLO algorithm drastically which manifests a strong potential of improving tracking and 
recognition accuracies of other conventional algorithms in the robot vision industry as well. It has the greatest accuracy 59.2% AP among all known real-time object detectors 
with 30 FPS or above on GPU RTX3060, and it outperforms all other known object detectors in the range of 5 FPS to 160 FPS. We used YOLOv7 as our reference point for the core research. 
The transformer-based detector SWINL Cascade-Mask R-CNN (9.2 FPS A100, 53.9% AP) and the convolutional detector ConvNeXt-XL Cascade-Mask R-CNN (8.6 FPS A100, 55.2% AP) are both 
outperformed by the SBHK-Net core object detector (56 FPS RTX3060, 56.4% AP) in terms of speed and accuracy, respectively. In terms of speed and accuracy, it surpasses a number of 
other object detectors, including DINO-5scale-R50, ViT-Adapter-B, Scaled-YOLOv4, YOLOv5, DETR, Deformable DETR, and YOLOR and YoLOX. 

techRxiv Preprint: https://github.com/ac005sheekar/SBHKNet.
