#문자열() 함수

# a = input("랜덤자료")30
# print('입력값은 {}입니다. {}' .format(a,a))




print('---계산기---')
print('---------')

number1 = int(input('숫자를 입력해 주세요 : '))
number2 = int(input('숫자를 입력해 주세요 : '))

print ('뭐할까요? \n1. 더하기 \n2. 빼기 \n3. 곱하기\n4. 나누기')
code = int(input("숫자를 골라주세요"))

if code ==1:
    print ("정답은 {}입니다." .format(number1 + number2))
elif code ==2:
    print("정답은 {}입니다.".format(number1 - number2))
elif code ==3:
    print("정답은 {}입니다.".format(number1 * number2))
elif code ==4:
    print("정답은 {}입니다.".format(number1 / number2))
else:
    print("잘못 입력했어요")
