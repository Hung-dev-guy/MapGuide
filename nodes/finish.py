# src/nodes/finish.py

from graph.state import AgentState
from typing import Dict, Any

def finish_node(state: AgentState) -> Dict[str, Any]:
    print("-> Finish Node: Quy trình hoàn tất. Đang trả về kết quả.")
    return state