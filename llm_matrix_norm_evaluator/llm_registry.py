
from dataclasses import dataclass
import json
import os

@dataclass
class LLMMetrics:
    compression_ratio: float
    predictive_diversity: float

class LLMRegistry:
    def __init__(self, config, registry_path="llm_registry.json"):
        self.config = config
        self.registered_models = self._register_models(registry_path)

    def _register_models(self, registry_path):
        if os.path.exists(registry_path):
            with open(registry_path, "r") as registry_file:
                registry_data = json.load(registry_file)
                return {name: LLMMetrics(**metrics) for name, metrics in registry_data.items()}
        else:
            return {
                "llama": LLMMetrics(compression_ratio=0.8, predictive_diversity=0.9)
            }

    def get_model(self, model_name):
        if model_name in self.registered_models:
            return self.registered_models[model_name]
        else:
            raise ValueError(f"Model '{model_name}' is not supported.")
    