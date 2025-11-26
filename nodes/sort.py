from graph.state import AgentState
from typing import Dict, Any
from utils.helper import calc_res_distance

def sort_node(state: AgentState) -> dict:
    """
    Sắp xếp (Sort) theo tiêu chí ưu tiên ('rating' hoặc 'distance').
    """
    print("-> Sort Node: Đang thực hiện Sắp xếp và Định dạng kết quả.")
    restaurants = state['restaurants']
    query = state['query'].lower()
    user_location = state['user_location']

    if 'khoảng cách' in query or 'gần' in query:
        # Sắp xếp theo khoảng cách 
        restaurants.sort(key=lambda r: (calc_res_distance(r, user_location), -r.rating))
        print("-> Sort Node: Đã sắp xếp ưu tiên khoảng cách gần nhất.")
    elif 'xếp hạng' in query or 'rating' in query or 'đánh giá' in query:
        # Sắp xếp theo rating 
        restaurants.sort(key=lambda r: (-r.rating, calc_res_distance(r, user_location)))
        print("-> Sort Node: Đã sắp xếp ưu tiên Rating cao nhất.")
    else:
        # Mặc định sắp xếp theo rating
        restaurants.sort(key=lambda r: -r.rating)
        print("-> Sort Node: Sắp xếp mặc định theo rating.")

    if restaurants:
        result_list = []
        for idx, res in enumerate(restaurants, 1):
            distance = calc_res_distance(res, user_location)
            result_list.append(
                f"{idx}. {res.name} - Rating: {res.rating}⭐ - Khoảng cách: {distance}km - Loại: {res.category}"
            )
        rtr = '\n'.join(result_list)
        state["final_result"] = "Đây là danh sách các quán ăn mà tôi đã tìm theo yêu cầu của bạn nha!\n" \
                                + f"{rtr}\nChúc bạn ngon miệng với lựa chọn của mình nhé:)))"
    else:
        state["final_result"] = "Rất tiếc, không tìm thấy quán ăn nào phù hợp với yêu cầu của bạn. Bạn thử mở rộng phạm vi tìm kiếm nhé!"

    return state