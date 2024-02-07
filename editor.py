import random

with open('edit_me.txt', 'w') as f:
    n = random.randint(100, 999)
    f.write('hello world ' + str(n) + '\n')
    print("should write: hello world " + str(n))