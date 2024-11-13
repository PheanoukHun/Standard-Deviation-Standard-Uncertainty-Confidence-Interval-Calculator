# Library Importations
import sys
import json

# Importing the Statistic Class

sys.path.append("/workspaces/Standard-Deviation-Standard-Uncertainty-Confidence-Interval-Calculator")
from StatisticsClass.statisticscalc import StatisticsCalc

# Variables

lenghtOfRamp = 1

# Importing the Data

with open("kineticEnergy/dataPoint.json") as file:
    data = json.load(file)

# Finding the Kinetic Energy of all points

pointKE = {}
for point in data.keys():
    avg_velocity = lenghtOfRamp/data[point][1]
    final_velocity = avg_velocity * 2
    kE = 0.5 * (data[point][0]) * (final_velocity ** 2)
    pointKE[point] = kE

# Finding the Average Kinetic Energy

statistic = StatisticsCalc(pointKE.values())

print(statistic.mean)
print(statistic.standard_deviation)