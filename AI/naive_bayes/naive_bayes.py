import csv
from collections import defaultdict


class NaiveBayesClassifier:
    def __init__(self, laplace_smoothing=False):
        self.laplace_smoothing = laplace_smoothing
        self.class_probs = {}
        self.cond_probs = {}
        self.classes = []
        self.n_features = 0
        self.feature_values = {}

    def train(self, data, labels):
        n_samples = len(labels)
        self.n_features = len(data[0])
        self.classes = list(set(labels))

        class_count = defaultdict(int)
        for label in labels:
            class_count[label] += 1

        self.class_probs = {cls: count / n_samples for cls, count in class_count.items()}

        for feat_idx in range(self.n_features):
            self.feature_values[feat_idx] = set(row[feat_idx] for row in data)

        cond_count = {
            cls: [defaultdict(int) for _ in range(self.n_features)]
            for cls in self.classes
        }

        for sample, label in zip(data, labels):
            for feat_idx, value in enumerate(sample):
                cond_count[label][feat_idx][value] += 1

        self.cond_probs = {}
        for cls in self.classes:
            self.cond_probs[cls] = []
            for feat_idx in range(self.n_features):
                n_values = len(self.feature_values[feat_idx])
                total = class_count[cls]
                prob_dict = {}
                for value in self.feature_values[feat_idx]:
                    count = cond_count[cls][feat_idx][value]
                    if self.laplace_smoothing:
                        prob_dict[value] = (count + 1) / (total + n_values)
                    else:
                        prob_dict[value] = count / total
                self.cond_probs[cls].append(prob_dict)

    def predict(self, x):
        scores = {}
        for cls in self.classes:
            score = self.class_probs[cls]
            for feat_idx, value in enumerate(x):
                score *= self.cond_probs[cls][feat_idx].get(value, 0)
            scores[cls] = score
        predicted_label = max(scores, key=lambda c: scores[c])
        return predicted_label, scores

    def evaluate(self, test_data, test_labels):
        correct = sum(
            1 for sample, true_label in zip(test_data, test_labels)
            if self.predict(sample)[0] == true_label
        )
        return correct / len(test_labels)


def load_csv(filepath):
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = [row for row in reader]
    feature_names = header[:-1]
    data = [row[:-1] for row in rows]
    labels = [row[-1] for row in rows]
    return data, labels, feature_names





def demo_tennis():
    data, labels, _ = load_csv("tennis.csv")
    split = 10
    model = NaiveBayesClassifier(laplace_smoothing=True)
    model.train(data[:split], labels[:split])
    acc = model.evaluate(data[split:], labels[split:])
    print(f"[Tennis]       Test accuracy: {acc:.2%}  ({round(acc * len(labels[split:]))}/{len(labels[split:])} mau dung)")


def demo_buys_computer():
    data, labels, _ = load_csv("buys_computer.csv")
    split = 10
    model = NaiveBayesClassifier(laplace_smoothing=True)
    model.train(data[:split], labels[:split])
    acc = model.evaluate(data[split:], labels[split:])
    print(f"[buys_computer] Test accuracy: {acc:.2%}  ({round(acc * len(labels[split:]))}/{len(labels[split:])} mau dung)")


if __name__ == "__main__":
    demo_tennis()
    demo_buys_computer()
