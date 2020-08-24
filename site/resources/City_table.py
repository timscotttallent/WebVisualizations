import pandas as pd

df=pd.read_csv("clean_city_data.csv")

with open("table_from_py.html", "w") as f:
    f.write(df.to_html())