from functions import read_table, percentagem_acerto
import seaborn as sns


url = "https://gist.githubusercontent.com/guilhermesilveira/1b7d5475863c15f484ac495bd70975cf/raw/16aff7a0aee67e7c100a2a48b676a2d2d142f646/projects.csv"

data_url = read_table(url)

print(data_url.head())

finished = {
    0: 1,
    1: 0
}

data_url["finished"] = data_url["unfinished"].map(finished)

print(data_url. head())

# Diferentes formas de fazer o mesmo gráfico
plot = sns.scatterplot(x="expected_hours",
                       y="price",
                       hue="finished",
                       data=data_url,
                       )

print(plot)

plot1 = sns.relplot(x="expected_hours",
                    y="price",
                    col="finished",
                    data=data_url,
                    )

print(plot1)

plot2 = sns.relplot(x="expected_hours",
                    y="price",
                    hue="finished",
                    col="finished",
                    data=data_url,
                    )

print(plot2)

x = data_url[["expected_hours", "price"]]
y = data_url["finished"]

percentagem_acerto(x, y)
