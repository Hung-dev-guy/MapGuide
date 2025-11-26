# src/nodes/node1_router.py
from graph.state import AgentState

def router_node(state: AgentState) -> dict:
    """
    Chia nhánh tìm quán ăn và trả lời câu hỏi tổng quát
    """
    query = state['query'].lower()

    if any(keyword in query for keyword in ["khoảng cách", "xa", "bán kính", "m", "xếp hạng", "đánh giá", "phạm vi"]):
        print("-> Router: Chuyển sang luồng tìm quán ăn")
        return {"search_criteria": "Find_restaurants"}
    else:
        print("-> Router: Chuyển sang luồng câu hỏi chung")
        return {"search_criteria": "Answer_general_quest"}

def route_decision(state: AgentState) -> str:
    """
    Hàm để quyết định routing dựa trên search_criteria
    """
    return state.get("search_criteria", "Answer_general_quest")


