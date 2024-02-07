import random

with open('edit_me.txt', 'w') as f:
    f.write('hello world ' + str(random.randint(100, 999)) + '\n')