# comparison operator
print(1 > 2)
print(1 < 2)
print(1 >= 2)
print(1 <= 2)
print(1 != 2)
print(1 == 2)

# logical operators
# and or
print(3 > 2 and 2 == 2)  # 'and' need both True to be True

print(1 > 2 or 2 == 2)  # 'or' need one as True to be True

user_input = "mypwd"
stored_password = "mypwd"

print(user_input == stored_password)

passs = "mpwd1"
stored_pw = 'mpwd'
admin = True

if passs == stored_pw:
    print('True!')
    print('another line')
elif admin:
    print("i'm admin")
else:
    print('no pwd match and not an admin')


# for-in: iterate in a sequence
my_iterable_list = [1, 2, 3]
for i in my_iterable_list:
    print(i)

my_iterable_tuple = (3, 2, 1)
for i in my_iterable_tuple:
    print(i)

employees = {'ceo': 'ci', 'cfo': 'j'}
for pos in employees:
    print(f"the {pos} is held by {employees[pos]}")

mylist = employees.items()  # convert dictionary to tuple list
for (item1, item2) in mylist:  # tuple unpacking if list has tuple pairs
    print(item1)  # grab tuple items, and just return the 1st
    print(item2)  # grab tuple items, and just return the 2nd


# while: execute block while condition is true
n = 1

while n < 5:
    print(f'n is currently {n}')
    n = n+1
