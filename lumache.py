"""
Lumache (name squatting for official Sphinx tutorial)
"""

__version__ = "1.0.0"

class InvalidKindError(Exception):
    """
    Raised if the kind is invalid."""
    pass

def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]

    """
    return ["shells", "gorgonzola", "parsley"]

def add(a, b):
    """
    Add two numbers `a` and `b`.

    You could add a more detailed description of the function here
    if it were more complicated than simply adding two arguments.

    Parameters:
        a (float): First number
        b (float): Second number

    Returns:
        float: Sum of `a` and `b`

    Examples:
        >>> add(1, 2)
        3
    """
    return a + b
