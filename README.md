# Data
This dataset is created for prediction of Graduate Admissions from an Indian perspective.The dataset contains several parameters which are considered important during the application for Masters Programs. The parameters included are : 1. GRE Scores ( out of 340 ) 2. TOEFL Scores ( out of 120 ) 3. University Rating ( out of 5 ) 4. Statement of Purpose and Letter of Recommendation Strength ( out of 5 ) 5. Undergraduate GPA ( out of 10 ) 6. Research Experience ( either 0 or 1 ) 7. Chance of Admit ( ranging from 0 to 1 )
.This dataset is inspired by the UCLA Graduate Dataset. The test scores and GPA are in the older format. The dataset is owned by Mohan S Acharya. 

# Data Science-Blog
Here analysis is done pandas to understand variuos parameter that affect to student to get student admission
The Code is written in Python 3.6.5 . If you don't have Python installed you can find it here. If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip.

# Installations

To install pip run in the command Line

python -m ensurepip -- default-pip

to upgrade it

python -m pip install -- upgrade pip setuptools wheel

to upgrade Python

pip install python -- upgrade

Additional Packages that are required are: Numpy, Pandas, MatplotLib, Pytorch, PIL and json which can be downloaded using pip command.

pip install numpy pandas matplotlib pil

or conda

conda install numpy pandas matplotlib pil

In order to intall Pytorch head over to the Pytorch site select your specs and follow the instructions given. Viewing the Jyputer Notebook

In order to better view and work on the jupyter Notebook I encourage you to use nbviewer . You can simply copy and paste the link to this website and you will be able to edit it without any problem. Alternatively you can clone the repository using

git clone https://github.com/mudigosa/DataScience-Blog/

then in the command Line type, after you have downloaded jupyter notebook type

Linear Regrssion
Scikit-learn is a powerful Python module for machine learning. Just import the library and start using model from it. 

import scikit-learn

jupyter notebook
locate the notebook and run it. Command Line Application

Train a new network on a data set with train.py
    Basic Usage : python train.py data_directory
    Prints out current epoch, training loss, validation loss, and validation accuracy as the netowrk trains
    Options:
        Set direcotry to save checkpoints: python train.py data_dor --save_dir save_directory
        Choose arcitecture (alexnet, densenet121 or vgg16 available): pytnon train.py data_dir --arch "vgg16"
        Set hyperparameters: python train.py data_dir --learning_rate 0.001 --hidden_layer1 120 --epochs 20
        Use GPU for training: python train.py data_dir --gpu gpu

Predict students who will get admissions from an csv with predict.py along with the probability of that name. That is you'll pass in a single image /path/to/image and return the flower name and class probability
    Basic usage: python predict.py /path/to/image checkpoint
    Options:
        Return top K most likely classes: python predict.py input checkpoint ---top_k 3
        Use a mapping of categories to real names: python predict.py input checkpoint --category_names cat_To_name.json
        Use GPU for inference: python predict.py input checkpoint --gpu

# Data File - CSV file

In order for the network to print out the graduate student admission data  a .csv file is required. By using a .csv file the data can be sorted into folders with numbers and those numbers will correspond to specific names specified in the .json file. Data and the json file

The data used specifically for this assignemnt are a graduate student admission criteria database are not provided in the repository as it's larger than what github allows. Nevertheless, feel free to create your own databases and train the model on them to use with your own projects. The structure of your data should be the following: The data need to comprised of 3 folders, test, train and validate. Generally the proportions should be 70% training 10% validate and 20% test. Inside the train, test and validate folders there should be folders bearing a specific number which corresponds to a specific category, clarified in the json file. For example if we have the image a.jpj and it is a rose it could be in a path like this /test/5/a.jpg and json file would be like this {...5:"rose",...}. Make sure to include a lot of photos of your catagories (more than 10) with different angles and different lighting conditions in order for the network to generalize better. GPU

# Data Analytics using linear Regression Model

Cuda -- If you have an NVIDIA GPU then you can install CUDA from here. With Cuda you will be able to train your model however the process will still be time consuming
Cloud Services -- There are many paid cloud services that let you train your models like AWS or Google Cloud
Coogle Colab -- Google Colab gives you free access to a tesla K80 GPU for 12 hours at a time. Once 12 hours have ellapsed you can just reload and continue! The only limitation is that you have to upload the data to Google Drive and if the dataset is massive you may run out of space.

However, once a model is trained then a normal CPU can be used for the predict.py file and you will have an answer within some seconds. Hyperparameters

Sample Training Command:

bash train.sh

Sample Prediction Command:

bash predict.sh

As you can see you have a wide selection of hyperparameters available and you can get even more by making small modifications to the code. Thus it may seem overly complicated to choose the right ones especially if the training needs at least 15 minutes to be completed. So here are some hints:

By increasing the number of epochs the accuracy of the network on the training set gets better and better however be careful because if you pick a large number of epochs the network won't generalize well, that is to say it will have high accuracy on the training image and low accuracy on the test images. Eg: training for 12 epochs training accuracy: 85% Test accuracy: 82%. Training for 30 epochs training accuracy 95% test accuracy 50%.
A big learning rate guarantees that the network will converge fast to a small error but it will constantly overshot
A small learning rate guarantees that the network will reach greater accuracies but the learning process will take longer
Densenet121 works best for images but the training process takes significantly longer than alexnet or vgg16

*My settings were lr=0.001, dropoup=0.5, epochs= 15 and my test accuracy was 86% with densenet121 as my feature extraction model. Pre-Trained Network

The checkpoint.pth file contains the information of a network trained to recognise 102 different species of flowers. I has been trained with specific hyperparameters thus if you don't set them right the network will fail. In order to have a prediction for an image located in the path /path/to/image using my pretrained model you can simply type python predict.py /path/to/image checkpoint.pth Contributing

Please read CONTRIBUTING.md for the process for submitting pull requests. Authors

Shanmukha Mudigonda - Initial work Udacity -  Project of the Data Science with Python Nanodegree
