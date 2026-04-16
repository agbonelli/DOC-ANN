import argparse
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from sklearn.preprocessing import StandardScaler

from doc_model.utils.config import load_config
from doc_model.utils.logger import setup_logger
from doc_model.utils.io import save_netcdf

from doc_model.models.inference import DOCModel
from doc_model.pipeline.runner import run_inference

import joblib


def main(config_path):

    # Load config
    config = load_config(config_path)

    # Logger
    logger = setup_logger(config)
    logger.info("Starting DOC inference pipeline")

    # dinamic scalar
    scaler = joblib.load(config["model"]["scaler"])

    # Load model
    model = DOCModel(
        model_path=config["model"]["path"],
        scaler=scaler
    )

    predictors = list(config["data"]["inputs"].keys())
    files = list(config["data"]["inputs"].values())

    logger.info(f"Using predictors: {predictors}")
    logger.info(f"Number of input files: {len(files)}")

    # Run pipeline
    pred_map, lat, lon = run_inference(files, predictors, model)

    # Save output
    output_path = config["output"]["path"]
    logger.info(f"Saving output to {output_path}")

    save_netcdf(output_path, pred_map, lat, lon)

    logger.info("Pipeline finished successfully")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run DOC model inference")
    parser.add_argument("--config", default="configs/config.yaml")

    args = parser.parse_args()
    main(args.config)
