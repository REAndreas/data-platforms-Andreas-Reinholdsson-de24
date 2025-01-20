import pandas as pd
import seaborn as sns
from pathlib import Path

data_path = Path(__file__).parent


df = pd.read_csv(data_path / "athlete_events.csv")

print(df.head())

plot = sns.barplot(data=df, x="Sex", y="Age").get_figure()
plot.savefig(data_path/"figure.png")