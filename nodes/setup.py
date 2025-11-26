# src/nodes/node1_router.py
from graph.state import AgentState
import re

def setup_node(state: 'AgentState') -> dict:
    """
    Trích xuất thông tin từ query: radius, rating, category
    """
    query = state['query'].lower()

    # Trích xuất radius (tìm số + 'm', ví dụ: "500m" hoặc "500 m")
    match_radius = re.search(r'(\d+)\s*m\b', query)
    if match_radius:
        radius_m = int(match_radius.group(1))
        state['radius'] = radius_m / 1000  # Chuyển từ mét sang km

    # Trích xuất rating (tìm số + '*', ví dụ: "3*" hoặc "3 *")
    match_rating = re.search(r'(\d+)\s*\*', query)
    if match_rating:
        state['rating'] = int(match_rating.group(1))

    # Trích xuất category (loại ẩm thực)
    categories = ['việt', 'thái', 'ý', 'nga', 'nhật', 'indo', 'hàn', 'mexico', 'trung', 'pháp', 'đài', 'ấn', 'myanmar']
    for category in categories:
        if category in query:
            state['category'] = category
            break

    print(f"-> Setup Node: radius={state.get('radius')}km, rating={state.get('rating')}*, category={state.get('category')}")
    return state
