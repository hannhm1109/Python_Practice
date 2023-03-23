def Divisible_By_5(List):
    print("Given list : ", List)

    print("Divisible by 5 :")

    for x in list_num:      
        if x % 5 == 0:
            print(f"{x}")
        else :
            pass

list_num = [5,3,10,45,9,2,30,6,75]
Divisible_By_5(list_num)