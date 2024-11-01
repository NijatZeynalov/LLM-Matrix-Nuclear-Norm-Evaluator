
import argparse
import os
from llm_matrix_norm_evaluator.config import Config
from llm_matrix_norm_evaluator.llm_evaluator import LLMEvaluator
from llm_matrix_norm_evaluator.result_visualizer import ResultVisualizer

def main():
    parser = argparse.ArgumentParser(description='Evaluate an LLM using Matrix Nuclear-Norm')
    parser.add_argument('--model-name', type=str, default=Config().default_model, help='Name of the model to evaluate')
    parser.add_argument('--input-file', type=str, default=Config().input_file_path, help='Path to the input file containing the model output')
    parser.add_argument('--save-path', type=str, default="evaluation_results.json", help='Path to save the evaluation results')
    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        raise FileNotFoundError(f"The input file '{args.input_file}' does not exist.")

    config = Config()
    evaluator = LLMEvaluator(config)
    visualizer = ResultVisualizer(config)

    try:
        evaluation_results = evaluator.evaluate_llm(args.model_name, args.input_file)
        visualizer.save_results(evaluation_results, args.save_path)
        visualizer.plot_results([evaluation_results])
    except ValueError as e:
        print(f"Error during evaluation: {e}")

if __name__ == "__main__":
    main()
    