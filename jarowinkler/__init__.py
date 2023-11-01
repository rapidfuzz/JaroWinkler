__author__: str = "Max Bachmann"
__license__: str = "MIT"

import rapidfuzz.distance.Jaro as _Jaro
import rapidfuzz.distance.JaroWinkler as _JaroWinkler

import importlib.metadata as _importlib_metadata

try:
    __version__: str = _importlib_metadata.version(__package__ or __name__)
except _importlib_metadata.PackageNotFoundError:
    __version__: str = "0.0.0"

__all__ = [
    "jaro_similarity",
    "jarowinkler_similarity",
]

def jaro_similarity(s1, s2, *, processor=None, score_cutoff=None) -> float:
    """
    Calculates the jaro similarity

    Parameters
    ----------
    s1 : Sequence[Hashable]
        First string to compare.
    s2 : Sequence[Hashable]
        Second string to compare.
    processor: callable, optional
        Optional callable that is used to preprocess the strings before
        comparing them. Default is None, which deactivates this behaviour.
    score_cutoff : float, optional
        Optional argument for a score threshold as a float between 0 and 1.0.
        For ratio < score_cutoff 0 is returned instead. Default is 0,
        which deactivates this behaviour.

    Returns
    -------
    similarity : float
        similarity between s1 and s2 as a float between 0 and 1.0

    """
    return _Jaro.similarity(s1, s2, processor=processor, score_cutoff=score_cutoff)


def jarowinkler_similarity(s1, s2, *, prefix_weight=0.1, processor=None, score_cutoff=None) -> float:
    """
    Calculates the jaro winkler similarity

    Parameters
    ----------
    s1 : Sequence[Hashable]
        First string to compare.
    s2 : Sequence[Hashable]
        Second string to compare.
    prefix_weight : float, optional
        Weight used for the common prefix of the two strings.
        Has to be between 0 and 0.25. Default is 0.1.
    processor: callable, optional
        Optional callable that is used to preprocess the strings before
        comparing them. Default is None, which deactivates this behaviour.
    score_cutoff : float, optional
        Optional argument for a score threshold as a float between 0 and 1.0.
        For ratio < score_cutoff 0 is returned instead. Default is 0,
        which deactivates this behaviour.

    Returns
    -------
    similarity : float
        similarity between s1 and s2 as a float between 0 and 1.0

    Raises
    ------
    ValueError
        If prefix_weight is invalid
    """
    return _JaroWinkler.similarity(
        s1,
        s2,
        prefix_weight=prefix_weight,
        processor=processor,
        score_cutoff=score_cutoff,
    )

# assign attributes to function. This allows rapidfuzz to call them more efficiently
# we can't directly copy the functions + replace the docstrings, since this leads to
# crashes on PyPy
jaro_similarity._RF_OriginalScorer = jaro_similarity
jarowinkler_similarity._RF_OriginalScorer = jarowinkler_similarity

jaro_similarity._RF_ScorerPy = _Jaro.similarity._RF_ScorerPy
jarowinkler_similarity._RF_ScorerPy = _JaroWinkler.similarity._RF_ScorerPy

if hasattr(_Jaro.similarity, "_RF_Scorer"):
    jaro_similarity._RF_Scorer = _Jaro.similarity._RF_Scorer
if hasattr(_JaroWinkler.similarity, "_RF_Scorer"):
    jarowinkler_similarity._RF_Scorer = _JaroWinkler.similarity._RF_Scorer