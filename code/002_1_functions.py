def fibonacci(n):
    a, b = 1, 2
    while a < n: 
        print (a, end= ' ')
        a, b = b, a+b
        print()

# fibonacci(500000000)
# print( fibonacci )

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('Do you really want to quit?')