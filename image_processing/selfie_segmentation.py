import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_selfie_segmentation = mp.solutions.selfie_segmentation

IMAGE_FILES = []
BG_COLOR = (192, 192, 192) #grey
MASK_COLOR = (255, 255, 255)#WHITE  
with mp_selfie_segmentation.SelfieSegmentation(
    model_selection=0) as selfie_segmentation:
  for idx, file in enumerate(IMAGE_FILES):
    image = cv2.imread(file)
    image_height, image_width, _ = image.shape

