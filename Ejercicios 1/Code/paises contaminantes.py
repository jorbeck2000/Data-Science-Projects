import pandas as pd

population = pd.read_csv("/Users/jorgebecker/Desktop/A01027251-Database/Ejercicios 1/TextFiles/greenhouse_gas_inventory_data_data.csv")

clean=population[["country_or_area","year","value"]]


select_year=clean.loc[clean["year"]==2010]


top5sum=select_year.groupby(by=['country_or_area','year']).sum()

top5dup=top5sum.sort_values(by = "value", ascending = False)


print(top5sum.tail(5))



