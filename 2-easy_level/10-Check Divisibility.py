numbers_list = [1, 56, 7, 27, 23, 0, 202, -34, -13]
print("Numbers:", numbers_list)

##Check Divisibility:
divisor = int(input("Enter divisor:"))
divisible_numbers = ([nums for nums in numbers_list if nums % divisor == 0])
print("Divisible numbers by", divisor, "are" , divisible_numbers)