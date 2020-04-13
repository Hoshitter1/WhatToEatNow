from dataclasses import dataclass
from typing import List, Dict, Any, Callable

import requests

from .utils import camel_to_snake
from .structure import CategoryRankingResult


# TODO: Update all once another client is added based on common functions amd usage

# @dataclass
class ClientBase:
    pass
#     __params: Dict[str, Any] = {}
#     __result: Any = {}
#     response: Any = {}
#
#     @property
#     def params(self):
#         return self.__params
#
#     @property
#     def result(self) -> Callable:  # TODO: Fix Type hint
#         raise NotImplementedError('')


class Rakuten(ClientBase):
    RAKUTEN_ENDPOINT = 'https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426'

    @property
    def params(self):
        self.__params = {
            'format': 'json',
            'applicationId': '1026784267881105216',
            'affiliateId': '1adaf0cf.8672fd67.1adaf0d0.c9778a1f',
            # 'categoryType': 'small'
        }
        return self.__params

    def result(self):
        snaked_data: List[Dict[str, Any]] = [
            {
                camel_to_snake(key): value
                for key, value in camel_dict.items()
            }
            for camel_dict in self.response
        ]
        # self.__result =
        return snaked_data

    @classmethod
    def request(cls) -> property:
        # breakpoint()
        instance = cls()
        res = requests.get(
            instance.RAKUTEN_ENDPOINT,
            params={
            'format': 'json',
            'applicationId': '1026784267881105216',
            'affiliateId': '1adaf0cf.8672fd67.1adaf0d0.c9778a1f',
            # 'categoryType': 'small'
        }
        )
        # breakpoint()
        instance.response = res.json()
        return CategoryRankingResult(instance.result)
