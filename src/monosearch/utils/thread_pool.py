import threading
from typing import List, Callable, Any, TypeVar, Generic, Dict
from concurrent.futures import ThreadPoolExecutor, as_completed

T = TypeVar('T')
R = TypeVar('R')


class ThreadPool:
    """线程池工具类"""
    
    @staticmethod
    def map(func: Callable[[T], R], items: List[T], max_workers: int = None) -> List[R]:
        """
        并行执行函数，返回结果列表
        
        Args:
            func: 需要执行的函数
            items: 函数输入列表
            max_workers: 最大线程数
            
        Returns:
            List[R]: 函数执行结果列表
        """
        results = []
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(func, item): item for item in items}
            for future in as_completed(futures):
                result = future.result()
                results.append(result)
        return results
    
    @staticmethod
    def map_with_key(func: Callable[[T], R], items_dict: Dict[Any, T], max_workers: int = None) -> Dict[Any, R]:
        """
        并行执行函数，返回字典结果
        
        Args:
            func: 需要执行的函数
            items_dict: 函数输入字典
            max_workers: 最大线程数
            
        Returns:
            Dict[Any, R]: 函数执行结果字典
        """
        results = {}
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_key = {executor.submit(func, item): key for key, item in items_dict.items()}
            for future in as_completed(future_to_key):
                key = future_to_key[future]
                result = future.result()
                results[key] = result
        return results 