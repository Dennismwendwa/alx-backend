#!/usr/bin/env python3
"""This script return tuple of start and end indexs"""


def index_range(page: int, page_size: int) -> tuple:
    """This function return the start and end indexs"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
