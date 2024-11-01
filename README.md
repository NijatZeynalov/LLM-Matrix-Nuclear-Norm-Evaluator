# LLM Matrix Nuclear-Norm Evaluator

## Overview
The **LLM Matrix Nuclear-Norm Evaluator** is a Python tool designed to evaluate the performance of Large Language Models (LLMs) using matrix norms, specifically the nuclear norm, as a measure of various output metrics. The evaluator helps assess different properties of LLMs, such as compression ratios and predictive diversity, allowing researchers and developers to gain insights into the performance and complexity of different models.


## Project Structure
- `llm_matrix_norm_evaluator/`
  - **config.py**: Configuration management for the evaluator, supporting both hard-coded defaults and configurable parameters from `config.json`.
  - **llm_evaluator.py**: Contains the core functionality for evaluating LLMs using matrix norms.
  - **matrix_norm_calculator.py**: Provides calculations for the nuclear norm and L1,2 norm of matrices.
  - **result_visualizer.py**: Handles visualization of evaluation results and saves them to a JSON file.
  - **llm_registry.py**: Manages supported LLMs and their metrics.
- `scripts/`
  - **evaluate_llm.py**: A script for running LLM evaluation from the command line using user-provided arguments.

## Installation
To get started with the LLM Matrix Nuclear-Norm Evaluator, follow these steps:

1. Clone this repository


2. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Configuration
You can customize the evaluation process using the configuration file `config.json`. Here is an example configuration:
```json
{
  "supported_models": ["llama"],
  "default_model": "llama",
  "input_file_path": "model_output.txt",
  "output_file_path": "evaluation_results.json",
  "l1_2_norm_threshold": 0.001
}
```

The configuration allows you to define the supported models, input/output paths, and various parameters for evaluation.

## Running the Evaluation
The evaluation script can be executed from the command line as follows:

```sh
python scripts/evaluate_llm.py --model-name llama --input-file <path/to/input/file> --save-path <path/to/output/file>
```

### Arguments
- `--model-name`: Name of the model to evaluate. Defaults to the value in `config.json`.
- `--input-file`: Path to the input file containing the model's output. Defaults to the value in `config.json`.
- `--save-path`: Path to save the evaluation results.

### Example
```sh
python scripts/evaluate_llm.py --model-name gpt3 --input-file data/sample_output.txt --save-path results/evaluation_gpt3.json
```

