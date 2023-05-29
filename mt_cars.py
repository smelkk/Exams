import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas as pd

# Update the file path and name
file_path = f'/Users/smelk/Desktop/mtcars.csv.xls'

# Read the CSV file
df = pd.read_csv(file_path)

# Display the contents of the DataFrame
print(df)

# Create a figure and gridspec
fig = plt.figure(figsize=(15, 10))
gs = gridspec.GridSpec(3, 3, figure=fig)

# Define subplots using gridspec
ax1 = fig.add_subplot(gs[:2, :2])    # Upper left subplot (spanning two rows and two columns)
ax3 = fig.add_subplot(gs[0, 2])       # Upper right subplot
ax6 = fig.add_subplot(gs[1, 2])       # Middle right subplot
ax7 = fig.add_subplot(gs[2, 0])       # Lower left subplot
ax8 = fig.add_subplot(gs[2, 1])       # Lower middle subplot
ax9 = fig.add_subplot(gs[2, 2])       # Lower right subplot

# Calculate mask for correlation heatmap
mask = np.tril(df.corr(numeric_only = True), k=-1)
#pd.set_option('mode.use_inf_as_null', True)

# Plot correlation heatmap
sns.heatmap(df.corr(numeric_only=True)[::-1], mask=mask[::-1], ax=ax1, cmap="coolwarm",
            linewidth=.5, center=0, cbar_kws={'shrink': 0.5}, vmax=1, vmin=-1)
cbar = ax1.collections[0].colorbar
cbar.set_label("Pearson correlation", rotation=90)
ax1.set_xlabel('Var1')
ax1.set_ylabel('Var2')
ax1.tick_params(axis='x', rotation=45)
ax1.tick_params(axis='y', rotation=0)

# Plot histogram with stacked bars
sns.histplot(data=df, x='wt', ax=ax3, hue='am', multiple='stack', bins=10)
sns.move_legend(ax3, "upper left", bbox_to_anchor=(1, 1), frameon=False, title='Transmission')
ax3.set_title('Weight and automatic/manual proportions on the plot', size=8)
ax3.set_xlabel('Ib')
ax3.set_ylabel('# of cars')
ax3.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)
ax3.set_xticks([2, 3, 4, 5])

# Boxplot
sns.boxplot(data=df, x="carb", y='mpg', ax=ax6)
ax6.set_xlabel('# of carburetors')
ax6.set_ylabel('mpg')

sns.scatterplot(data=df, x='hp', y='drat', hue='gear', size='cyl', ax=ax7, palette="bright")
ax7.set_xlabel('Gross horsepower')
ax7.set_ylabel('Rear axle ratio')
sns.move_legend(ax7, "upper left", bbox_to_anchor=(1, 1), frameon=False)

sns.histplot(data=df, x='am', ax=ax8, hue='carb', palette="ch:start=.2,rot=-.3",
             edgecolor=None, discrete=True, shrink=0.8)
sns.move_legend(ax8, "upper left", bbox_to_anchor=(1, 1), frameon=False)
ax8.set_xlabel('Transmission')
ax8.set_xticks([0, 1])

sns.kdeplot(data=df, x='mpg', hue='am', multiple='stack', ax=ax9)

fig.tight_layout()

fig
plt.show()