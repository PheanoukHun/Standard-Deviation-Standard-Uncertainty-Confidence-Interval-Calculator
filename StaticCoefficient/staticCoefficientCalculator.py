# Library Importations
import sys
import json

# Importing the Statistic Class

sys.path.append("/workspaces/Standard-Deviation-Standard-Uncertainty-Confidence-Interval-Calculator")
from StatisticsClass.statisticscalc import StatisticsCalc

## Iniatilization of the Variables

dataKeys = []
point_list = []
data_list = [];

# Taking the Data

with open("StaticCoefficient/dataPoint.json") as file:
    data_dict = json.load(file)

# Converts all Data Points into a Float

dataKeys = sorted(data_dict.keys())
for x in dataKeys:
    friction_coefficient = float(data_dict[x][1]) / float(data_dict[x][0])
    point = (x, friction_coefficient)
    data_list.append(friction_coefficient)
    point_list.append(point)

# Initiating the Class

results = StatisticsCalc(data_list)

## Print Out Results
print("\nData Points: ");
for point in point_list:
    print(f"  {point[0]} : {point[1]}")
print()
print(f"Mean: {round(results.mean, 10)}");
print()
print(f"Standard Deviation: {round(results.standard_deviation, 10)}");
print()
print(f"Standard Uncertainty: {round(results.standard_uncertainty, 10)}");
print()
print(f"Confidence Interval:\n   -Lower Internal: {results.low}\n   -Higher Interval: {results.high}");
print();