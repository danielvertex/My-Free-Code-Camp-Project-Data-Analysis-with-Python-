import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df["overweight"] = ((df["weight"] / ((df["height"] / 100) ** 2)) > 25).astype(int)

# 3
df["cholesterol"] = df["cholesterol"].apply(lambda x: 0 if x == 1 else 1)
df["gluc"] = df["gluc"].apply(lambda x: 0 if x == 1 else 1)

# 4
def draw_cat_plot():
    # Group and reformat the data to split it by "cardio". Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    df_cat = pd.melt(df, var_name = "variable", value_vars = ["active","alco","cholesterol", "gluc","overweight","smoke"], id_vars = "cardio")

    # Draw the catplot with "sns.catplot()"
    fig = sns.catplot(data=df_cat, kind="count",  x="variable",hue="value", col="cardio").set_axis_labels("variable", "total")
    fig = fig.fig

    # Do not modify the next two lines
    fig.savefig("catplot.png")
    return fig


# 10
def draw_heat_map():
    # Clean the data
    # 11
    df_heat = df[(
        (df["ap_lo"] <= df["ap_hi"]) &
        (df["height"] >= df["height"].quantile(0.025)) &
        (df["height"] <= df["height"].quantile(0.975)) &
        (df["weight"] >= df["weight"].quantile(0.025)) &
        (df["weight"] <= df["weight"].quantile(0.975))
        )]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(corr)

    # 14
    fig, ax = plt.subplots(figsize=(7, 5))

    # 15
    sns.heatmap(corr,mask=mask, fmt=".1f",vmax=.3, linewidths=.5,square=True, cbar_kws = {"shrink":0.5},annot=True, center=0)

    # 16
    fig.savefig("heatmap.png")
    return fig


