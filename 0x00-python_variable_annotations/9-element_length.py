#!/usr/bin/env python3
'''duck typing annotation'''
from typing import Iterable, Sequence, List, Tuple
def element_length(lst: Iterable[Sequence])->List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]