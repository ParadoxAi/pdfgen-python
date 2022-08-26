import collections.abc

import six


def is_iterable(arg):
    return (
        isinstance(arg, collections.abc.Iterable)
        and not isinstance(arg, six.string_types) # not string
        and not hasattr(arg, 'read') # not file
    )
