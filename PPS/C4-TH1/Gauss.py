def in_ma_tran(a):
    for dong in a:
        he_so = "  ".join(f"{x:8.3f}" for x in dong[:-1])
        ket_qua = f"{dong[-1]:8.3f}"
        print(f"[ {he_so} | {ket_qua} ]")
    print()


def giai_gauss(a):
    n = len(a)
    a = [list(map(float, dong)) for dong in a]

    print("Ma trận ban đầu:")
    in_ma_tran(a)

    for cot in range(n):
        print(f"Chọn cột {cot + 1} làm cột khử.")

        if abs(a[cot][cot]) < 1e-12:
            dong_doi = -1
            for dong in range(cot + 1, n):
                if abs(a[dong][cot]) > 1e-12:
                    dong_doi = dong
                    break

            if dong_doi == -1:
                print("Không tìm được phần tử chính khác 0.")
                print("Hệ có thể vô nghiệm hoặc vô số nghiệm.")
                return None

            a[cot], a[dong_doi] = a[dong_doi], a[cot]
            print(f"Đổi dòng {cot + 1} với dòng {dong_doi + 1}:")
            in_ma_tran(a)

        phan_tu_chinh = a[cot][cot]
        print(f"Phần tử chính = {phan_tu_chinh:.3f}")

        for dong in range(cot + 1, n):
            he_so = a[dong][cot] / phan_tu_chinh
            print(
                f"Khử dòng {dong + 1}: "
                f"D{dong + 1} = D{dong + 1} - ({he_so:.3f}) * D{cot + 1}"
            )

            for j in range(cot, n + 1):
                a[dong][j] = a[dong][j] - he_so * a[cot][j]

            in_ma_tran(a)

    x = [0.0] * n
    print("Bắt đầu thế ngược:")

    for i in range(n - 1, -1, -1):
        tong_da_biet = 0.0
        for j in range(i + 1, n):
            tong_da_biet += a[i][j] * x[j]

        if abs(a[i][i]) < 1e-12:
            print("Gặp 0 trên đường chéo chính, không thể chia.")
            return None

        x[i] = (a[i][n] - tong_da_biet) / a[i][i]
        print(
            f"x{i + 1} = ({a[i][n]:.3f} - {tong_da_biet:.3f}) "
            f"/ {a[i][i]:.3f} = {x[i]:.3f}"
        )

    print("\nNghiệm của hệ:")
    for i, gia_tri in enumerate(x, start=1):
        print(f"x{i} = {gia_tri:.3f}")

    return x


def vi_du():
    a = [
        [3, -1, 4, 2],
        [17, 2, 1, 14],
        [1, 12, -7, 54],
    ]

    return giai_gauss(a)

vi_du()