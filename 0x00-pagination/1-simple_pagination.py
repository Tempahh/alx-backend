import csv
import math
from typing import List

def index_range(page: int, page_size: int) -> tuple:
    initial_index = (page - 1) * page_size
    last_index = page * page_size
    
    return (initial_index, last_index)

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        try:
            assert(int(page) > 0 and int(page_size) > 0)
        except(ValueError, AssertionError):
            return []
        if page < 1 or page_size < 1 or page_size > len(self.dataset()):
            return []
        else:
            start, end = index_range(page, page_size)
            return self.dataset()[start:end]
        