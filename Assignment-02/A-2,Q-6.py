#WAP to find mean, median, mode, variance, standard deviation using UDF.
def calculate_mean(data):
    return sum(data) / len(data)


def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2

    if n % 2 == 0:
        median = (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        median = sorted_data[mid]

    return median


def calculate_mode(data):
    freq = {}

    for i in data:
        freq[i] = freq.get(i, 0) + 1

    mode = max(freq, key=freq.get)
    return mode


def calculate_variance(data):
    mean = calculate_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / (len(data) - 1)
    return variance


def calculate_standard_deviation(data):
    variance = calculate_variance(data)
    std = variance ** 0.5
    return std


data = [int(x) for x in input("Enter a series of numbers: ").split()]

mean = calculate_mean(data)
median = calculate_median(data)
mode = calculate_mode(data)
variance = calculate_variance(data)
std = calculate_standard_deviation(data)

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std}")