# Motivation
This dataset is created for prediction of Graduate Admissions from an Indian perspective.The dataset contains several parameters which are considered important during the application for Masters Programs. The parameters included are : 1. GRE Scores ( out of 340 ) 2. TOEFL Scores ( out of 120 ) 3. University Rating ( out of 5 ) 4. Statement of Purpose and Letter of Recommendation Strength ( out of 5 ) 5. Undergraduate GPA ( out of 10 ) 6. Research Experience ( either 0 or 1 ) 7. Chance of Admit ( ranging from 0 to 1 )
.This dataset is inspired by the UCLA Graduate Dataset. The test scores and GPA are in the older format. The dataset is owned by Mohan S Acharya. 

# Data Science-Blog
Here analysis is done pandas to understand variuos parameter that affect to student to get student admission
The Code is written in Python 3.6.5 . If you don't have Python installed you can find it here. If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip.

# Libraries
Pandas
python
matplotlib
numpy
pip
scikit-learn

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

# Data File - Admission Predict CSV file

In order for the network to print out the graduate student admission data  a .csv file is required. By using a .csv file the data can be sorted into folders with numbers and those numbers will correspond to specific names specified in the .json file. Data and the json file

# Admission Blog Post IPython Notebook
It has all the pandas code written to analyse the Admission Predict CSV File, visualize results(BAR Charts,Heat Map) and evaluate them.

# Blog Post

please find graduate admission blog post at following url

https://github.com/mudigosa/DataScience-Blog/wiki/Graduate-Admission-Statistics

# Data Analytics using linear Regression Model

Cloud Services -- There are many paid cloud services that let you train your models like AWS or Google Cloud
Coogle Colab -- Google Colab gives you free access to a tesla K80 GPU for 12 hours at a time. Once 12 hours have ellapsed you can just reload and continue! The only limitation is that you have to upload the data to Google Drive and if the dataset is massive you may run out of space.

However, once a model is trained then a normal CPU can be used for the predict.py file and you will have an answer within some seconds. Hyperparameters-The data used specifically for this assignemnt are a graduate student admission criteria database are not provided in the repository as it's larger than what github allows. Nevertheless, feel free to create your own databases and train the model on them to use with your own projects. 


Sample Training Command:

bash train.sh

Sample Prediction Command:

bash predict.sh

# Summary of Result
The students who has managed to score high GRE,great research skills along with very good SOP will get admission into good graduate schools

Please read CONTRIBUTING.md for the process for submitting pull requests. Authors

Shanmukha Mudigonda - Initial work Udacity -  Project of the Data Science with Python Nanodegree
