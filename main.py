import math

data_list = None;
standard_deviation = 0;
standard_uncertainty = 0;
n = None;
mean = 0;

# Taking the Data

with open("dataList.txt") as file:
    data_list = file.read().split(",")
    n = len(data_list)

## Finding the Mean for Later Use

# Sum of All data
for data in data_list:
    mean += float(data);

# Find Mean
mean = mean / n

## Finding the Standard Deviation

# Summation of the differences between data point and mean
sum_of_differences = 0
for data in data_list:
    sum_of_differences += ((float(data) - mean) ** 2)

# Finding Stand Deviation
temp = (1/(n-1)) * sum_of_differences
standard_deviation = math.sqrt(temp)

## Finding Standard Uncertainty
standard_uncertainty = standard_deviation / math.sqrt(n)

## Minimum and Maximum Confidence Interval
min = standard_deviation - 2 * standard_uncertainty
max = standard_deviation + 2 * standard_uncertainty

## Print Out Results
print(f"\nMean: {round(mean, 10)}")
print(f"Standard Deviation: {round(standard_deviation, 10)}")
print(f"Standard Uncertainty: {round(standard_uncertainty, 10)}")
print(f"Confidence Interval:\nLower Internal: {min}\nHigher Interval: {max}")