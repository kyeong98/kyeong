import math

class Calculator:   
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y
        
    def squared(self, x, y):
        return x ** y
        
    def modulo(self, x, y):
        return x % y
        
    def square_root(self, x):  #제곱근
        return math.sqrt(x)

    def variance(self, nums):  #분산
        n = len(nums)
        mean = sum(nums) / n
        return sum((x-mean) ** 2 for x in nums) / n
    
    def std_deviation(self, nums):   #표준편차
        return math.sqrt(self.variance(nums))


cal = Calculator()
print("계산 가능한 연산 목록")
print("더하기(+)   빼기(−)   곱하기(×)   나누기(÷)   제곱(**)  나머지(%)  제곱근(√)")



while True:
    choice = input("수식 선택>>")
    if choice == '더하기' or choice == '+':
        while True: 
            try:
                num1 = float(input("첫번째 숫자>>"))
                num2 = float(input("두번째 숫자>>"))
                break
            except ValueError:
                print("숫자를 입력하세요")
                continue
        print(num1, "+", num2, "=", cal.add(num1, num2))

    elif choice == '빼기' or choice == '-':
        while True:
            try:
                num1 = float(input("첫번째 숫자>>"))
                num2 = float(input("두번째 숫자>>"))
                break
            except ValueError:
                print("숫자를 입력하세요")
                continue
        print(num1, "-", num2, "=", cal.subtract(num1,num2))

    elif choice == '곱하기' or choice == '*':
        while True: 
            try:
                num1 = float(input("첫번째 숫자>>"))
                num2 = float(input("두번째 숫자>>"))
                break
            except ValueError:
                print("숫자를 입력하세요")
                continue
        print(num1, "*", num2, "=", cal.multiply(num1,num2))

    elif choice == '나누기' or choice == '/':
        while True: 
            try:
                num1 = float(input("첫번째 숫자>>"))
                num2 = float(input("두번째 숫자>>"))
                break
            except ValueError:
                print("숫자를 입력하세요")
                continue
        print(num1, "/", num2, "=", cal.divide(num1,num2))

    elif choice == '제곱' or choice == '**':
        while True: 
            try:
                num1 = float(input("첫번째 숫자>>"))
                num2 = float(input("제곱할 수>>"))
                break
            except ValueError:
                print("숫자를 입력하세요")
                continue
        print(num1, "**", num2, "=", cal.squared(num1,num2))
   
    elif choice == '나머지' or choice == '%':
        while True: 
            try:
                num1 = float(input("첫번째 숫자>>"))
                num2 = float(input("나눌 수>>"))
                break
            except ValueError:
                print("숫자를 입력하세요")
                continue
        print(num1, "%", num2, "=", cal.modulo(num1,num2))

    elif choice == '제곱근' or choice == '√':
        while True: 
            try:
                num = float(input("숫자>>"))
                break
            except ValueError:
                print("숫자를 입력하세요")
        print("√", num, "=", cal.square_root(num))
        
    elif choice == '분산':
        nums = []
        while True:
            try:
                input_data = input("데이터를 입력하세요(구분자: 공백 또는 쉼표)>> ")
                nums = [float(x) for x in input_data.replace(",", " ").split()]
                if len(nums) < 2:
                    print("데이터를 두 개 이상 입력하세요")
                    continue
                else:
                    break
            except ValueError:
                print("숫자를 입력하세요")
                continue
        print("분산:", cal.variance(nums))
    
    elif choice == '표준편차':
        nums = []
        while True:
            try:
                input_data = input("데이터를 입력하세요(구분자: 공백 또는 쉼표)>> ")
                nums = [float(x) for x in input_data.replace(",", " ").split()]
                if len(nums) < 2:
                    print("데이터를 두 개 이상 입력하세요")
                    continue
                else:
                    break
            except ValueError:
                print("숫자를 입력하세요")
                continue
        print("표준편차:", cal.std_deviation(nums))


    elif choice == '종료':
        print("사용종료")
        break
    else:
        print("잘못된 입력입니다.")
        continue