from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class CategoryRanking:
    """
    example:
    {
      "foodImageUrl":
        "https://image.space.rakuten.co.jp/d/strg/ctrl/3/fbd7dd260d736654532e6c0b1ec185a0cede8675.49.2.3.2.jpg",
      "recipeDescription": "そのままでも、ご飯にのせて丼にしても♪",
      "recipePublishday": "2017/10/10 22:37:34",
      "shop": 0,
      "pickup": 0,
      "recipeId": 1760028309,
      "nickname": "はぁぽじ",
      "smallImageUrl":
        "https://image.space.rakuten.co.jp/d/strg/ctrl/3/fbd7dd260d736654532e6c0b1ec185a0cede8675.49.2.3.2.jpg?thum=55",
      "recipeMaterial": [
        "鶏むね肉",
        "塩",
        "酒",
        "片栗粉",
        "○水",
        "○塩",
        "○鶏がらスープの素",
        "○黒胡椒",
        "長ネギ",
        "いりごま",
        "ごま油"
      ],
      "recipeIndication": "約10分",
      "recipeCost": "300円前後",
      "rank": "1",
      "recipeUrl": "https://recipe.rakuten.co.jp/recipe/1760028309/",
      "mediumImageUrl":
        "https://image.space.rakuten.co.jp/d/strg/ctrl/3/fbd7dd260d736654532e6c0b1ec185a0cede8675.49.2.3.2.jpg?thum=54",
      "recipeTitle": "ご飯がすすむ！鶏むね肉のねぎ塩焼き"
    }
    """

    food_image_url: str
    recipe_description: str
    recipe_publishday: str
    shop: int
    pickup: int
    recipe_id: int
    nickname: str
    small_image_url: str
    recipe_material: List[str]
    recipe_indication: str
    recipe_cost: str
    rank: str
    recipe_url: str
    medium_image_url: str
    recipe_title: str


@dataclass
class CategoryRankingResult:
    results: List[Dict[str, Any]]

    def __post_init__(self):
        results = [
            CategoryRanking(**dic_item)
            for dic_item in self.results
        ]
        self.results = results
