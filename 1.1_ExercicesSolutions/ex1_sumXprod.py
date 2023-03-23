def multiplication_or_sum( a,  b):
    product = a * b
    if product <= 1000 :
        return product
    else :
        return a + b
print(multiplication_or_sum(60,60))