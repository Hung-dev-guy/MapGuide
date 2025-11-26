from graph.state import AgentState
from typing import Dict, Any
import pdb
from utils.helper import is_valid_distance, satisfy_rank, satisfy_category


def filter_node(state: AgentState) -> AgentState:
    """
    Filter based on fixed criterias
    """
    print("->Filter Node: Đang thực hiện lọc theo yêu cầu của bạn...")
    user_location = state["user_location"]
    user_category = state["category"]
    restaurants = state['restaurants']

    print(f"-> Filter Node: Kiểm tra thể loại của bạn '{user_category}'")

    filtered_restaurants = []
    for res in restaurants:
        res_category = res.category
        print(f"   Kiểm tra: {res.name} - thể loại: '{res_category}' == '{user_category}' ? {user_category == res_category}")
# 
        if is_valid_distance(user_location, res) and satisfy_rank(state, res) and user_category == res_category:
            filtered_restaurants.append(res)
            print(f"Thỏa mãn: {res.name}")

    print(f"-> Filter Node: Số quán sau khi lọc: {len(filtered_restaurants)}")
    state['restaurants'] = filtered_restaurants
    return state