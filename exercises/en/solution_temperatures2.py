import altair as alt
import pandas as pd


temps_df = pd.read_csv('data/temperature.csv', parse_dates=['date'])
temps_df = temps_df.assign(month=temps_df['date'].dt.month_name())
temps_df.info()