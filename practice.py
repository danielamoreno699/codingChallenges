# write prgram to determine whether a number N is equal to the sum of proper divirsor 
#excluding the number itself

#obtain a dict with the number and its divisors
# sum the values of the dictornary and determine whether its equal to the N number

# def sum_dict_values(input_dict):
#     new_dict = {}
#     for key, value in input_dict.items():
#         new_dict[key] = sum(value)
#     return new_dict


# def solve(numbers):
#     divisors = {}
#     for number in numbers:
#         divisors_list=[]
#         for i in range(1, number + 1):
#                 if number % i == 0:
#                      divisors_list.append(i)
#         divisors[number] = divisors_list
#         new_dict = sum_dict_values(divisors)
#     return new_dict

# def if_divisors_equal_to_number(new_dict):
#     results = []
#     for key, value in new_dict.items():
#         if key == value:
#             results.append("YES")
#         else:
#             results.append("NO")
#     return results
    

     

# number = 6,5,28
# result = solve(number)
# print("Divisors of", number, "are:", result)
# equality_result = if_divisors_equal_to_number(result)
# print(equality_result)

def get_proper_divisors(number):
    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    return divisors

def is_sum_of_proper_divisors(number):
    divisors = get_proper_divisors(number)
    sum_of_divisors = sum(divisors)
    return sum_of_divisors == number

def main():
    numbers = [6, 28, 12]  # Example numbers to check
    results = {}

    for number in numbers:
        if is_sum_of_proper_divisors(number):
            results[number] = "YES"
        else:
            results[number] = "NO"

    for number, result in results.items():
        print(f"{number}: {result}")

if __name__ == "__main":
    main()
