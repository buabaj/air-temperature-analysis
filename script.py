
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['axes.labelsize'] = 20
plt.rcParams['axes.titlesize'] = 25


data = input("Enter the location: ")
data += ".csv"
df = pd.read_csv(data)

df["date"] = pd.to_datetime(df[["year", "month", "day"]])
df['day_name'] = df['date'].dt.day_name()
df["week"] = df["date"].dt.isocalendar().week

# plot time series of daily temperature
plt.rcParams["figure.figsize"] = (35, 15)
plt.xlabel('Years')  # label x-axis
plt.xticks(fontsize=15)  # set x-axis ticks font size
plt.yticks(fontsize=15)  # set y-axis ticks font size
plt.ylabel('temperature')  # label y-axis
plt.title('Timeseries of daily temperature')  # title
plt.plot(df['temperature'], color='orange')  # plot data
plt.savefig('results/timeseries_temperature.jpg')  # save figure
plt.close()


# plot yearly average temperature

yearly_mean = df.groupby('year')['temperature'].mean()
plt.rcParams["figure.figsize"] = (35, 20)
plt.xlabel('year')  # label x-axis
plt.ylabel('mean temperature')  # label y-axis
plt.title('Yearly average temperature')  # title
plt.xticks(yearly_mean.index, rotation=50, fontsize=15)  # rotate x-axis labels
plt.plot(yearly_mean.index, yearly_mean, color='red', linewidth=5)  # plot data
plt.savefig('results/yearly_mean_plot.jpg')  # save figure
plt.close()


# write yearly mean to csv
f = open('results/yearly_mean.csv', 'w')
f.write('year,mean\n')
f.write('\n'.join(['{},{}'.format(k, v) for k, v in yearly_mean[1:].items()]))
f.close()

print("Yearly mean temperature saved to csv file, plots generated and saved to results folder")
