import csv
import math
from pathlib import Path


class SVMCustom:
    def __init__(self, c: float = 10.0, gamma: float = 0.5,
                 tolerance: float = 1e-3, max_passes: int = 20):
        self.c = c
        self.gamma = gamma
        self.tolerance = tolerance
        self.max_passes = max_passes
        self.x_train = []
        self.y_train = []
        self.alphas = []
        self.bias = 0.0

    def fit(self, x_train: list[list[float]], y_train: list[int]):
        self.x_train = x_train
        self.y_train = y_train
        n_samples = len(x_train)
        self.alphas = [0.0] * n_samples
        passes = 0

        while passes < self.max_passes:
            changed_alphas = 0

            for i in range(n_samples):
                error_i = self._decision_at(i) - y_train[i]
                violates_kkt = (
                    (y_train[i] * error_i < -self.tolerance and self.alphas[i] < self.c)
                    or (y_train[i] * error_i > self.tolerance and self.alphas[i] > 0)
                )

                if not violates_kkt:
                    continue

                j = self._select_second_index(i, error_i)
                error_j = self._decision_at(j) - y_train[j]
                alpha_i_old = self.alphas[i]
                alpha_j_old = self.alphas[j]

                lower, upper = self._bounds(i, j)
                if lower == upper:
                    continue

                eta = 2 * self._kernel(x_train[i], x_train[j]) \
                    - self._kernel(x_train[i], x_train[i]) \
                    - self._kernel(x_train[j], x_train[j])
                if eta >= 0:
                    continue

                self.alphas[j] -= y_train[j] * (error_i - error_j) / eta
                self.alphas[j] = max(lower, min(upper, self.alphas[j]))

                if abs(self.alphas[j] - alpha_j_old) < 1e-5:
                    self.alphas[j] = alpha_j_old
                    continue

                self.alphas[i] += y_train[i] * y_train[j] * (alpha_j_old - self.alphas[j])

                b1 = self.bias - error_i \
                    - y_train[i] * (self.alphas[i] - alpha_i_old) * self._kernel(x_train[i], x_train[i]) \
                    - y_train[j] * (self.alphas[j] - alpha_j_old) * self._kernel(x_train[i], x_train[j])
                b2 = self.bias - error_j \
                    - y_train[i] * (self.alphas[i] - alpha_i_old) * self._kernel(x_train[i], x_train[j]) \
                    - y_train[j] * (self.alphas[j] - alpha_j_old) * self._kernel(x_train[j], x_train[j])

                if 0 < self.alphas[i] < self.c:
                    self.bias = b1
                elif 0 < self.alphas[j] < self.c:
                    self.bias = b2
                else:
                    self.bias = (b1 + b2) / 2

                changed_alphas += 1

            passes = passes + 1 if changed_alphas == 0 else 0

        return self

    def predict(self, x_test: list[list[float]]):
        return [1 if self.decision_function(x) >= 0 else -1 for x in x_test]

    def decision_function(self, x: list[float]):
        score = self.bias
        for alpha, y, x_train in zip(self.alphas, self.y_train, self.x_train):
            if alpha > 0:
                score += alpha * y * self._kernel(x_train, x)
        return score

    def _decision_at(self, index: int):
        return self.decision_function(self.x_train[index])

    def _select_second_index(self, first_index: int, first_error: float):
        errors = [self._decision_at(i) - self.y_train[i] for i in range(len(self.x_train))]
        candidates = [i for i in range(len(self.x_train)) if i != first_index]
        return max(candidates, key=lambda i: abs(first_error - errors[i]))

    def _bounds(self, i: int, j: int):
        if self.y_train[i] != self.y_train[j]:
            return (
                max(0.0, self.alphas[j] - self.alphas[i]),
                min(self.c, self.c + self.alphas[j] - self.alphas[i])
            )
        return (
            max(0.0, self.alphas[i] + self.alphas[j] - self.c),
            min(self.c, self.alphas[i] + self.alphas[j])
        )

    def _kernel(self, x1: list[float], x2: list[float]):
        squared_distance = sum((a - b) ** 2 for a, b in zip(x1, x2))
        return math.exp(-self.gamma * squared_distance)


def doc_du_lieu(file_path: Path):
    with file_path.open(encoding="utf-8-sig", newline="") as file:
        rows = list(csv.DictReader(file))

    x_data = [[float(row["x1"]), float(row["x2"])] for row in rows]
    y_data = [int(row["y"]) for row in rows]
    return x_data, y_data


def bai_svm():
    data_path = Path(__file__).with_name("svm_data.csv")
    x_data, y_data = doc_du_lieu(data_path)

    print("Bai SVM custom tren du lieu x1, x2:")
    print(f"So mau: {len(x_data)}, so dac trung: {len(x_data[0])}\n")

    model = SVMCustom(c=10.0, gamma=0.5, max_passes=20)
    model.fit(x_data, y_data)
    predictions = model.predict(x_data)
    actual = y_data
    correct = sum(pred == label for pred, label in zip(predictions, actual))

    print("Ket qua tren tap du lieu:")
    for index, (pred, label) in enumerate(zip(predictions, actual), start=1):
        print(f"Mau {index:2}: du doan = {pred:2}, thuc te = {label:2}")

    print(f"\nDo chinh xac train: {correct / len(actual):.2%}")
    print(f"So support vectors: {sum(alpha > 1e-5 for alpha in model.alphas)}")


if __name__ == "__main__":
    bai_svm()
