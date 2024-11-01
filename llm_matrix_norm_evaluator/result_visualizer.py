
import matplotlib.pyplot as plt
import json

class ResultVisualizer:
    def __init__(self, config):
        self.config = config

    def save_results(self, evaluation_results, save_path):
        with open(save_path, 'w') as f:
            json.dump(evaluation_results, f, indent=4)

    def plot_results(self, evaluation_results, save_path=None):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

        ax1.bar([r["model_name"] for r in evaluation_results], [r["matrix_nuclear_norm"] for r in evaluation_results])
        ax1.set_title("Matrix Nuclear-Norm")
        ax1.set_xlabel("Model")
        ax1.set_ylabel("Nuclear-Norm")

        ax2.bar([r["model_name"] for r in evaluation_results], [r["compression_ratio"] for r in evaluation_results], label="Compression Ratio")
        ax2.bar([r["model_name"] for r in evaluation_results], [r["predictive_diversity"] for r in evaluation_results], label="Predictive Diversity")
        ax2.set_title("Model Metrics")
        ax2.set_xlabel("Model")
        ax2.set_ylabel("Metric")
        ax2.legend()

        if save_path:
            plt.savefig(save_path)
        plt.show()
    