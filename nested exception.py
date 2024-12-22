print('main start')
try:
    print('outer started')
    print(a)
    try:
        print('inner started')
        print(10/2)
        print('inner ended')
    except Exception as e:
        print(e)
    print('outer is ended')
except Exception as e:
    print(e)
print('main end')    
        
