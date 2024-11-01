
import json
import os

class Config:
    def __init__(self, config_path="config.json"):
        if os.path.exists(config_path):
            with open(config_path, "r") as config_file:
                config_data = json.load(config_file)
                self.supported_models = config_data.get("supported_models", ["llama"])
                self.default_model = config_data.get("default_model", "llama")
                self.input_file_path = config_data.get("input_file_path", "model_output.txt")
                self.output_file_path = config_data.get("output_file_path", "evaluation_results.json")
                self.l1_2_norm_threshold = config_data.get("l1_2_norm_threshold", 1e-3)
        else:
            # Fallback to default values if config file is not available
            self.supported_models = ["llama"]
            self.default_model = "llama"
            self.input_file_path = "model_output.txt"
            self.output_file_path = "evaluation_results.json"
            self.l1_2_norm_threshold = 1e-3
    