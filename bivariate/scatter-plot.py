import matplotlib.pyplot as plt
import seaborn as sns

lemon_diameter = [6.44, 6.87, 7.7, 8.85, 8.15, 
                  9.96, 7.21, 10.04, 10.2, 11.06]
lemon_weight = [112.05, 114.58, 116.71, 117.4, 128.93, 
                132.93, 138.92, 145.98, 148.44, 152.81]

# with matplot
# plt.scatter(x=lemon_diameter, y=lemon_weight)

# with seaborn
# sns.scatterplot(x=lemon_diameter, y=lemon_weight)
#  scatter plot dan regression function (metode statistik untuk memperkirakan korelasi antar independent dan dependent variable) 
sns.regplot(x=lemon_diameter, y=lemon_weight)

plt.show()