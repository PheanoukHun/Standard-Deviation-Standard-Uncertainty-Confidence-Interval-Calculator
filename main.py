# Library Importations

import math

## Iniatilization of the Variables

data_list = [];
standard_deviation = 0;
standard_uncertainty = 0;
sum_of_differences = 0;
n = 0;
mean = 0;
low = 0;
high = 0;
std_squared = 0;

# Taking the Data
with open("dataList.txt") as file:
    data_list = file.read().split(",");
    n = len(data_list);

# Converts all Data Points into a Float
for i in range(len(data_list)):
    data_list[i] = float(data_list[i]);

## Finding the Mean for Later Use

# Sum of All data
for data in data_list:
    mean += data;

# Find Mean
mean = mean / n;

## Finding the Standard Deviation

# Summation of the differences between data point and mean
for data in data_list:
    sum_of_differences += ((data - mean) ** 2);

# Finding Standard Deviation
std_squared = (1/(n-1)) * sum_of_differences;
standard_deviation = math.sqrt(std_squared);

## Finding Standard Uncertainty
standard_uncertainty = standard_deviation / math.sqrt(n);

## Minimum and Maximum Confidence Interval
low = mean - (2 * standard_uncertainty);
high = mean + (2 * standard_uncertainty);

## Print Out Results
print("\nData Points: ", end = "");
print(*data_list, sep = ", ");
print(f"Mean: {round(mean, 10)}");
print(f"Standard Deviation: {round(standard_deviation, 10)}");
print(f"Standard Uncertainty: {round(standard_uncertainty, 10)}");
print(f"Confidence Interval:\n   -Lower Internal: {low}\n   -Higher Interval: {high}");
print();