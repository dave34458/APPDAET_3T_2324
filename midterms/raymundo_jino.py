def is_perfect(number: int, sigma: int) -> bool:
    return number == sigma

def get_sum(divisors: list[int]) -> int:
    return sum(divisors)

def get_divisors(midterm_number: int) -> list[int]:
    divisors = [] 
    for i in range(1, midterm_number):
        if midterm_number % i == 0:
            divisors.append(i)
    return divisors

def main():
    midterm_number = input("Please enter a number: ")
    if not midterm_number.isnumeric():
        print("this is not a number")
    else:                  
        midterm_number = int(midterm_number)
        divisors = get_divisors(midterm_number)        
        print(f"divisors: {divisors}")

        sigma = get_sum(divisors)
        print(f"sigma is: {sigma}")
                
        print(f"is_perfect is {is_perfect(midterm_number, sigma)}")

if __name__ == "__main__":
    main()