def say_hello():
    print('hey')


say_hello()


def hey():
    return 'hello'


myvar = hey()

print(myvar)


def hmm(age, name):
    return f"hello {name} your age is {age}"


# using explicit argument
# not using positional argument
print(hmm(name='raccoon', age=35))


def checker(num):
    if num > 100:
        return f'{num} greater than 100'
    else:
        return f'{num} not greater than 100'


print(checker(90))


mylist = [1, 3, 2, 5, 5, 64, 10, 42, 51, 22, 2]


def checkerlist(list_to_check):
    for n in list_to_check:
        if n == 10:
            return True  # when return encountered, exit function

    return False  # if nothing found after for-in loop, return default


print(checkerlist(mylist))
