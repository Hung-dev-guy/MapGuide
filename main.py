from graph.builder import GraphBuilder
from graph.state import AgentState
from utils.helper import MOCK_LOCATION
while True:
    print("Chào fennn, để tôi tìm quán ăn ngon gần đây giúp bạn nha! Hãy để tôi gợi ý giúp bạn nhỉ:>>>")
    print("1. Bạn muốn chọn quán ăn cách đây trong phạm vi bao nhiêu? (đơn vị m, ví dụ 100m)")
    print("2. Bạn muốn chọn quán ăn ẩm thực của nước nào? (Việt, Thái, Trung, Hàn, Nhật, Pháp, Ý, Nga)")
    print("3. Bạn muốn chọn quán ăn được xếp hạng từ mấy sao trở lên? (kí hiệu bằng *, điểm số từ 1 đến 10, ví dụ 8*)")
    print("4. Bạn muốn sắp xếp ưu tiên theo tiêu chí nào? khoảng cách hay xếp hạng?")
    """
    Giả sử:
Tôi muốn ăn quán nhật, phạm vi 500m, xếp hạng 3* trở lên, sắp xếp ưu tiên theo khoảng cách nhé!
    """
    query = input()
    builder = GraphBuilder()
    app = builder.compile()
    result = app.invoke(AgentState(query=query, radius=None, rating=None, category=None, user_location=MOCK_LOCATION, search_criteria=None, restaurants=[], final_result=""))
    print(f"\nKẾT QUẢ: {result["final_result"]}\n")


