from functools import wraps


def ensure_authorized(fn):
    """Accepts a function and returns another function.

    Args:
        fn (function): any passed function

    Returns:
        function: function with return from another function
    """

    @wraps(fn)
    def inner(*args, **kwargs):
        """Decorated function invoked only if there exists
        a keyword argument "role" with a value "admin".

        Returns:
            function: passed function
            or
            str: "Unauthorized"
        """

        if kwargs.get("role") == "admin":
            return fn(*args, **kwargs)
        else:
            return "Unauthorized"
    return inner
