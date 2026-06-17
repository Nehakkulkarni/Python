import statistics

numbers =[12, 7, 22, 5, 17, 9, 22, 15, 7, 14]
mean_value = statistics.mean(numbers)
median_value = statistics.median(numbers)
mode_value = statistics.mode(numbers)

print("Numbers:", numbers)
print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)