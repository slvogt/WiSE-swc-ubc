import sys

def main():
    num1 = sys.argv[1]
    operator = sys.argv[2]
    num2 = sys.argv[3]
    print eval(num1 + operator + num2)
    

main()
