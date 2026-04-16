#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import joblib

from doc_model.models.inference import DOCModel


def run_evaluation(config):

    # =========================
    # 1. Selección de modelo
    # =========================
    model_id = config["evaluation"]["model"]

    model_path = config["model"][f"{model_id}_path"]
    scaler_path = config["model"][f"{model_id}_scaler"]

    train_idx_path = config["data"][f"train_idx_{model_id.lower()}"]
    val_idx_path   = config["data"][f"val_idx_{model_id.lower()}"]

    predictors = config["model"][f"{model_id}_predictors"]
    target = config["data"]["target"]
    matchup_path = config["data"]["matchup"]

    # =========================
    # 2. Load data
    # =========================
    df = pd.read_csv(matchup_path)

    train_idx = pd.read_csv(train_idx_path).iloc[:, 0]
    val_idx   = pd.read_csv(val_idx_path).iloc[:, 0]

    df_train = df.loc[train_idx, predictors + [target]]
    df_val   = df.loc[val_idx, predictors + [target]]

    y_train = df_train[target].values
    y_val   = df_val[target].values

    # =========================
    # 3. Load model + scaler
    # =========================
    scaler = joblib.load(scaler_path)
    model = DOCModel(model_path, scaler)

    # =========================
    # 4. Predictions
    # =========================
    y_pred_train = model.predict(df_train, predictors)
    y_pred_val   = model.predict(df_val, predictors)

    # =========================
    # 5. Metrics
    # =========================
    def rmse(y_true, y_pred):
        return np.sqrt(np.mean((y_true - y_pred)**2))

    def bias(y_true, y_pred):
        return np.mean(y_pred - y_true)

    train_metrics = {
        "rmse": rmse(y_train, y_pred_train),
        "bias": bias(y_train, y_pred_train)
    }

    val_metrics = {
        "rmse": rmse(y_val, y_pred_val),
        "bias": bias(y_val, y_pred_val)
    }

    return train_metrics, val_metrics
