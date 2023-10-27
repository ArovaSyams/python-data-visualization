import seaborn as sns
import matplotlib.pyplot as plt

penguin = sns.load_dataset("penguins")

sns.scatterplot(data=penguin, x="body_mass_g", y="flipper_length_mm", hue="species", style="species")
plt.show()