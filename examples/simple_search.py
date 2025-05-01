#!/usr/bin/env python
"""
MonoSearch简单使用示例。
"""
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.monosearch import MonoSearch
from src.monosearch.utils.logger import get_logger

logger = get_logger("monosearch.example")

def main():
    # 创建MonoSearch实例
    search_engine = MonoSearch(max_iterations=2)
    
    # 执行查询
    query = "Python深度学习框架比较"
    logger.info(f"执行查询: {query}")
    
    # 添加自定义属性
    properties = {
        "language": "zh",
        "sort_by": "relevance"
    }
    
    # 获取搜索结果
    results = search_engine.search(query, properties=properties)
    
    # 打印结果
    print("\n" + "="*80)
    print(results)
    print("="*80 + "\n")
    
    # 打印文档详情
    logger.info(f"找到 {len(results.documents)} 个文档")
    for i, doc in enumerate(results.documents, 1):
        print(f"{i}. {doc}")


if __name__ == "__main__":
    main() 