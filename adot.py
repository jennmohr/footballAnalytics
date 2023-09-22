# package imports
import pandas as pd
import nfl_data_py as nfl

# 2022 nfl pbp data import
pbp_py = nfl.import_pbp_data([2022])
filter_crit = 'play_type == "pass" & air_yards.notnull()'

# filter pbp data by passing plays that had recorded depth
# then aggregate data by counting number of plays and calculating mean air yards per pass
pbp_py_p = (
    pbp_py.query(filter_crit).groupby(["passer_id", "passer"]).agg({"air_yards": ["count", "mean"]})
)

# reformat column heads and only include players with more than 100 air yards
pbp_py_p.columns = list(map("_".join, pbp_py_p.columns.values))
sort_crit = "air_yards_count > 100"

# sort data by mean of the air yards and print the output
print(
    pbp_py_p.query(sort_crit).sort_values(by="air_yards_mean", ascending=[False]).to_string()
)