import cv2
from matplotlib import image 
import numpy as np
import matplotlib.pyplot as plt
import vortex.runtime as vrt
import sys
import argparse
from PIL import Image
import torchvision as vision



# def predict(img_path, model_path='pneumonianet_resnet50.onnx', runtime_device='cpu'):
#     img = cv2.imread(img_path)
#     img = img[:,:, ::-1]
#     img = cv2.resize(img, (256, 256)).astype('float32')/255.
#     img = np.transpose(img, [2, 0, 1])
#     img = np.expand_dims(img, 0)

#     model = vrt.create_runtime_model(model_path=model_path, runtime=runtime_device)

#     results = model(img)
#     return results

mean = [0.485, 0.456, 0.406]
std = [0.229, 0.224, 0.225]
def predict(img, model_path='pneumonianet_resnet50.onnx', runtime_device='cpu'):
    transform_image = vision.transforms.Compose([
        vision.transforms.Resize((256, 256)),
        vision.transforms.ToTensor(),
        vision.transforms.Normalize(mean=mean, std=std)
    ])
    img = transform_image(img)
    img = np.array(img)
    img = np.expand_dims(img, 0)
    model = vrt.create_runtime_model(model_path=model_path, runtime=runtime_device)
    results = model(img)
    return results


def visualize_output(img, confidence, class_name):
    plt.imshow(img), plt.xticks([]), plt.yticks([])
    plt.xlabel("Predicted class is: {}\nConfidence (%): {}%".format(class_name, confidence))
    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--image",  help="Path images")
    args = parser.parse_args()
    class_names={
        0: "Normal",
        1: "Pneumonia"
    }

    img_path = args.image
    image = Image.open(img_path).convert('RGB')


    results = predict(image)
    print(results)
    confidence = results[0]['class_confidence'][0][0] * 100
    class_name = class_names[results[0]['class_label'][0][0].astype('int')]
    print(confidence)
    print(class_name)

    visualize_output(image, confidence, class_name)
