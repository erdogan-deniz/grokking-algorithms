from decimal import Decimal
from datetime import date, datetime
from typing import (
    Union,
    TypeVar,
    Sequence,
)


_type: TypeVar = TypeVar("user_type", bound=[
    int,
    str,
    date,
    float,
    Decimal,
    datetime,
], )


def binary_search(arr: Sequence, val: _type) -> _type | None:
    """
    ...
    """

    left_b: int = 0
    right_b: int = len(arr, ) - 1

    while left_b <= right_b:
        mid_idx: _type = (left_b + right_b) // 2
        mid_val: _type = arr[mid_idx]

        if mid_val == val:
            return mid_idx
        elif mid_val > val:
            right_b = mid_idx - 1
        else:
            left_b = mid_idx + 1
