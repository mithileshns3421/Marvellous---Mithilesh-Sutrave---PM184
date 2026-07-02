def check_perfect_no(num):
    sum_of_divisors = 0

    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i

    return sum_of_divisors

def main():
    num = int(input("Enter a number: "))
    sod = check_perfect_no(num)
    if sod == num:
        print(num, "is a Perfect Number")
    else:
        print(num, "is Not a Perfect Number")


if __name__ == '__main__':
    main()
