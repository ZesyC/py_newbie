# Import deque de tao hang doi hai dau, dung cho BFS lay phan tu dau nhanh.
from collections import deque


# Dinh nghia lop cai dat thuat toan Iterative Deepening Search IDS.
class IterativeDeepeningSearch:
    # Ham khoi tao nhan vao do thi, dinh bat dau va dinh dich.
    def __init__(self, graph: dict, start, goals):
        # Luu do thi dang dictionary, moi dinh tro toi danh sach dinh ke.
        self.graph = graph
        # Luu dinh xuat phat.
        self.start = start
        # Neu goals la chuoi thi dua vao set 1 phan tu, neu khong thi ep thanh set.
        self.goals = {goals} if isinstance(goals, str) else set(goals)

    # Ham chay IDS voi do sau toi da va tuy chon in chi tiet tung buoc.
    def ids(self, max_depth: int = 50, verbose: bool = False):
        # Luu tat ca cac dinh da duyet qua moi lan tang gioi han do sau.
        all_closed = []

        # Lap gioi han do sau tu 0 den max_depth.
        for limit in range(max_depth + 1):
            # Khoi tao stack open, moi phan tu gom dinh hien tai va duong di toi dinh do.
            op = [(self.start, [self.start])]
            # Danh sach cac dinh da mo rong trong lan lap hien tai.
            closed = []
            # Dictionary luu cha cua tung dinh de truy vet duong di.
            parent = {self.start: None}
            # Bien dem so buoc mo rong.
            step = 0

            # Neu bat verbose thi in gioi han do sau dang xet.
            if verbose:
                # In ra muc gioi han do sau hien tai.
                print(f"Gioi han do sau = {limit}:")

            # Lap den khi stack open rong.
            while op:
                # Lay phan tu cuoi stack theo co che LIFO cua DFS.
                x, path = op.pop()
                # Tang so thu tu buoc.
                step += 1
                # Tinh do sau hien tai bang so canh trong path.
                depth = len(path) - 1

                # Dua dinh hien tai vao danh sach da mo rong.
                closed.append(x)

                # Kiem tra neu dinh hien tai la mot trong cac dinh dich.
                if x in self.goals:
                    # Gop cac dinh da mo rong cua lan lap nay vao danh sach tong.
                    all_closed.extend(closed)
                    # Neu bat verbose thi in trang thai tai buoc tim thay dich.
                    if verbose:
                        # In dinh dang thong tin buoc, open va close.
                        print(
                            f"Buoc {step}:\n"
                            f"X = {x}, depth = {depth},\n"
                            f"open = {[node for node, _ in op]},\n"
                            f"close = {closed}\n"
                        )
                    # Tra ve duong di truy vet duoc va tat ca dinh da mo rong.
                    return self._reconstruct(parent, x), all_closed

                # Chi mo rong dinh con neu chua vuot qua gioi han do sau.
                if depth < limit:
                    # Duyet danh sach dinh ke theo thu tu dao nguoc de khi pop ra van dung thu tu goc.
                    for child in reversed(self.graph.get(x, [])):
                        # Lay danh sach ten dinh dang co trong stack open.
                        open_nodes = [node for node, _ in op]
                        # Chi them dinh con neu khong tao chu trinh va chua nam trong open/closed.
                        if child not in path and child not in closed and child not in open_nodes:
                            # Them dinh con vao stack, kem theo duong di moi.
                            op.append((child, path + [child]))
                            # Luu cha cua dinh con la dinh hien tai.
                            parent[child] = x

                # Neu bat verbose thi in trang thai sau khi xu ly xong buoc hien tai.
                if verbose:
                    # In dinh dang thong tin buoc, dinh dang xet, open va close.
                    print(
                        f"Buoc {step}:\n"
                        f"X = {x}, depth = {depth},\n"
                        f"open = {[node for node, _ in op]},\n"
                        f"close = {closed}\n"
                    )

            # Neu khong tim thay trong gioi han nay, gop closed vao danh sach tong.
            all_closed.extend(closed)

            # Neu bat verbose thi bao khong tim thay o gioi han hien tai.
            if verbose:
                # In thong bao khong tim thay tai do sau limit.
                print(f"Khong tim thay o do sau {limit}\n")

        # Neu het moi gioi han ma van khong thay, tra ve None va danh sach da duyet.
        return None, all_closed

    # Ham truy vet duong di tu dinh dich ve dinh bat dau bang dictionary parent.
    def _reconstruct(self, parent, goal):
        # Khoi tao path rong va bien cur bat dau tu dinh dich.
        path, cur = [], goal
        # Lap nguoc theo cha cho den khi gap None o dinh bat dau.
        while cur is not None:
            # Them dinh hien tai vao duong di dang nguoc.
            path.append(cur)
            # Di len dinh cha cua cur.
            cur = parent[cur]
        # Dao nguoc lai de co duong di tu start den goal.
        return list(reversed(path))


# Dinh nghia lop cai dat thuat toan Breadth First Search BFS.
class BreadthFirstSearch:
    # Ham khoi tao nhan vao do thi, dinh bat dau va dinh dich.
    def __init__(self, graph: dict, start, goals):
        # Luu do thi dang dictionary.
        self.graph = graph
        # Luu dinh xuat phat.
        self.start = start
        # Chuyen goals thanh set de kiem tra thuoc tap hop nhanh hon.
        self.goals = {goals} if isinstance(goals, str) else set(goals)

    # Ham chay BFS va co the in chi tiet neu verbose=True.
    def bfs(self, verbose: bool = False):
        # Tao hang doi open ban dau chi co dinh start.
        op = deque([self.start])
        # Danh sach cac dinh da mo rong.
        closed = []
        # Luu cha cua tung dinh de truy vet duong di.
        parent = {self.start: None}

        # Bien dem so buoc mo rong.
        step = 0
        # Lap den khi hang doi open rong.
        while op:
            # Lay dinh dau hang doi theo co che FIFO cua BFS.
            x = op.popleft()
            # Tang so thu tu buoc.
            step += 1

            # Dua dinh hien tai vao danh sach da mo rong.
            closed.append(x)

            # Neu dinh hien tai la dich thi dung tim kiem.
            if x in self.goals:
                # Neu bat verbose thi in trang thai tai buoc tim thay dich.
                if verbose:
                    # In dinh dang thong tin buoc, open va close.
                    print(
                        f"Buoc {step}:\n"
                        f"X = {x},\n"
                        f"open = {list(op)},\n"
                        f"close = {closed}\n"
                    )
                # Tra ve duong di truy vet duoc va danh sach dinh da mo rong.
                return self._reconstruct(parent, x), closed

            # Duyet cac dinh ke cua dinh hien tai.
            for child in self.graph.get(x, []):
                # Chi them dinh con neu chua mo rong va chua nam trong hang doi.
                if child not in closed and child not in op:
                    # Them dinh con vao cuoi hang doi.
                    op.append(child)
                    # Luu cha cua dinh con la dinh hien tai.
                    parent[child] = x

            # Neu bat verbose thi in trang thai sau khi xu ly xong buoc hien tai.
            if verbose:
                # In dinh dang thong tin buoc, dinh dang xet, open va close.
                print(
                    f"Buoc {step}:\n"
                    f"X = {x},\n"
                    f"open = {list(op)},\n"
                    f"close = {closed}\n"
                )

        # Neu khong tim thay dich, tra ve None va danh sach da mo rong.
        return None, closed

    # Ham truy vet duong di tu dinh dich ve dinh bat dau bang dictionary parent.
    def _reconstruct(self, parent, goal):
        # Khoi tao path rong va bien cur bat dau tu dinh dich.
        path, cur = [], goal
        # Lap nguoc theo cha cho den khi gap None o dinh bat dau.
        while cur is not None:
            # Them dinh hien tai vao duong di dang nguoc.
            path.append(cur)
            # Di len dinh cha cua cur.
            cur = parent[cur]
        # Dao nguoc lai de co duong di tu start den goal.
        return list(reversed(path))


# Ham tinh tong chi phi cua mot duong di dua tren bang trong so weights.
def tinh_chi_phi_duong_di(path, weights):
    # Neu khong co duong di thi khong co chi phi.
    if path is None:
        # Tra ve None de bieu dien khong tinh duoc chi phi.
        return None

    # Khoi tao tong chi phi bang 0.
    cost = 0
    # Duyet tung cap dinh lien tiep tren duong di.
    for current_node, next_node in zip(path, path[1:]):
        # Tao canh theo chieu current_node -> next_node.
        edge = (current_node, next_node)
        # Neu canh khong co trong weights, thu chieu nguoc lai vi do thi vo huong.
        if edge not in weights:
            # Doi canh sang chieu next_node -> current_node.
            edge = (next_node, current_node)
        # Cong trong so cua canh vao tong chi phi.
        cost += weights[edge]
    # Tra ve tong chi phi duong di.
    return cost


# Ham bien danh sach dinh thanh chuoi duong di de in ra dep hon.
def dinh_dang_duong_di(path):
    # Neu path la None nghia la khong tim thay duong di.
    if path is None:
        # Tra ve thong bao khong tim thay.
        return "Khong tim thay"
    # Noi cac dinh bang dau gach ngang de tao chuoi duong di.
    return " - ".join(path)


# Ham in bang so sanh ket qua IDS va BFS.
def in_bang_so_sanh(ids_path, ids_closed, bfs_path, bfs_closed, weights):
    # Tinh chi phi duong di IDS.
    ids_cost = tinh_chi_phi_duong_di(ids_path, weights)
    # Tinh chi phi duong di BFS.
    bfs_cost = tinh_chi_phi_duong_di(bfs_path, weights)

    # In dong trong va tieu de bang so sanh.
    print("\nBANG SO SANH")
    # In nhan cua phan IDS.
    print("IDS:")
    # In duong di IDS sau khi dinh dang.
    print(f"- Duong di: {dinh_dang_duong_di(ids_path)}")
    # In chi phi duong di IDS.
    print(f"- Chi phi: {ids_cost}")
    # In so luong trang thai IDS da mo rong.
    print(f"- So trang thai mo rong: {len(ids_closed)}")
    # In thu tu cac dinh IDS da duyet.
    print(f"- Thu tu duyet: {ids_closed}")

    # In dong trong va nhan cua phan BFS.
    print("\nBFS:")
    # In duong di BFS sau khi dinh dang.
    print(f"- Duong di: {dinh_dang_duong_di(bfs_path)}")
    # In chi phi duong di BFS.
    print(f"- Chi phi: {bfs_cost}")
    # In so luong trang thai BFS da mo rong.
    print(f"- So trang thai mo rong: {len(bfs_closed)}")
    # In thu tu cac dinh BFS da duyet.
    print(f"- Thu tu duyet: {bfs_closed}")


# Ham in nhan xet ve su khac nhau giua IDS va BFS trong bai nay.
def in_nhan_xet():
    # In dong trong va tieu de nhan xet.
    print("\nNHAN XET")
    # In nhan xet ve duong di ngan nhat theo so canh.
    print(
        "- Ca IDS va BFS deu tim duoc duong di ngan nhat theo so canh la "
        "A - C - G - I, voi chi phi bang 3."
    )
    # In nhan xet ve so trang thai BFS mo rong.
    print(
        "- BFS mo rong it trang thai hon trong bai nay vi no duyet theo tung "
        "muc va khong lap lai cac dinh da dua vao hang doi."
    )
    # In nhan xet ve viec IDS phai duyet lai nhieu lan.
    print(
        "- IDS ton nhieu lan mo rong hon vi phai chay lai tu dinh A voi cac "
        "gioi han do sau tang dan, nen mot so dinh bi duyet lai nhieu lan."
    )


# Ham chinh cho phan 2: tao du lieu, chay IDS/BFS va in ket qua.
def bai_phan_2():
    # In tieu de chuong trinh.
    print("PHAN 2: CODING VA DOI SANH IDS - BFS")

    # Khai bao do thi vo huong bang danh sach ke.
    graph = {
        # Dinh A noi voi B va C.
        "A": ["B", "C"],
        # Dinh B noi voi A, D va E.
        "B": ["A", "D", "E"],
        # Dinh C noi voi A, F va G.
        "C": ["A", "F", "G"],
        # Dinh D noi voi B.
        "D": ["B"],
        # Dinh E noi voi B va H.
        "E": ["B", "H"],
        # Dinh F noi voi C va H.
        "F": ["C", "H"],
        # Dinh G noi voi C va I.
        "G": ["C", "I"],
        # Dinh H noi voi E, F va I.
        "H": ["E", "F", "I"],
        # Dinh I noi voi G va H.
        "I": ["G", "H"],
    }

    # Khai bao trong so cac canh cua do thi.
    weights = {
        # Canh A-B co chi phi 1.
        ("A", "B"): 1,
        # Canh A-C co chi phi 1.
        ("A", "C"): 1,
        # Canh B-D co chi phi 1.
        ("B", "D"): 1,
        # Canh B-E co chi phi 1.
        ("B", "E"): 1,
        # Canh C-F co chi phi 1.
        ("C", "F"): 1,
        # Canh C-G co chi phi 1.
        ("C", "G"): 1,
        # Canh E-H co chi phi 1.
        ("E", "H"): 1,
        # Canh F-H co chi phi 1.
        ("F", "H"): 1,
        # Canh G-I co chi phi 1.
        ("G", "I"): 1,
        # Canh H-I co chi phi 1.
        ("H", "I"): 1,
    }

    # Gan dinh xuat phat la A.
    start = "A"
    # Gan dinh dich la I.
    goal = "I"

    # In dinh xuat phat.
    print(f"Dinh xuat phat: {start}")
    # In dinh dich.
    print(f"Dinh dich: {goal}")

    # Tao doi tuong IDS voi do thi, dinh bat dau va dinh dich.
    ids_search = IterativeDeepeningSearch(graph, start=start, goals=goal)
    # Chay IDS voi do sau toi da 10 va khong in tung buoc.
    ids_path, ids_closed = ids_search.ids(max_depth=10, verbose=False)

    # Tao doi tuong BFS voi do thi, dinh bat dau va dinh dich.
    bfs_search = BreadthFirstSearch(graph, start=start, goals=goal)
    # Chay BFS va khong in tung buoc.
    bfs_path, bfs_closed = bfs_search.bfs(verbose=False)

    # In bang so sanh ket qua cua IDS va BFS.
    in_bang_so_sanh(ids_path, ids_closed, bfs_path, bfs_closed, weights)
    # In nhan xet cuoi cung.
    in_nhan_xet()


# Kiem tra file co dang duoc chay truc tiep hay khong.
if __name__ == "__main__":
    # Neu chay truc tiep file nay thi goi ham bai_phan_2.
    bai_phan_2()
