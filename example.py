# from checkpoint import checkpoint
from raven import Client
client = Client('https://6e8a4d42f33f4bbeb1c90396108c0d42:9f970186d9cf4acea135561061054466@sentry.io/210052')

# @checkpoint
def just_some_function(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        try:
            raise ValueError('checkpoint n')
        except ValueError:
            client.captureException()
        return 'Buzz'
    else:
        return str(n)


just_some_function(5)