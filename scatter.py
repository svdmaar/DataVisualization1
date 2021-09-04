import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = []
for x in x_values:
    y_values.append(x * x)

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor="none", s=40)

plt.title("Square Numbers", fontsize=24)

plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis="both", which="major", labelsize=14)

plt.savefig("plot.png", bbox_inches="tight")

plt.show()
