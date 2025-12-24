from answer import Answer

def main():
    n = int(input())
    answer = Answer()
    result = answer.decomp(n)
    print(result)
    
if __name__ == '__main__':
    main()