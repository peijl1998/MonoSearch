#!/usr/bin/env python
from monosearch.datatypes.common import LlmConfig
from monosearch.monosearch import MonoSearch


def main():
    search_engine = MonoSearch()
    model_config = LlmConfig(
        model_name = "Pro/deepseek-ai/DeepSeek-V3"
        # model_name = "Pro/deepseek-ai/DeepSeek-R1"
        # model_name = "Qwen/Qwen3-8B"
    )
    
    # query = "特朗普最近上任总统后有哪些壮举"
    query = "后摇滚Mono乐队成员研究，最近在中国有哪些演出，演出曲目分别是什么"

    results = search_engine.search(query, model_config, max_iterations=5)

    print(results)


if __name__ == "__main__":
    main() 