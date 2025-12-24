def square_digits(num):
    result = ""
    num =str(num)
    for i in range(0, len(num)):
        a = int(num[i]) ** 2
        result += str(a)
    return int(result)

def main():
    num = int(input())
    print(square_digits(num))
    
if __name__ == '__main__':
    main()