numbers = [1, 2, 3, 4]

def all_even(num_list):

    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers

a = all_even(numbers)

print(a)

b = input('please input')

print(b)