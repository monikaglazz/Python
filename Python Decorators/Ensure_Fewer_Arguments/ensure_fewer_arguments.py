from functools import wraps


def ensure_fewer_than_three_args(fn):
    """Accepts a function and returns another function

    Args:
        fn (function): _description_

    Returns:
        function: function with return from another function
    """

    @wraps(fn)
    def wrapper(*args, **kwargs):
        """Wrapped function invoked only if there are fewer than
        three positional arguments passed to it.

        Returns:
            function: passed function
            or
            str: "Too many arguments!"
        """

        if len(args) < 3:
            return fn(*args, **kwargs)
        return "Too many arguments!"
    return wrapper
