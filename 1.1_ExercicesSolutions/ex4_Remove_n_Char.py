def remove_char(str, n):
    if n < len(str) :
        return str[n::]
    else :
        print("error")

print(remove_char("kawoppps", 3))