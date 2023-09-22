import seaborn as sns
import matplotlib.pyplot as plt
import nfl_data_py as nfl
import numpy as np

# get nfl pbp data from 2020-2022
seasons = range(2017, 2022 + 1)
pbp_py = nfl.import_pbp_data(seasons)

# subset data down to just the passing plays
pbp_py_p = pbp_py.query("play_type == 'pass' & air_yards.notnull()").reset_index()
pbp_py_p["passing_yards"] = np.where(pbp_py_p["passing_yards"].isnull(), 0, pbp_py_p["passing_yards"])

pbp_py_p_s = pbp_py_p.groupby(["passer_id", "passer", "season"]).agg({"passing_yards": ["mean", "count"]})
pbp_py_p_s.columns = list(map("_".join, pbp_py_p_s.columns.values))
pbp_py_p_s.rename(columns={'passing_yards_mean': 'ypa', 'passing_yards_count': 'n'}, inplace=True)
pbp_py_p_s.sort_values(by=["ypa"], ascending=False).head()

pbp_py_p_s_100 = pbp_py_p_s.query("n >= 100").sort_values(by=["ypa"], ascending=False)

print(pbp_py_p_s_100)