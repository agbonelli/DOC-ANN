#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from doc_model.utils.config import load_config
from doc_model.evaluation.evaluate import run_evaluation


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/config.yaml")
    args = parser.parse_args()

    config = load_config(args.config)

    train_metrics, val_metrics = run_evaluation(config)

    print("Train:", train_metrics)
    print("Validation:", val_metrics)
