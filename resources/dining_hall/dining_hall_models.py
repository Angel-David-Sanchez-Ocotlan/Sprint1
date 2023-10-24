from __future__ import annotations
from pydantic import BaseModel
from typing import List,Dict

from resources.rest_models import Link


class DiningHallModel(BaseModel):
    dining_hall: str
    staff: list[str]
    menu_items: Dict[str,Dict]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "dining_hall": "Ferris Booth Commons",
                    "staff": ["Angel", "Mauricio", "Otito"],
                    "menu_items": {
                        "breakfast": {
                            "main_line": ["pancakes", "scrambled eggs", "sausage gravy"],
                            "vegan_station": ["broccoli", "tofu scramble"]
                        },
                        "lunch": {
                            "main_line": ["pancakes", "scrambled eggs"],
                            "action_station": ["grilled cheese"],
                            "daily_pizza": ["cheese pizza", "vegan cheese pizza"],
                            "vegan_staion": ["pasta", "asparagus"]
                        },
                        "dinner": {
                            "main_line": ["fried chicken", "kale with curried apples"],
                            "vegan_station": ["vegan chicken", "dirty rice"],
                            "action_station": ["chicken quesadillas", "vegetarian quesadillas"]
                        }
                    }
                }
            ]
        }
    }


class DiningHallRspModel(DiningHallModel):
    links: List[Link] = None



