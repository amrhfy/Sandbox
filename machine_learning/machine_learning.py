from collections import Counter

def find_most_frequent(lst):
   counter = Counter(lst)
   max_count = max(counter.values())
   most_frequent_values = [item for item, count in counter.items() if count == max_count]

   if len(most_frequent_values) == 1:
      return most_frequent_values[0]
   else:
      return tuple(most_frequent_values)

def find_variance(lst, mean):
   sum_squared_diff = 0
   for a in lst:
      x = round((a - mean) * (a - mean), 2)
      sum_squared_diff = sum_squared_diff + x

   return sum_squared_diff/len(lst)