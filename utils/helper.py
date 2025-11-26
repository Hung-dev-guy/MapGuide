import os
import math
from typing import List, Dict, Any, Tuple, Optional
from dotenv import load_dotenv
from graph.state import Restaurant, AgentState
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()

MOCK_LOCATION = (21.0285, 105.8542)
MOCK_RESTAURANTS = [
    Restaurant(name="Phở Gia Truyền Bát Đàn", rating=4.5, location=(21.0295, 105.8552), category="việt"),
    Restaurant(name="Pizza 4P's Tràng Tiền", rating=4.9, location=(21.0275, 105.8538), category="việt"),
    Restaurant(name="Bún Chả Hương Liên", rating=4.2, location=(21.0255, 105.8562), category="việt"),
    Restaurant(name="Highlands Coffee Nhà Hát Lớn", rating=3.8, location=(21.0288, 105.8545), category="việt"),
    Restaurant(name="Cơm Tấm Sài Gòn", rating=4.0, location=(21.0310, 105.8580), category="việt"),
    Restaurant(name="Thái Lan Quán", rating=4.3, location=(21.0300, 105.8570), category="thái"),
    Restaurant(name="Pizza Ý Napoli", rating=4.7, location=(21.0260, 105.8520), category="ý"),
    Restaurant(name="Borscht Nga", rating=4.4, location=(21.0240, 105.8550), category="nga"),
    Restaurant(name="Sushi Nhật Bản", rating=4.6, location=(21.0290, 105.8530), category="nhật"),
    Restaurant(name="Nasi Goreng Indo", rating=4.1, location=(21.0270, 105.8560), category="indo"),
    Restaurant(name="Bibimbap Hàn Quốc", rating=4.5, location=(21.0285, 105.8540), category="hàn"),
    Restaurant(name="Tacos Mexico", rating=4.2, location=(21.0250, 105.8525), category="mexico"),
    Restaurant(name="Dim Sum Trung Quốc", rating=4.3, location=(21.0265, 105.8555), category="trung"),
    Restaurant(name="Baguette Pháp", rating=4.4, location=(21.0275, 105.8535), category="pháp"),
]


def getLLM():
    api_key = os.environ.get("GEMINI_API_KEY")
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key)
    return llm

def get_all_restaurants() -> List[Restaurant]:
    print(f"-> Helper: Đang tìm kiếm quán ăn...")
    return MOCK_RESTAURANTS

def calc_res_distance(res, user_location: Tuple[float, float]) -> float:
    """
    Tính khoảng cách từ user_location đến nhà hàng sử dụng công thức Haversine.

    Args:
        res: Restaurant object hoặc Dictionary chứa thông tin nhà hàng
        user_location: Tọa độ người dùng (latitude, longitude)

    Returns:
        Khoảng cách tính bằng km
    """
    user_lat = user_location[0]
    user_lon = user_location[1]

    # Xử lý cả Restaurant object và dictionary
    if isinstance(res, dict):
        res_lat = res['latitude']
        res_lon = res['longitude']
    else:
        # Restaurant object với thuộc tính location là tuple (lat, lon)
        res_lat = res.location[0]
        res_lon = res.location[1]

    # Công thức Haversine để tính khoảng cách chính xác cho tọa độ địa lý
    lat1, lon1 = math.radians(user_lat), math.radians(user_lon)
    lat2, lon2 = math.radians(res_lat), math.radians(res_lon)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))

    # Bán kính Trái Đất (km)
    radius = 6371.0
    distance = c * radius
    return round(distance, 1)

def get_valid_distance_res(origin: Tuple[float, float], restaurants: List, limit_distance: float) -> List:
    """
    Lọc các nhà hàng nằm trong phạm vi khoảng cách cho phép.

    Args:
        origin: Tọa độ người dùng (latitude, longitude)
        restaurants: Danh sách Restaurant objects hoặc dictionaries
        limit_distance: Giới hạn khoảng cách tính bằng km

    Returns:
        Danh sách các nhà hàng thỏa mãn điều kiện khoảng cách
    """
    res_lis = []
    for res in restaurants:
        distance = calc_res_distance(res, origin)
        if distance <= limit_distance:
            res_lis.append(res)
    return res_lis


def is_valid_distance(user_location: Optional[Tuple[float, float]], res: Restaurant, max_distance_km: float = 5.0) -> bool:
    if user_location is None:
        return False
    distance = calc_res_distance(res, user_location)
    return distance <= max_distance_km

def satisfy_rank(state: AgentState, res: Restaurant, min_rating: float = 3.5) -> bool:
    if not hasattr(res, 'rating') or res.rating is None:
        return False  # Không có thông tin rating
    search_criteria = state.get('search_criteria', '')
    if search_criteria == 'rating':
        min_rating = 4.0
    return res.rating >= min_rating


def satisfy_category(user_category: str, res: Restaurant) -> bool:

    categories= [
        'vietnamese', 'thái',
        'ý', 'nga',
        'nhật', 'indo',
        'hàn', 'mexico',
        'trung', 'pháp'
    ]
    # Nếu query có chứa từ khóa cụ thể về loại hình, lọc theo đó
    for category in categories:
        if user_category.lower() == category:
            return True
    return False