lily = ['lily',18]
mary = ['mary',20]
database = [lily,mary]
print (database)


database1 = [
    ['albert','1111'],
    ['dilbert','2222'],
    ['jones','3333']
]
username = input('Username:')
pin = input('PIN code:')
if [username,pin] in database1:
    print('Access granted')