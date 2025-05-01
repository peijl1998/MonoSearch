from typing import List
from abc import ABC, abstractmethod

from ..datatypes.common import SearchContext, Document, QueryDocuments
from ..utils import ThreadPool


class BaseRetriever(ABC):
    def retrieve(self, query_list: List[str], context: SearchContext, max_workers: int = None) -> QueryDocuments:
        """
        并行召回
        
        Args:
            query_list: 关键词列表
            context: 搜索上下文
            max_workers: 最大线程数
            
        Returns:
            QueryDocuments: 查询文档结果
        """
        # 使用线程池并行处理每个查询
        def process_query(query):
            documents = self.retrieve_single(query, context)
            return query, documents
        
        # 并行执行召回
        results = ThreadPool.map(lambda q: process_query(q), query_list, max_workers=max_workers)
        
        # 合并结果
        merged_results = QueryDocuments()
        for query, documents in results:
            merged_results.addDocuments(query, documents)
            
        return merged_results
    
    @abstractmethod
    def retrieve_single(self, query: str, context: SearchContext) -> List[Document]:
        """子类需要实现此方法"""
        return []
