import cv2
import numpy as np
from PIL import Image
import streamlit as st
MODEL = "./model/MobileNetSSD_deploy.caffemodel"
CONFIG = "./model/MobileNetSSD_deploy.prototxt.txt"


def process_image(image):
    net = cv2.dnn.readNetFromCaffe(CONFIG, MODEL)
    blob = cv2.dnn.blobFromImage(cv2.resize(
        image, (300, 300)), 0.007843, (300, 300), 127.5)

    net.setInput(blob)
    dections = net.forward()
    return dections


def annotate_image(image, detections, confidence_threshold=0.7):
    h, w = image.shape[:2]
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > confidence_threshold:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (start_x, start_y, end_x, end_y) = box.astype("int")
            cv2.rectangle(image, (start_x, start_y),
                          (end_x, end_y), (0, 255, 0), 2)
    return image


def main():
    st.title('Object Detection for Image')
    file = st.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png'])
    if file is not None:
        image = Image.open(file)
        image = np.array(image)
        detections = process_image(image)
        processed_image = annotate_image(image, detections)
        st.image(processed_image, caption="Processed Image")
        st.write("Done!")


if __name__ == '__main__':
    main()
