# from raven import Client
# client = Client('https://6e8a4d42f33f4bbeb1c90396108c0d42:9f970186d9cf4acea135561061054466@sentry.io/210052')

import inspect
import ast
from functools import wraps

@wraps
def decorate(f):
    exec(inspect.getsource(f))
    print("??")
    print(f.__name__)
    return eval(f.__name__)

@decorate
def test():
    print("?")
    return 1

# @wraps
# def decorate(f):
#     print("??")
#     tree = ast.parse(inspect.getsource(f))
#     print(tree)
#     exec(compile(tree, filename="<ast>", mode="eval"))
#     return eval(f.__name__)

# @decorate
# def test():
#     print("?")
#     return 1

test()


# def checkpoint(some_function):

#     def wrapper(*args, **kwargs):
#         some_function(*args, **kwargs)
#         client.captureException(Exception('I know Python!'))

#     return wrapper
