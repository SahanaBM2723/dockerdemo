
def calculate_average(numbers):
    if not numbers or not isinstance(numbers, list):
        return 0
    return sum(numbers) / len(numbers)

