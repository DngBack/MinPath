import networkx as nx


def update_weights(G, blocked):
    """Cập nhật trọng số của các cạnh trong đồ thị.

    Args:
      G: Đồ thị.
      blocked: Danh sách các ID của đỉnh bị chặn.

    Returns:
      None.
    """

    for u, v, d in G.edges(data=True):
        # Nếu đỉnh u bị chặn, thì gán trọng số 1000 cho cạnh (u, v).
        if u in blocked:
            d["weight"] = 1000
        # Nếu đỉnh v bị chặn, thì gán trọng số 1000 cho cạnh (v, u).
        if v in blocked:
            d["weight"] = 1000


def find_shortest_path(G, start, target, blocked):
    """Tìm đường đi ngắn nhất từ đỉnh start đến đỉnh target, mà không đi qua các đỉnh bị chặn.

    Args:
      G: Đồ thị.
      start: ID của đỉnh bắt đầu.
      target: ID của đỉnh kết thúc.
      blocked: Danh sách các ID của đỉnh bị chặn.

    Returns:
      Một danh sách các ID của các đỉnh trên đường đi ngắn nhất.
    """

    # Khởi tạo tập các đỉnh đã được thăm dò.
    visited = set()

    # Tạo một hàng đợi ưu tiên để lưu các đỉnh chưa được thăm dò.
    queue = [(0, start)]

    # Vòng lặp cho đến khi tìm thấy đường đi.
    while queue:
        # Lấy đỉnh có trọng số đường đi ngắn nhất từ hàng đợi ưu tiên.
        _, current = queue.pop(0)

        # Nếu đỉnh hiện tại là đích, thì trả về đường đi.
        if current == target:
            return [current]

        # Nếu đỉnh hiện tại không bị chặn, thì thêm nó vào tập các đỉnh đã được thăm dò và thêm các đỉnh kề của nó vào hàng đợi ưu tiên.
        if current not in blocked:
            visited.add(current)
            for neighbor in G[current]:
                if neighbor not in visited:
                    queue.append((current + G[current][neighbor]["weight"], neighbor))

    # Nếu không tìm thấy đường đi, thì trả về None.
    return None


def main():
    # Khởi tạo đồ thị
    G = nx.Graph()

    # Thêm các đỉnh
    for i in range(1, 10):
        G.add_node(i)

    # Thêm các cạnh
    for i in range(1, 10):
        for j in range(1, 10):
            if i != j:
                G.add_edge(i, j, weight=5)

    # Khởi tạo danh sách các đỉnh bị chặn
    blocked = []

    # Cho camera 5 bị cháy
    blocked.append(5)

    # Cập nhật trọng số của các cạnh
    update_weights(G, blocked)

    # Tìm đường đi
    path = find_shortest_path(G, 4, 2, blocked)

    # In ra đường đi
    print(path)


if __name__ == "__main__":
    main()
