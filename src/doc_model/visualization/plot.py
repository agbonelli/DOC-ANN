#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 20:43:16 2026

@author: gabibonelli
"""

import matplotlib.pyplot as plt
import numpy as np
from netCDF4 import Dataset
import cartopy.crs as ccrs
import cartopy.feature as cfeature


def plot_doc_map(nc_path, vmin=0, vmax=75, save_path=None):

    ds = Dataset(nc_path)

    lat = ds.variables["lat"][:]
    lon = ds.variables["lon"][:]

    var_name = list(ds.variables.keys())[-1]
    doc = ds.variables[var_name][:]

    ds.close()

    lon2d, lat2d = np.meshgrid(lon, lat)

    fig = plt.figure(figsize=(10, 5))
    ax = plt.axes(projection=ccrs.PlateCarree())

    im = ax.pcolormesh(
        lon2d, lat2d, doc,
        vmin=vmin,
        vmax=vmax,
        transform=ccrs.PlateCarree()
    )

    # continentes
    ax.add_feature(cfeature.LAND, facecolor='lightgray')
    ax.add_feature(cfeature.COASTLINE, linewidth=0.5)

    # grilla
    gl = ax.gridlines(draw_labels=True, linewidth=0.5,
                      color='gray', alpha=0.5, linestyle='--')
    gl.top_labels = False
    gl.right_labels = False

    plt.colorbar(im, ax=ax, label="DOC (µmol L⁻¹)")
    ax.set_title("Surface DOC (0–50 m)")
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300)

    plt.show()