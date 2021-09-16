# PneumoniaNetResnet50
## Description
Main objective of this program is to classify Pneumonia with deep learning methods. Through this model i hope it can help health workers to automate process classifying Pneumonia throug chest ray image

My main method to make this is using a deep learning approach. I use Convolution Neural Nets to create the classifier and apply transfer learning with pre-trained models. I used ResNet50 as the backbone 
fine-tune it with my own dataset (which I got from this [Kaggle](https://www.kaggle.com/tolgadincer/labeled-chest-xray-images) link). For the architecture, I used Pytorch as the base framework.

## Installation Guide
### Docker
Build the Image
````DOCKER_BUILDKIT=1 docker build -t clayrisee/pneumonianet:resnet50 . ```

Run Container
````sh runDocker.sh```



### Github

* Clone this repository in your local with this command ```git clone https://github.com/Clayrisee/PneumoniaNetResnet50.git```
* Install the requirement modules ```pip install -r requirements.txt```
* If the module already satisfied, you can run the inference.py
### Main.py
To use ```main.py```, the model is in ```.onnx``` format.
My ```.onnx``` saved model is in [this](hhttps://github.com/Clayrisee/PneumoniaNetResnet50/blob/main/pneumonianet_resnet50.onnx) folder.

1. See details arguments
```python main.py -i```

2. Perform inference
```python inference.py -i <your_image_path>```

## Result
| Input Image      | Output |
| ----------- | ----------- |
| ![Image1](https://github.com/Clayrisee/PneumoniaNet/blob/main/test_image/test_1.jpeg)     | Pneumonia Confidence:99.98% |
| ![Image2](https://github.com/Clayrisee/PneumoniaNet/blob/main/test_image/test_2.jpeg)     | Pneumonia Confidence: 99.83%|
| ![Image3](https://github.com/Clayrisee/PneumoniaNet/blob/main/test_image/test_3.jpeg)     | Pneumonia Confidence: 97.71% |

## Othe Version using ResNet50
I Also build another version of this project using Vgg-19 backbone, you can visit this [Repository](https://www.github.com/Clayrisee/PneumoniaNet)

