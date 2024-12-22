print('main start')
try:
    print('try started')
    n1=int(input('enter a value'))
    n2=int(input('enter a value'))
    res=n1/n2
    print('try ended')
except Exception as e:
    print(e)
else:
    print('inside else block')
    print(res)
print('main ends')    
