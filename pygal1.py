import pygal
from random import randint

class Die():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)

die = Die()
die2 = Die()

results = []
for roll_num in range(50 * 1000):
    result = die.roll() + die2.roll()
    results.append(result)

max_result = die.num_sides + die2.num_sides

frequencies = []
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Result of rolling two D6 1000 times."
hist.x_labels = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6 + D6", frequencies)
hist.render_to_file("die_visual2.svg")
