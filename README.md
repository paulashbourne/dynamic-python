# dynamic-python
A python decorator which uses dynamic programming to optimize functions.
A fibonacci sequence function is included for demonstration purposes.
This decorator requires the function is only called with positional arguments.

Just add the decorator @dynamic to any function. All calls to that function will
all be cached based on the argument values provided. Repeat calls are then avoided
by using the previously computed and stored value.
