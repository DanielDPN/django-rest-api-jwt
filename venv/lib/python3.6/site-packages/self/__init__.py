#!/usr/bin/env python
import inspect
from decorator import decorator
from public import public


@decorator
@public
def self(method, self, *args, **kwargs):
    """method decorator to return self object

    Example:

    @self
    def method(self):
        # statement
    """
    if not inspect.isroutine(method):
        err = "@self decorator for methods only, got %s" % method
        raise TypeError(err)
    margs = [self] + list(args)
    r = method(*margs, **kwargs)
    if r:
        raise ValueError("@self %s result is not None" % method)
    return self
