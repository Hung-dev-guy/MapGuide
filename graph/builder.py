from langgraph.graph import StateGraph, END
from graph.state import AgentState

from nodes.router import router_node, route_decision
from nodes.setup import setup_node
from nodes.general_quest import general_search_node
from nodes.map_search import map_search_node
from nodes.filter import filter_node
from nodes.sort import sort_node


class GraphBuilder:
    def __init__(self):
        self.workflow = StateGraph(AgentState)

    def add_nodes(self):
        """Thêm tất cả các nodes vào graph"""
        print("Đang thêm nodes...")
        self.workflow.add_node("router", router_node)
        self.workflow.add_node("setup_node", setup_node)
        self.workflow.add_node("general_search_node", general_search_node)
        self.workflow.add_node("map_search_node", map_search_node)
        self.workflow.add_node("filter_node", filter_node)
        self.workflow.add_node("sort_node", sort_node)

    def add_edges(self):
        """Thiết lập điểm bắt đầu, các cạnh có điều kiện và cạnh thông thường"""
        print("Thiết lập Edges...")

        # 1. Điểm bắt đầu
        self.workflow.set_entry_point("router")

        # 2. Conditional edges từ router
        self.workflow.add_conditional_edges(
            "router",
            route_decision,  # Sử dụng hàm route_decision để quyết định
            {
                "Find_restaurants": "setup_node",
                "Answer_general_quest": "general_search_node"
            }
        )

        # 3. Luồng tìm kiếm quán ăn
        self.workflow.add_edge("setup_node", "map_search_node")
        self.workflow.add_edge("map_search_node", "filter_node")
        self.workflow.add_edge("filter_node", "sort_node")
        self.workflow.add_edge("sort_node", END)

        # 4. Luồng câu hỏi chung
        self.workflow.add_edge("general_search_node", END)

    def compile(self):
        """Biên dịch đồ thị và trả về ứng dụng LangGraph"""
        print("Biên dịch LangGraph...")
        self.add_nodes()
        self.add_edges()
        return self.workflow.compile()


if __name__ == "__main__":
    try:
        builder = GraphBuilder()
        app = builder.compile()
        print("\n✅ Đồ thị LangGraph đã biên dịch thành công!")

    except ImportError as e:
        print(f"\n⚠️ Lỗi: Thiếu một số file node cần thiết. {e}")
    except Exception as e:
        print(f"\n❌ Lỗi khi biên dịch hoặc chạy: {e}")