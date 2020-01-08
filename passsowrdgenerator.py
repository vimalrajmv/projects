import random
char_set=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
        'p','q','r','s','t','u','v','w','x','y','z','A','B','C','D',
        'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T',
        'U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9',
        '!','@','#','$','%','^','&','*','(',')','{','}','[',']','=','+','-',
        '_','/','.',';',':','?','<','>','\'','|','\\']
numbers=['0','1','2','3','4','5','6','7','8','9']
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
        'p','q','r','s','t','u','v','w','x','y','z','A','B','C','D',
        'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T',
        'U','V','W','X','Y','Z']
symbols=['!','@','#','$','%','^','&','*','(',')','{','}','[',']','=','+','-',
        '_','/','.',';',':','?','<','>','\'','|','\\']
password_len=int(input("Enter password length:"))
no_of_letters=int(input("Enter Number of Letters(Between 1 & 5):"))
no_of_numbers=int(input("Enter Number of Numbers(Between 1 & 5):"))
no_of_symbols=password_len - no_of_letters - no_of_numbers
password=""
while password_len != len(password):
 while no_of_letters != 0:
   password=password+random.choice(letters)
   no_of_letters-=1
 while no_of_numbers !=0:
   password=password+random.choice(numbers)
   no_of_numbers-=1
 while no_of_symbols !=0:
   password=password+random.choice(symbols)
   no_of_symbols-=1
print(password)

