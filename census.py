# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 13:55:13 2019

@author: shanm
"""

# Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
train_df = pd.read_csv("C:/Users/shanm/OneDrive/Documents/macine-learning/census/census-block-group-american-community-survey-data/safegraph_open_census_data/data/cbg_b01.csv",sep = ",")
print(train_df.head())
print(train_df.info())
print(train_df.shape[0])
train_df.columns
train_df.isnull().sum()