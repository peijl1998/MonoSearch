# MonoSearch

一个简单版本的DeepSearch实现，用于GitHub公开仓库搜索，供学习使用。

## 项目架构

MonoSearch采用模块化、低耦合、可插拔设计，包含以下核心模块：

1. **Query Analyzer**：分析用户查询，将其拆分为多个可能的关键词
2. **Retriever**：召回模块，负责搜索和获取与查询相关的文档
3. **Ranker**：排序筛选模块，对检索到的文档进行排序和筛选
4. **Reflex**：反思模块，基于当前结果判断是否需要追加查询
5. **Summarizer**：总结器，汇总搜索过程和结果，生成最终答案

所有模块共享一个SearchContext上下文，方便参数共享和结果传递。

## 安装

使用uv包管理器安装依赖：

```bash
uv init
uv add -r requirements.txt
```

## 使用方法

```python
from monosearch import MonoSearch

search_engine = MonoSearch()
results = search_engine.search("如何实现一个简单的搜索引擎")
print(results)
```
