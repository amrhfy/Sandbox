import statistics
import numpy
import machine_learning as ml

from collections import Counter
from scipy import stats


student_age = [22, 25, 29, 35, 19, 20, 24, 27, 28, 29, 29, 18, 19, 23, 22]
sum_age = 0

for s in student_age:
   sum_age = sum_age + s

# MEAN - Average
mean = sum_age/(len(student_age))
print("Mean (Average) - ", round(mean, 2))

# MEDIAN - Middle Value
median = numpy.median(student_age)
print("Median (Middle Value) - ", median)

# MODE - Value that appears the most
mode = ml.find_most_frequent(student_age)
print("Mode (Value That Appears The Most) - ", mode)

# STANDARD DEVIATION - Spread data between mean
std = numpy.std(student_age)
print("Standard Deviation - ", round(std, 2))

# VARIANCE
num_variance = numpy.var(student_age)
print("NumPY Variance - ", round(num_variance, 2))

# MANUAL VARIANCE
man_variance = ml.find_variance(student_age, mean)
print("Manual Variance - ", round(man_variance, 2))

# PERCENTILE
percentile = str(numpy.percentile(student_age, 22)) + "%"
print("Percentile (Ages 22) - ", percentile)

