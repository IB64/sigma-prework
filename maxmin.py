
def max_min(list):
    min = max = list[0]
    for number in list:
        if number > max:
            max = number
        if number < min:
            min = number
    return [int(min),int(max)]

# sliced the input to omit the square brackets as input is a literal string of a list
number_list = input("Please provide a list of integers:")[1:-1].split(", ")
print(max_min(number_list))
