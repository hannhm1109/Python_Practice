def prime(num):

    if num < 2:
        print("Not a prime number")
    for i in range(2, num):
        if (num % i == 0) :
            print("Not a prime number")
        
    print("Prime number")

prime(5)