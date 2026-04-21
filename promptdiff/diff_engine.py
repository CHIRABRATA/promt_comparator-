import difflib

def get_diff(text1, text2):
    """
    Returns word-by-word difference between two texts
    """
    words1 = text1.split()
    words2 = text2.split()

    diff = difflib.ndiff(words1, words2)
    return "\n".join(diff)