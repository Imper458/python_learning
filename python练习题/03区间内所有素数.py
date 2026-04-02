
def is_prime(number:int):
    if number == 1 | 2 :
        return True
    for idx in range(2,number):
        if number % idx == 0:
            return False
    return True


def print_primes(num1: int,num2: int):
    for number in range(num1,num2):
        if is_prime(number):
            print(number)


print_primes(3,50)