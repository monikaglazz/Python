from functools import wraps


def double_return(fn):
    """Accepts a function and returns another function.

    Args:
        fn (function): any passed function

    Returns:
        function: function with return from another function
    """

    @wraps(fn)
    def wrapper(*args, **kwargs):
        """Decorated function returning two copies of passed function.

        Returns:
            list: list of two copies of the inner function's
        """
        v = fn(*args, **kwargs)
        return [v, v]
    return wrapper
