"""
>>> fizzbuzz(1, 2, 3, 5, 9, 10, 11, 15)
1
2
fizz
buzz
fizz
buzz
11
fizzbuzz
>>> fizzbuzz(*range(1, 4))
1
2
fizz
"""
def fizzbuzz(*values):
    if not values:
        return None
    value = values[0]
    if not (value % 3 or value % 5):
        print 'fizzbuzz'
    elif not value % 3:
        print 'fizz'
    elif not value % 5:
        print 'buzz'
    else:
        print value
    return fizzbuzz(*values[1:])
