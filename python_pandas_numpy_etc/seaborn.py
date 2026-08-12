# seaborn
# visualize distribution with seaborn
# seaborn is a library that uses matplotlib underneath to plot graph. it will be used to visualize random distributions.

# displot stands for distribution plot, it takes as input an array and plot a curve corresponding to the distribution of points in the array

import matplotlib.pyplot as plt
import seaborn as sns

# plotting a Displot 
sns.displot([0,1,2,3,4,5], kind = "kde")
plt.show()

#