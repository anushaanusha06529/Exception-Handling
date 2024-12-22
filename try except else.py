print('main start')
a=int(input('enter a vaalue'))
b=int(input('enter b value'))
try:
    print('try started')
    res=a/b
    print('try ended')
except ZeroDivisionError:
    print('we can not divided with zero')
else:
    print('else is executing')
    print(res)
print('main ends')    
