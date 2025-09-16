# def greet():
#     print('Hello World')
#     print('Hello Nima')
#     print('Hello Faisal')
#     print('Hello Shayan')
#     print('Hello Yaser')
#     print('Hello Neman')
    
# greet()
# print(' ')
# greet()


# def greet(name, lastname, ):
#     print(f"Hello {name} {lastname}")


# greet('Nima','Ghafoori')
# greet('Shayan', 'Watandar')
# greet('Faisal', 'Mahmoudi')
# greet('Yaser', 'Atayee')
# greet('Neman', 'Atayee')



# def addition(num1, num2):
#     return num1 + num2

# print(addition(10,20)) 

# def greet(name = 'Pashmak', lastName = 'Pashmakiyan'):
#     print(f"Hello {name} {lastName}")
    
# greet()
# greet('Yaqoob', 'Yaqoobi')

# def studentInfo(name, age):
#     print(f"{name} is {age} years old")

# studentInfo('nman', 17)
# studentInfo(name="neman", age=17)

def greet(*names):
    # print(f"Hello {name}")
    for name in names:
        print(f"Hello {name}")
    
greet('shayan', 'faisal', 'yaser', 'nima', 'yaqoob', 'samim')