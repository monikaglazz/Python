from functools import wraps


def show_args(fn):
    """Accepts a function and returns another function.

    Args:
        fn (function): any function passed to it

    Returns:
        function: function with return from another function
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """Before invoking the function passed to it. Prints: a tuple of the
        positional arguments, and a dictionary of the keyword arguments.

        Returns:
            function: passed function
        """
        print("Here are the args:", args)
        print("Here are the kwargs:", kwargs)
        return fn(*args, **kwargs)
    return wrapper
