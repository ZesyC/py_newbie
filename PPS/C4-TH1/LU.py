def in_ma_tran(a):
    for dong in a:
        print("[ " + "  ".join(f"{x:8.3f}" for x in dong) + " ]")
    print()


def tach_lu(a):
    n = len(a)
    a = [list(map(float, dong)) for dong in a]
    l = [[0.0 for _ in range(n)] for _ in range(n)]
    u = [[0.0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        l[i][i] = 1.0

    print("Ma trận A:")
    in_ma_tran(a)

    for i in range(n):
        print(f"Tính dòng {i + 1} của U:")
        for j in range(i, n):
            tong = 0.0
            for k in range(i):
                tong += l[i][k] * u[k][j]
            u[i][j] = a[i][j] - tong
            print(f"U{i + 1}{j + 1} = {u[i][j]:.3f}")

        if abs(u[i][i]) < 1e-12:
            print("Không thể tách LU vì phần tử chính bằng 0.")
            return None, None

        print(f"Tính cột {i + 1} của L:")
        for j in range(i + 1, n):
            tong = 0.0
            for k in range(i):
                tong += l[j][k] * u[k][i]
            l[j][i] = (a[j][i] - tong) / u[i][i]
            print(f"L{j + 1}{i + 1} = {l[j][i]:.3f}")

        print("Ma trận L hiện tại:")
        in_ma_tran(l)
        print("Ma trận U hiện tại:")
        in_ma_tran(u)

    print("Kết quả tách A = L * U:")
    print("Ma trận L:")
    in_ma_tran(l)
    print("Ma trận U:")
    in_ma_tran(u)

    return l, u


def giai_lu(a):
    n = len(a)
    A = [dong[:-1] for dong in a]
    b = [float(dong[-1]) for dong in a]

    l, u = tach_lu(A)
    if l is None or u is None:
        return None

    y = [0.0] * n
    print("Giải Ly = b:")

    for i in range(n):
        tong = 0.0
        for j in range(i):
            tong += l[i][j] * y[j]
        y[i] = (b[i] - tong) / l[i][i]
        print(f"y{i + 1} = ({b[i]:.3f} - {tong:.3f}) / {l[i][i]:.3f} = {y[i]:.3f}")

    x = [0.0] * n
    print("Giải Ux = y:")

    for i in range(n - 1, -1, -1):
        tong = 0.0
        for j in range(i + 1, n):
            tong += u[i][j] * x[j]

        if abs(u[i][i]) < 1e-12:
            print("Gặp 0 trên đường chéo chính, không thể chia.")
            return None

        x[i] = (y[i] - tong) / u[i][i]
        print(f"x{i + 1} = ({y[i]:.3f} - {tong:.3f}) / {u[i][i]:.3f} = {x[i]:.3f}")

    print("Nghiệm của hệ:")
    for i, gia_tri in enumerate(x, start=1):
        print(f"x{i} = {gia_tri:.3f}")

    return x


def vi_du():
    a = [
        [3, -1, 4, 2],
        [17, 2, 1, 14],
        [1, 12, -7, 54],
    ]

    return giai_lu(a)

vi_du()