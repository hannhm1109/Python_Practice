def first_last_same(numberList):
    print("Given list : ",numberList)

    first_num = numberList[0]
    last_name = numberList[-1]

    if first_num == last_name:
        return True
    else :
        return False

number_x = [3,4,5,6,7,3]
print("result is", first_last_same(number_x))

number_y = [3,4,5,6,7,5]
print("result is", first_last_same(number_y))

