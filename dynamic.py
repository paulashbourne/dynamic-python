from collections import defaultdict

class InfiniteDict(defaultdict):
   def __init__(self):
      defaultdict.__init__(self, self.__class__)

# Only supports positional arguments
def dynamic(func):
    lookup = InfiniteDict()

    def execute(*args):
        # Try to look up value
        # Assumes function takes at least one argument
        result = lookup
        has_result = True
        for arg in args:
            if arg in result:
                result = result[arg]
            else:
                has_result = False
        if has_result:
            return result
        else:
            result = func(*args)
        store = lookup
        for i in xrange(len(args) - 1):
            store = store[args[i]]
        store[args[-1]] = result
        return result

    return execute

@dynamic
def fibonacci(n):
    assert n > 0, "Input integer must be positive"
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    print fibonacci(100)
