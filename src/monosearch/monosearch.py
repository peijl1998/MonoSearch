from .datatypes.common import LlmConfig, SearchContext
from .query_analyzer import LLMQueryAnalyzer
from .retriever import BochaRetriever
from .ranker import LLMRanker
from .reflex import DefaultReflex
from .summarizer import PlainSummarizer


class MonoSearch:
    def __init__(
        self,
        query_analyzer=None,
        retriever=None,
        ranker=None,
        reflex=None,
        summarizer=None
    ):
        self.query_analyzer = query_analyzer or LLMQueryAnalyzer()
        self.retriever = retriever or BochaRetriever()
        self.ranker = ranker or LLMRanker()
        self.reflex = reflex or DefaultReflex()
        self.summarizer = summarizer or PlainSummarizer()

    def search(self, query: str, llm_config: LlmConfig = LlmConfig(), max_iterations: int = 10) -> str:
        
        context = SearchContext(
            user_query = query,
            llm_config = llm_config
        )
        
        # Query analysis
        query_list = self.query_analyzer.analyze(query, context)
        
        iteration = 0
        while query_list and iteration < max_iterations:
            iteration += 1
            print(f"-----------\033[31mIteration {iteration}\033[0m--------------")
            print(f"\033[31mQueries to process\033[0m\n{query_list}")
            
            # Retrieval
            query_documents = self.retriever.retrieve(query_list, context)
            print(f"\033[31mRetrieval results\033[0m：\n {query_documents.desc()}")
            
            # Ranking
            rank_documents = self.ranker.rank(query_documents, context)
            context.intermediate_results.addResult(rank_documents)
            print(f"\033[31mRanking results\033[0m：\n {rank_documents.desc()}")
            
            # Reflection
            should_continue, new_query_list = self.reflex.reflect(context)
            print(f"\033[31mContinue searching?\033[0m {should_continue}, {new_query_list}")
            print("=========================================")

            query_list = new_query_list
            if not should_continue:
                break
        
        # 总结
        return self.summarizer.summarize(context)