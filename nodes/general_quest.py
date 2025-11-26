from graph.state import AgentState
from utils.helper import getLLM
from typing import Dict, Any



def general_search_node(state: AgentState) -> dict:
    """
    Xử lý các câu hỏi chung không liên quan đến tìm kiếm quán ăn/bản đồ.
    """
    print("-> General Node: Xử lý câu hỏi chung.")
    llm = getLLM()  
    response = llm.invoke(state["query"])
    state["final_result"] = response.content
    return state