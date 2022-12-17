from typing import Tuple


def find_best_alignment(transcription: str, text: str) -> Tuple[int, int]:
    """
    Find the best alignment for the given text within the given transcription.

    Args:
        transcription (str): The large text in which to find the best alignment for the given text.
        text (str): The small text to align within the large text.

    Returns:
        A tuple (start_index, end_index) representing the best alignment of the small text within
            the large text.
    """
    best_alignment = (0, 0)
    max_matching_characters = 0
    for i in range(len(transcription) - len(text) + 1):
        num_matching_characters = sum(transcription[i + j] == text[j] for j in range(len(text)))
        if num_matching_characters > max_matching_characters:
            max_matching_characters = num_matching_characters
            best_alignment = (i, i + len(text))
    return best_alignment
