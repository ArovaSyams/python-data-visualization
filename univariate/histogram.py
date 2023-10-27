import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# make random number with tital 250 dots, mean = 15, and std.deviation = 5
x = np.random.normal(15,5, 250)

# make histogram with matplot
# plt.hist(x=x, bins=15)

# make hist with seaborn
sns.histplot(x=x, bins=15, kde=True)
plt.show()