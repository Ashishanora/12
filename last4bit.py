if __name__ == '__main__':
    b=int(input("Enter the integer"))
    c=bin(b)
    c=c.replace("0b","")

    print(c)
    print(c[0:4])