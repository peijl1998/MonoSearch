"""
反思模块实现。
"""
from typing import List, Dict, Any, Optional, Tuple, Set
from abc import ABC, abstractmethod

from ..datatypes.common import SearchContext, Document


class BaseReflex(ABC):
    """反思模块基类"""
    
    @abstractmethod
    def reflect(self, context: SearchContext) -> Tuple[bool, List[str]]:
        """基于当前搜索结果反思，决定是否需要生成新的查询"""
        pass


class SimpleReflex(BaseReflex):
    """简单反思模块，基于文档数量和关键词提取生成新查询"""
    
    def __init__(self, min_documents: int = 5, min_confidence: float = 0.5):
        """
        初始化简单反思模块。
        
        Args:
            min_documents: 判断结果是否足够的最小文档数
            min_confidence: 结果相关性的最小置信度
        """
        self.min_documents = min_documents
        self.min_confidence = min_confidence
    
    def reflect(self, context: SearchContext) -> Tuple[bool, List[str]]:
        """
        基于当前结果反思并生成新查询
        
        Args:
            context: 搜索上下文
            
        Returns:
            Tuple[bool, List[str]]: (是否继续搜索, 新的查询列表)
        """
        # 检查当前结果数量
        if len(context.ranked_documents) >= self.min_documents:
            # 检查结果质量
            avg_score = self._calculate_average_score(context.ranked_documents)
            if avg_score >= self.min_confidence:
                # 结果足够好，不需要继续搜索
                return False, []
        
        # 生成新的查询
        new_queries = self._generate_new_queries(context)
        
        # 如果没有新查询，结束搜索
        if not new_queries:
            return False, []
        
        return True, new_queries
    
    def _calculate_average_score(self, documents: List[Document]) -> float:
        """
        计算文档的平均分数
        
        Args:
            documents: 文档列表
            
        Returns:
            float: 平均分数
        """
        if not documents:
            return 0.0
        
        total_score = 0.0
        count = 0
        
        for doc in documents:
            if doc.score is not None:
                total_score += doc.score
                count += 1
        
        return total_score / count if count > 0 else 0.0
    
    def _generate_new_queries(self, context: SearchContext) -> List[str]:
        """
        基于当前结果生成新的查询
        
        Args:
            context: 搜索上下文
            
        Returns:
            List[str]: 新的查询列表
        """
        original_query = context.original_request.query
        used_queries = set(context.all_queries)
        new_queries = []
        
        # 从文档中提取新的关键词
        keywords = self._extract_keywords_from_documents(context.ranked_documents)
        
        # 组合关键词和原始查询
        for keyword in keywords:
            combined_query = f"{original_query} {keyword}"
            if combined_query not in used_queries:
                new_queries.append(combined_query)
        
        # 限制新查询数量
        return new_queries[:3]  # 最多返回3个新查询
    
    def _extract_keywords_from_documents(self, documents: List[Document]) -> Set[str]:
        """
        从文档中提取关键词
        
        Args:
            documents: 文档列表
            
        Returns:
            Set[str]: 关键词集合
        """
        # 简单实现：从文档标题中提取词
        keywords = set()
        
        for doc in documents:
            if doc.title:
                # 分割标题并提取词
                words = [w for w in doc.title.split() if len(w) > 3]
                keywords.update(words)
        
        return keywords


# 默认使用简单反思模块
Reflex = SimpleReflex 