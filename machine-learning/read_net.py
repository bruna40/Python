import pandas as pd

url = "https://gist.githubusercontent.com/guilhermesilveira/2d2efa37d66b6c84a722ea627a897ced/raw/10968b997d885cbded1c92938c7a9912ba41c615/tracking.csv"

data_url = pd.read_csv(url)

x = data_url[["home", "how_it_works", "contact"]]
y = data_url["bought"]

print(x, y)
