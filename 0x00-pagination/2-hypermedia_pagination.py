#!/usr/bin/env python3
"""This script imprements hypermedia pagination"""
import math
import importlib


module_name = "1-simple_pagination"
class_name = "Server"

module = importlib.import_module(module_name)
BaseServer = getattr(module, class_name)


class Server(BaseServer):
    """This is class server extetion of base class (server)"""
    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """This method returns data paginated as dict"""
        page_data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            "page_size": len(page_data),
            "page": page,
            "data": page_data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }
