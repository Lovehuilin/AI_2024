"""
Project: ResolutionFOL Testing.
Author : Jason Rao
Time   : 24-03-23
"""

from perprocessing import text
from myResolutionFOL import ResolutionFOL

def test_function(knowledge_base: set) -> None:
    print("\n")
    resolver = ResolutionFOL()
    resolution_results = resolver(knowledge_base)
    print("\n".join(resolution_results))
    return

KB = text.preprocessing()
test_function(KB)