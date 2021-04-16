#Linghang Kong
#acoustic id intro assignment

import pandas as pd
import numpy as np
import random

def stratified_random_sample(file):
    #Load data and preprocessing
    try:
        df = pd.read_csv('audio_data.csv')
        df = df.copy()
        df = df.drop(columns=['Error'])
        df = df.dropna()
        df = df.loc[df['Duration']>=60]
    
    #convert time to hours of the day
        hours = []
        for i in df['StartDateTime']:
            hours.append(int(i[11:13]))
        df['Hours'] = hours
    
    #group by id
        grouped = df.groupby(['AudioMothID','Hours']).count().reset_index()
        for i in grouped['AudioMothID'].value_counts().index:
            if len(grouped[grouped['AudioMothID']==i])<24:
                df = df.drop(df[df['AudioMothID']==i].index)
        df_original = df['AudioMothID'].value_counts().index.to_list()
        result = []
        for i in df_original:
            for j in range(0,24):
                df_selected = df[(df['Hours']==j) & (df['AudioMothID']==i)].sample(1)
                result.append(df_selected)
        result1 = pd.concat(result)
        result1.to_csv("result_sample.csv")
        return True
    except FileNotFoundError as e:
        return False
    else:
        return False

#stratified_random_sample('audio_data.csv')