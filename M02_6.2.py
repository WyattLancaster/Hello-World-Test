guess_me = 7
number = 1

while number < guess_me or number > guess_me or number == guess_me:
    if number < guess_me:
        print('too low')
    if number == guess_me:
        print('found it!')
        break
    elif number > guess_me:
        print('oops')
        break
    number += 1

