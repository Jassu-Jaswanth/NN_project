#1
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import scipy as scpy

from zmq import NULL

#2
pokemondb = pd.read_csv("./data/Pokemon.csv")

#3
print(pokemondb.shape)

#4
cols = np.array(pokemondb.columns)

#5
del pokemondb["#"]

#6
print("Unique pokemon types in 'Type 1' are " + str(pokemondb["Type 1"].unique()))

#7
print("Number of pokemons with 'Mega' in their name = " + str(int(pokemondb[pokemondb["Name"].str.contains("Mega")].size / (cols.size-1))))

#8
print("Standrad Deviaton of column Sp. Def = " + str(pokemondb["Sp. Def"].std()))

#9
legPokemons = int(pokemondb[pokemondb["Legendary"]].size / (cols.size-1))
percentageOfLegPokemons = legPokemons/pokemondb.shape[0] * 100
print("Percentage of legendary pokemons in the dataset = " + str(round(percentageOfLegPokemons,3)))




#10
pokemondb = pokemondb.fillna("noTyp2")
# for col in cols:
#     if col == "#" or col == "Name" : 
#         continue
#     freq = dict(pokemondb[col].value_counts().sort_values())
#     x = list(freq.keys())
#     mode = x[-1]
#     if(mode == "noTyp2"):
#         mode = x[-2]
#     print("Mode of " + col + " is " + str(mode))
#     xmin = min(x)
#     xmax = max(x)
#     if isinstance(xmin,str) or isinstance(xmin,bool):
#         plt.hist(pokemondb[col],range(len(x)+1))
#     else:
#         plt.hist(pokemondb[col],range(xmin,xmax+2))
#     plt.xlabel("Distribution Range")
#     plt.ylabel(col)
#     plt.show()

#11

# Needed analysis of:
#   mean,
#   variance,
#   skew,
#   min,
#   max,
#   median,
#   25th percentile,
#   75th percentile,
#   inter-quartile range

    # With Dataframe provided as part of arguments to function
def pokemonInfo(db,feature):
    featureList = np.array(db[feature])
    print("Mean of given feature " + str(featureList.mean()))
    print("Variance of given feature " + str(featureList.var()))
    print("Skew of given feature " + str(scpy.stats.skew(featureList)))
    print("Min of given feature " + str(min(featureList)))
    print("Max of given feature " + str(max(featureList)))
    print("Median of given feature " + str(np.median(featureList)))
    print("25th percentile of given feature " + str(np.percentile(list(db[feature]),25)))
    print("75th percentile of given feature " + str(np.percentile(list(db[feature]),75)))
    print("Interquartile range of given feature " + str(scpy.stats.iqr(db[feature], interpolation = 'midpoint')))

    # Without Dataframe provided as part of arguments to function
    # Must use pokemondb as your database/dataframe name
def pokemonInfo(feature):
    featureList = np.array(pokemondb[feature])
    print("Mean of given feature " + str(featureList.mean()))
    print("Variance of given feature " + str(featureList.var()))
    print("Skew of given feature " + str(scpy.stats.skew(featureList)))
    print("Min of given feature " + str(min(featureList)))
    print("Max of given feature " + str(max(featureList)))
    print("Median of given feature " + str(np.median(featureList)))
    print("25th percentile of given feature " + str(np.percentile(list(pokemondb[feature]),25)))
    print("75th percentile of given feature " + str(np.percentile(list(pokemondb[feature]),75)))
    print("Interquartile range of given feature " + str(scpy.stats.iqr(pokemondb[feature], interpolation = 'midpoint')))

def pokemonWhiskerPlot(feature):
    featureList = pokemondb[feature]
    plt.boxplot(featureList)
    plt.show()

#12
data = [pokemondb["Sp. Def"],pokemondb["Sp. Atk"]]
plt.boxplot(data,labels=["Sp. Def", "Sp. Atk"])
plt.show()

sb.heatmap(pokemondb.corr())
plt.show()