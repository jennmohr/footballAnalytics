# package imports
import pandas as pd
import numpy as np
import nfl_data_py as nfl

# get nfl pbp data from 2016-2021
seasons = range(2016, 2021 + 1)
pbp_py = nfl.import_pbp_data(seasons)

# subset data down to just the passing plays
pbp_py_p = pbp_py.query("play_type == 'pass' & air_yards.notnull()").reset_index()

# data cleaning/wrangling. defining long & short passes
pbp_py_p["pass_length_air_yards"] = np.where(
    pbp_py_p["air_yards"] >= 20, "long", "short"
)

# setting incomplete passes as 0 instead of null
pbp_py_p["passing_yards"] = np.where(pbp_py_p["passing_yards"].isnull(), 0, pbp_py_p["passing_yards"])

# describing basic passing yards data numbers
print("Basic passing data:")
print(pbp_py_p["passing_yards"].describe())

# describing short passes data
print("Short passing data:")
print(pbp_py_p.query('pass_length_air_yards == "short"')["passing_yards"].describe())

# describing long passes data
print("Long passing data:")
print(pbp_py_p.query('pass_length_air_yards == "long"')["passing_yards"].describe())

# describing short passes epa
print("Short passing epa:")
print(pbp_py_p.query('pass_length_air_yards == "short"')["epa"].describe())

# describing long passes epa
print("Long passing epa:")
print(pbp_py_p.query('pass_length_air_yards == "long"')["epa"].describe())