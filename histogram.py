# package imports
import seaborn as sns
import matplotlib.pyplot as plt
import nfl_data_py as nfl
import numpy as np

# get nfl pbp data from 2016-2021
seasons = range(2016, 2021 + 1)
pbp_py = nfl.import_pbp_data(seasons)

sns.displot(data=pbp_py, x="passing_yards")
plt.show()

sns.set_theme(style="whitegrid", palette="colorblind")

# subset data down to just the passing plays
pbp_py_p = pbp_py.query("play_type == 'pass' & air_yards.notnull()").reset_index()

# data cleaning/wrangling. defining long & short passes
pbp_py_p["pass_length_air_yards"] = np.where(
    pbp_py_p["air_yards"] >= 20, "long", "short"
)

# setting incomplete passes as 0 instead of null
pbp_py_p["passing_yards"] = np.where(pbp_py_p["passing_yards"].isnull(), 0, pbp_py_p["passing_yards"])

pbp_py_p_short = pbp_py_p.query('pass_length_air_yards == "short"')

# display chart of yards gained or lost
pbp_py_hist_short = sns.displot(data=pbp_py_p_short, binwidth=1, x="passing_yards")
pbp_py_hist_short.set_axis_labels("Yards gained (or lost) during a passing play", "Count")
plt.show()