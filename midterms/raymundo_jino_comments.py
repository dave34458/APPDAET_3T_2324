def is_perfect(number: int, sigma: int) -> bool:
    # TODO: condition to check if the two parameters are equal
    return number == sigma

def get_sum(divisors: list[int]) -> int:
    # TODO: return the sum of all divisors
    # option 1: loop through each item in the list
    # sigma = 0
    # for i in divisors:
    #     print(f"divisor is {i}")
    #     sigma += i
    # return sigma

    # option 2: use the sum() function/method
    return sum(divisors)

def get_divisors(midterm_number: int) -> list[int]:
    # TODO: return a list containing all divisors for this number
    divisors = [] 
    for i in range(1, midterm_number):
        # print(f"inside the loop: {i}")
        # print(f"{midterm_number} % {i} is {midterm_number % i}")
        if midterm_number % i == 0:
            divisors.append(i)
    return divisors

def main():
    # 01: prompt user for a number and assign it to a variable named midterm_number
    midterm_number = input("Please enter a number: ")
    # 02: condition to check if midterm_number (string) can be parsed to a number
    if not midterm_number.isnumeric():
        print("this is not a number")
    else:        
        # 03: cast midterm_number to an integer        
        midterm_number = int(midterm_number)
    
        # 04: call method get_divisors(midterm_number) and assign the returned value to a variable named divisors
        divisors = get_divisors(midterm_number)

        # 05: print the value of variable divisors
        print(f"divisors: {divisors}")

        # 06: call method get_sum(divisors) and assign the returned value to a variable named sigma
        sigma = get_sum(divisors)

        # 07: print the value of variable sigma
        print(f"sigma is: {sigma}")

        # 08: print the returned value of is_perfect(midterm_number, sigma) method call
        print(f"is_perfect is {is_perfect(midterm_number, sigma)}")

if __name__ == "__main__":
    main()