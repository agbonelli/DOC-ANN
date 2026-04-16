#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 20:14:29 2026

@author: gabibonelli
"""

import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

def build_scaler(df, idx, predictors, output_path):
    df_sub = df.loc[idx, predictors].dropna()
    scaler = StandardScaler().fit(df_sub.values)
    joblib.dump(scaler, output_path)

# usarlo para ANNa y ANNb