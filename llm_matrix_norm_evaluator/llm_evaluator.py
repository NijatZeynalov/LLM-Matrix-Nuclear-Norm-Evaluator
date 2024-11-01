
import numpy as np
from .matrix_norm_calculator import MatrixNormCalculator
from .llm_registry import LLMRegistry

class LLMEvaluator:
    def __init__(self, config):
        self.config = config
        self.matrix_norm_calculator = MatrixNormCalculator(config)
        self.llm_registry = LLMRegistry(config)

    def evaluate_llm(self, model_name, input_file):
        try:
            model = self.llm_registry.get_model(model_name)
            model_output = np.loadtxt(input_file)
            matrix_norm = self.matrix_norm_calculator.matrix_nuclear_norm(model_output)
            return {
                "model_name": model_name,
                "matrix_nuclear_norm": matrix_norm,
                "compression_ratio": model.compression_ratio,
                "predictive_diversity": model.predictive_diversity
            }
        except FileNotFoundError:
            raise FileNotFoundError(f"The input file '{input_file}' does not exist.")
        except ValueError:
            raise ValueError(f"Failed to read model output from '{input_file}'. Ensure it is properly formatted.")
    