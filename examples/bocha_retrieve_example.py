from monosearch.datatypes.common import LlmConfig, SearchContext
from monosearch.ranker.llm_ranker import LLMRanker
from monosearch.retriever.bocha_retriever import BochaRetriever
from monosearch.query_analyzer.llm_query_analyzer import LLMQueryAnalyzer


def retrieveAndRank():
    qu = LLMQueryAnalyzer()
    retriever = BochaRetriever(count=10, page=1)
    ranker = LLMRanker(max_workers=10)
    
    model_config = LlmConfig(
        # model_name = "Pro/deepseek-ai/DeepSeek-V3"
        model_name = "Qwen/Qwen3-8B"
    )
    
    user_query = "Mono乐队介绍"
    context = SearchContext(
        user_query=user_query,
        llm_config=model_config
    )
    
    queries = qu.analyze(user_query, context)
    print(queries)
    
    query_docs = retriever.retrieve(queries, context)
    ranked_docs = ranker.rank(query_docs, context)

    for key in ranked_docs.getAllKeywords():
        documents = ranked_docs.getDocuments(key)
        print(key, len(documents))
        for doc in documents:
            print(doc.id, doc.content)
        print("--------------" * 10)
        print("\n\n")
        
def main():
    retriever = BochaRetriever(count=10, page=1)
    context = SearchContext(
        user_query="今天上海天气是什么？"
    )
    
    query_docs = retriever.retrieve(["今天上海天气是什么？","上海什么天气","上海实时天气怎么样"], context)

    for key in query_docs.getAllKeywords():
        documents = query_docs.getDocuments(key)
        print(key, len(documents))
        for doc in documents:
            print(doc.id, doc.content)
        print("--------------" * 10)
        print("\n\n")


if __name__ == "__main__":
    retrieveAndRank()
    # main()