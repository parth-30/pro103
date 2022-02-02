import pandas as pd
import plotly.express as px

df=pd.read_csv("data.csv")
fig=px.scatter(df,x ="date", y="cases",  title="Cases around the world", color="country")
fig.show()      