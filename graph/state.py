from typing_extensions import List, Optional, Tuple, Any, Dict
from langgraph.graph import StateGraph
from typing import TypedDict

class Restaurant:
    def __init__(self, name: str, rating: float, location: Tuple[float,float], category: str, distance: Optional[float] = None):
        self.name = name
        self.rating = rating
        self.location = location
        self.category = category
        self.distance = distance  # Optional, có thể tính sau 

class AgentState(TypedDict):
    query: str
    radius: float
    category: str
    rating: int
    user_location: Optional[Tuple[float, float]]
    search_criteria: Optional[str]
    restaurants: List[Dict[str, Any]]
    final_result: str




