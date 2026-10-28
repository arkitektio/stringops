"""stringops: simple string operations, offered as Arkitekt actions.

The app is a declaration: who it is, and what it offers. `arkitekt run dev`
finds it in this module (as `app`) and runs it; so does `python app.py`.
"""

from typing import Generator, List, Literal

from arkitekt import App, bsx, run

#: Raised by semantic-release on every release (see pyproject.toml).
__version__ = "0.2.1"

app = App("stringops", __version__, author="jhnnsrs")


#: A letter case to convert a string into. A Literal becomes a choice port.
Case = Literal["upper", "lower", "title", "swap"]

app.blok(
    "stringops",
    bsx("""
    <Html>
      <Text text="Simple string operations" />
    </Html>
    """),
    description="What the app offers.",
)


@app.action
def concatenate(left: str, right: str, separator: str = " ") -> str:
    """Concatenate

    Joins {{left}} and {{right}} with {{separator}} in between

    Parameters
    ----------
    left : str
        The first string
    right : str
        The second string
    separator : str, optional
        What goes between them, by default a single space

    Returns
    -------
    str
        The joined string
    """
    return f"{left}{separator}{right}"


@app.action
def change_case(text: str, case: Case = "upper") -> str:
    """Change Case

    Converts {{text}} to {{case}} case

    Parameters
    ----------
    text : str
        The string to convert
    case : Case, optional
        The target case, by default upper

    Returns
    -------
    str
        The converted string
    """
    if case == "upper":
        return text.upper()
    if case == "lower":
        return text.lower()
    if case == "title":
        return text.title()
    return text.swapcase()


@app.action
def reverse(text: str) -> str:
    """Reverse

    Reverses the characters of {{text}}

    Parameters
    ----------
    text : str
        The string to reverse

    Returns
    -------
    str
        The reversed string
    """
    return text[::-1]


@app.action
def repeat(text: str, times: int = 2, separator: str = "") -> str:
    """Repeat

    Repeats {{text}} {{times}} times, separated by {{separator}}

    Parameters
    ----------
    text : str
        The string to repeat
    times : int, optional
        How often to repeat it, by default 2
    separator : str, optional
        What goes between the repetitions, by default nothing

    Returns
    -------
    str
        The repeated string
    """
    if times < 0:
        raise ValueError("times needs to be zero or more")
    return separator.join([text] * times)


@app.action
def replace(text: str, old: str, new: str = "") -> str:
    """Replace

    Replaces every {{old}} in {{text}} with {{new}}

    Parameters
    ----------
    text : str
        The string to edit
    old : str
        The substring to look for
    new : str, optional
        What to put in its place, by default nothing (removes it)

    Returns
    -------
    str
        The edited string
    """
    return text.replace(old, new)


@app.action
def strip(text: str, characters: str = " \t\n") -> str:
    """Strip

    Removes leading and trailing {{characters}} from {{text}}

    Parameters
    ----------
    text : str
        The string to trim
    characters : str, optional
        The characters to remove from both ends, by default whitespace

    Returns
    -------
    str
        The trimmed string
    """
    return text.strip(characters)


@app.action
def count(text: str, substring: str) -> int:
    """Count

    Counts how often {{substring}} occurs in {{text}}

    Parameters
    ----------
    text : str
        The string to search
    substring : str
        What to count

    Returns
    -------
    int
        The number of non-overlapping occurrences
    """
    return text.count(substring)


@app.action
def length(text: str) -> int:
    """Length

    Counts the characters of {{text}}

    Parameters
    ----------
    text : str
        The string to measure

    Returns
    -------
    int
        The number of characters
    """
    return len(text)


@app.action
def split(text: str, separator: str = " ") -> List[str]:
    """Split

    Splits {{text}} on {{separator}}

    Parameters
    ----------
    text : str
        The string to split
    separator : str, optional
        Where to split, by default a single space

    Returns
    -------
    List[str]
        The parts, in order
    """
    return text.split(separator)


@app.action
def join(parts: List[str], separator: str = " ") -> str:
    """Join

    Joins {{parts}} with {{separator}}

    Parameters
    ----------
    parts : List[str]
        The strings to join
    separator : str, optional
        What goes between them, by default a single space

    Returns
    -------
    str
        The joined string
    """
    return separator.join(parts)


@app.action
def is_palindrome(text: str, ignore_case: bool = True) -> bool:
    """Is Palindrome

    Checks whether {{text}} reads the same backwards

    Parameters
    ----------
    text : str
        The string to check
    ignore_case : bool, optional
        Compare without regard to case, by default True

    Returns
    -------
    bool
        True if the string is a palindrome
    """
    normalized = text.lower() if ignore_case else text
    return normalized == normalized[::-1]


@app.action
def words(text: str) -> Generator[str, None, None]:
    """Words

    Yields the words of {{text}} one by one

    Parameters
    ----------
    text : str
        The string to walk through

    Returns
    -------
    str
        Each word, in order
    """
    for word in text.split():
        yield word


if __name__ == "__main__":
    run(app)
