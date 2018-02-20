# from raven import Client
# client = Client('https://6e8a4d42f33f4bbeb1c90396108c0d42:9f970186d9cf4acea135561061054466@sentry.io/210052')

import inspect
import ast
from functools import wraps

import inspect, itertools

class ReturnLister(ast.NodeTransformer):
    def visit_Return(self, node):
        print(node)
        # self.generic_visit(node)
        import ipdb;
        ipdb.set_trace()
        return node


def decorate(f):
    source = inspect.getsource(f)
    source = itertools.dropwhile(lambda line: line.startswith('@'), source.splitlines())
    source = '\n'.join(source)
    tree = ast.parse(source)
    ReturnLister().visit(tree)
    # print(tree)
    exec(compile(tree, filename="<ast>", mode="exec"))
    
    return eval(f.__name__)

@decorate
def test():
    print("running ")
    return 1

test()
