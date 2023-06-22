def palindrom():
    word = str(input())
    a = word[::-1]
    if word == a:
        print(True)
    else:
        print(False)

palindrom()