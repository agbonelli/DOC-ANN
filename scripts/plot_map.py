#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 20:43:47 2026

@author: gabibonelli
"""

import argparse
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from doc_model.visualization.plot import plot_doc_map


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot DOC map")
    parser.add_argument("--input", default="outputs/doc_map.nc")
    parser.add_argument("--output", default=None)

    args = parser.parse_args()

    plot_doc_map(args.input, save_path=args.output)