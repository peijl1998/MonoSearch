#!/usr/bin/env python
import sys
from monosearch.datatypes.common import LlmConfig
from monosearch.monosearch import MonoSearch


def main():
    if len(sys.argv) <= 1:
        print("Error: Search query parameter is required")
        print("Usage: uv run examples/simple_search.py \"your search query\"")
        sys.exit(1)
        
    query = sys.argv[1]
    print(f"Using query: {query}")
    
    search_engine = MonoSearch()
    model_config = LlmConfig(
        model_name = "Pro/deepseek-ai/DeepSeek-V3"
        # model_name = "Pro/deepseek-ai/DeepSeek-R1"
        # model_name = "Qwen/Qwen3-8B"
    )

    results = search_engine.search(query, model_config, max_iterations=5)

    print(results)


if __name__ == "__main__":
    main() 