# Breast Cancer Detection using Convolutional Neural Networks and Transfer Learning with DenseNet-201

## Introduction
Breast cancer is a significant health concern worldwide, and early detection methods are crucial for improving outcomes. This project focuses on the development of a breast cancer detection system using Convolutional Neural Networks (CNN) and transfer learning with DenseNet-201. The study utilizes a dataset of breast ultrasound images and applies machine learning techniques for breast cancer classification, detection, and segmentation.

## Authors
- Marwa El Kamil
- Supervised by: Prof. Meryem El Mouhtadi

## Affiliation
Euromed University of Fez-EIDIA

## Abstract
This scientific article presents a study on the development of a breast cancer detection system using Convolutional Neural Networks (CNN) and transfer learning with DenseNet-201. The research focuses on utilizing a dataset of breast ultrasound images and explores the efficacy of machine learning techniques in breast cancer classification, detection, and segmentation. The article discusses the dataset characteristics, including image size and categorization into normal, benign, and malignant classes. The proposed approach utilizes the DenseNet-201 architecture as a pre-trained CNN model and applies fine-tuning techniques to adapt it specifically for breast cancer detection.

## Methodology

### Dataset
The dataset used in this study consists of breast ultrasound images collected from 600 female patients between the ages of 25 and 75 years. The dataset comprises a total of 780 images, with an average image size of 500 × 500 pixels. The images are categorized into three classes: normal, benign, and malignant, with the following distribution:

Benign: 487 images
Malignant: 210 images
Normal: 133 images
### DenseNet-201
DenseNet-201 is a pre-trained CNN architecture employed in this study. It consists of multiple dense blocks, each containing several layers. The dense connectivity within each block enables efficient information and gradient flow throughout the network, leading to improved feature reuse and enhanced model performance. The pre-trained DenseNet-201 model provides valuable knowledge about image features, which can be fine-tuned for the specific task of breast cancer detection.

### Fine-tuning and Transfer Learning
Fine-tuning involves adjusting the weights of the pre-trained DenseNet-201 model using the breast ultrasound dataset. By fine-tuning the model, it can accurately classify and detect abnormalities related to breast cancer. The transfer learning approach allows leveraging the learned representations in the pre-trained model and adapting them to the dataset's specific characteristics, leading to improved accuracy and generalization ability.

### Method
The proposed model architecture utilizes DenseNet-201 for training on the dataset. To enhance accuracy, the test set is augmented through data augmentation techniques, such as random resizing, rotating, cropping, and flipping of the original images. Data augmentation increases sample diversity and helps train a deep network.

### Experimental Design
Dataset Collection
The breast ultrasound images used in this study were collected at Baheya hospital and stored in DICOM format. The dataset includes grayscale images of normal, benign, and malignant cases. Initially, 1100 images were collected, but after preprocessing, the dataset was refined to 780 images, with duplicates removed.

### Preprocessing
Preprocessing steps were performed to make the dataset useful for training. The dataset was refined by removing duplicates, resulting in a final dataset size of 780 images. Additionally, images were cropped to remove unused and unimportant boundaries.

### Ground Truth
Ground truth annotations (mask images) were created for each ultrasound image to facilitate the breast cancer detection process. Freehand segmentation was performed using Matlab, and mask images were generated. The dataset was organized into three folders corresponding to the three classes of breast cancer (normal, benign, and malignant).

### Conclusion
This project demonstrates the potential of using Convolutional Neural Networks (CNN) and transfer learning with DenseNet-201 for breast cancer detection. The study contributes to the field of medical image analysis and provides insights into the development of computer-aided diagnosis systems for breast cancer. Further research and development in this area can leverage the findings presented in this article.

## References
[1] P. D. Velusamy and P. Karandharaj. Medical image processing schemes for cancer detection: A survey. In International Conference on Green Computing Communication and Electrical Engineering (ICGC-CEE), pages 1-6, March 2014.

[2] "Deep learning approaches for data augmentation and classification of breast masses using ultrasound images" Walid Al-Dhabyani, Mohammed Gomaa, Hussien Khaled, Fahmy Aly Int. J. Adv. Comput. Sci. Appl., 10(5), 2019.

