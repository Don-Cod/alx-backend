#!/usr/bin/env python3
"""2. Hypermedia pagination"""
import csv
import math
from typing import List, Tuple


class Server:
    """Server for popular baby names database.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """List of rows from dataset."""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        start, end = index_range(page, page_size)
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return pagination info."""
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            'page_size': len(self.get_page(page, page_size)),
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """A start index and an end index."""
    return ((page - 1) * page_size, page * page_size)


if __name__ == "__main__":
    server = Server()

    print(server.get_hyper(1, 2))
    print("---")
    print(server.get_hyper(2, 2))
    print("---")
    print(server.get_hyper(100, 3))
    print("---")
    print(server.get_hyper(3000, 100))
