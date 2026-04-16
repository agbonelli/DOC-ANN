#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 21:33:58 2026

@author: gabibonelli
"""

import numpy as np
from scipy import stats

def compute_metrics(y, yp):
    slope, intercept, r, p, _ = stats.linregress(y, yp)
    rmsd = np.sqrt(np.mean((y-yp)**2))
    mapd = np.mean(np.abs((y-yp)/y))*100
    mb = np.mean(yp-y)

    return {
        "N": len(y),
        "RMSD": rmsd,
        "MAPD": mapd,
        "MB": mb,
        "R": r
    }