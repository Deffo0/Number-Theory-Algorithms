import os
import random


def sieve_of_eratosthenes():
    """
    A function that gets the primes of a given number
    :return: void
    """
    clear()
    n = int(input("Enter the wanted number: "))
    prime = [True for _ in range(n + 1)]
    i = 2
    while i * i <= n:

        # If prime[i] is not
        # changed, then it is a prime
        if prime[i]:

            # Update all multiples of i
            for j in range(i * i, n + 1, i):
                prime[j] = False
        i += 1

    # Print all prime numbers
    print("Primes are:")
    filtered_primes = []
    for i in range(2, n + 1):
        if prime[i]:
            filtered_primes.append(i)

    print("\t", filtered_primes)


def trial_division():
    """
    A function that gets the prime factors of a given number and specify if it is prime or composite
    :return: void
    """
    clear()
    n = int(input("Enter the wanted number: "))
    og_num = n
    primes = [1]
    while n % 2 == 0:
        primes.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            primes.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        primes.append(n)

    if og_num not in primes:
        primes.append(og_num)
    # Only odd number is possible
    print("Factors are:")
    print("\t", primes)
    if len(primes) == 1:
        print("This number is prime")
    else:
        print("This number is composite")


def extended_euclidean():
    """
    A function that calculate the greatest common divisor using Extended Euclidean Algorithm
    :return: void
    """
    clear()
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("GCD({}, {})".format(a, b))
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a
    result = ""
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    result += "Bézout Coefficients: \n\ts = {}\n \tt = {}\n".format(old_s, old_t)
    result += "Greatest Common Divisor = {}\n".format(old_r)
    result += "Quotients by The GCD: {}, {}\n".format(t, s)
    print(result)


def inv(a, b):
    # Apply extended Euclid Algorithm
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_s


def calculate_min_x(numbers, remainders):
    # Compute product of all numbers
    numbers_product = 1
    for i in range(0, len(numbers)):
        numbers_product = numbers_product * numbers[i]

    result = 0
    for i in range(0, len(numbers)):
        modified_number = numbers_product // numbers[i]
        result = result + remainders[i] * inv(modified_number, numbers[i]) * modified_number
    return result % numbers_product


def chinese_remainder():
    """
    A function that find minimum positive number x such that:
    x % num[0]    =  rem[0],
    x % num[1]    =  rem[1],
    .......................
    x % num[k-1]  =  rem[k-1]
    :return: void
    """
    clear()
    numbers = input("Enter the numbers array(ex: 1,2,3,4): ").replace("[", "").replace("]", "").strip().split(",")
    numbers = [int(i) for i in numbers]
    remainders = input("Enter the remainders array(ex: 1,2,3,4): ").replace("[", "").replace("]", "").strip().split(
        ",")
    remainders = [int(i) for i in remainders]
    print(f"X is {calculate_min_x(numbers, remainders)}")


def miller_test(d, n):
    # Pick a random number in [2..n-2]
    a = random.randint(2, n - 2)
    # Calc a^d % n
    x = pow(a, d, n)

    if x == 1 or x == n - 1:
        return True

    while d != n - 1:
        x = (x * x) % n
        d *= 2

        if x == 1:
            return False
        if x == n - 1:
            return True

    return False


def miller_test_driver():
    """
    A function that determine whether the number is prime or composite using miller test
    :return: void
    """
    clear()
    number = int(input("Enter the number which you want to test whether it is prime or composite: "))
    accuracy = int(input("Enter the level of accuracy that you want: "))
    # corner cases
    if number <= 1 or number == 4:
        return False
    if number <= 3:
        return True

    d = number - 1
    while d % 2 == 0:
        d //= 2

    for i in range(accuracy):
        if not miller_test(d, number):
            print("the number is composite")
            return

    print("the number is probably prime")


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_algorithm_type():
    """
    A function that ask the user which algorithm do you want to use
    :return: str
    """
    valid_inputs = ["1", "2", "3", "4", "5"]
    algorithm_type = input("Which algorithm you want to use from the following algorithms:\n"
                           "(1) sieve of Eratosthenes algorithm.\n"
                           "(2) Trial Division algorithm for integer factorization.\n"
                           "(3) Euclidean algorithm.\n"
                           "(4) Chinese remainder algorithm.\n"
                           "(5) Miller’s test algorithm.\n"
                           "Enter the number of the algorithm(ex: 3): ").strip()
    if algorithm_type not in valid_inputs:
        print("Invalid Input\n")
        return get_algorithm_type()
    return algorithm_type


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    go_out = "n"
    while go_out.lower() == "n":
        algorithm_type = get_algorithm_type()
        try:
            if algorithm_type == "1":
                sieve_of_eratosthenes()
            elif algorithm_type == "2":
                trial_division()
            elif algorithm_type == "3":
                extended_euclidean()
            elif algorithm_type == "4":
                chinese_remainder()
            elif algorithm_type == "5":
                miller_test_driver()
        except:
            print("Invalid Input")
        go_out = input("Do you want to exit?(y/n): ")
        if go_out.lower() == "y":
            break
        clear()