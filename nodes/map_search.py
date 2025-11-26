from graph.state import AgentState
from utils.helper import (
    get_valid_distance_res,
    get_all_restaurants,
    MOCK_RESTAURANTS
)
from typing import Dict, Any
import pdb

def map_search_node(state: AgentState) -> AgentState:
    """
    Thực hiện chức năng tìm kiếm quán ăn
    """
    print("-> Map Search Node: Bắt đầu tìm kiếm theo yêu cầu của bạn")
    query = state['query']
    criteria = state['search_criteria']
    limit_distance = state['radius']
    user_location = state['user_location']
    all_restaurants = MOCK_RESTAURANTS
    suitable_distance_res = get_valid_distance_res(user_location, all_restaurants, limit_distance)
    state['restaurants'] = suitable_distance_res

    return state