#!/usr/bin/env python3
from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    initial_index = (page - 1) * page_size
    last_index = page * page_size
    
    return (initial_index, last_index)