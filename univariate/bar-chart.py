import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

cities = ('Bogor', 'Bandung', 'Jakarta', 'Semarang', 'Yogyakarta', 
          'Surakarta','Surabaya', 'Medan', 'Makassar')
 
populations = (45076704, 11626410, 212162757, 19109629, 50819826, 17579085,
               34832121, 287732520, 7854094)


# plt.bar(x=cities, height=populations)     # vertical bar chart

# plt.xticks(rotation=45)   # rotate each category dot in x axis

# plt.barh(y=cities, width=populations)     # Horizontal bar
# plt.show()

df = pd.DataFrame({
    "cities": cities,
    "population": populations
})

df.sort_values(by="population", inplace=True)

# plt.barh(y=df["cities"], width=df["population"])
# make a title
# plt.title("Population of cities in Indonesia")
# make xlabel
# plt.xlabel("Population (Millions)")
# make ylabel
# plt.ylabel("Cities")
# plt.show()



# Bar chart with seaborn
sns.barplot(y=df["cities"], x=df["population"], orient="h", color="blue")

# make a title
plt.title("Population of cities in Indonesia")
# make xlabel
plt.xlabel("Population (Millions)")

plt.show()