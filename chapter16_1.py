import csv
from matplotlib import pyplot as plt

filename = "sitka_weather_07-2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)

plt.figure(dpi=128, figsize=(20, 20))
plt.plot(highs)    

plt.show()
