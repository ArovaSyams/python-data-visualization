import seaborn as sns
import matplotlib.pyplot as plt

penguin = sns.load_dataset("penguins")

sns.barplot(data=penguin, x="species", y="body_mass_g", hue="sex", errorbar=None)
plt.show()