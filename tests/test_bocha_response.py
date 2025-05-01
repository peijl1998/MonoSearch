import json
import sys
import os

# 添加项目根目录到sys.path，以便导入模块
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.monosearch.ability.search.bocha_search import BochaResponse

# 示例响应
example_response = {
    'code': 200, 
    'log_id': '1d3930977cb26dd4', 
    'msg': None, 
    'data': {
        '_type': 'SearchResponse', 
        'queryContext': {
            'originalQuery': '天空为什么是蓝色的？'
        }, 
        'webPages': {
            'webSearchUrl': 'https://bochaai.com/search?q=天空为什么是蓝色的？', 
            'totalEstimatedMatches': None, 
            'value': [
                {
                    'id': 'https://api.bochaai.com/v1/#WebPages.0', 
                    'name': '一个看似简单实则很复杂的问题:天为什么是蓝的?|粒子|天空|波长|大气层|太阳光_网易订阅', 
                    'url': 'https://www.163.com/dy/article/JSG1D0ED0511A3AG.html?f=post1603_tab_news', 
                    'displayUrl': 'https://www.163.com/dy/article/JSG1D0ED0511A3AG.html?f=post1603_tab_news', 
                    'snippet': '"天空是什么颜色的?" 这是孩子们充满好奇,常常提出的问题。每当这时,大人们往往会毫不犹豫地回答:"天空是蓝色的呀!"但是天空为什么是蓝色的呢?当孩子紧接着抛出这个问题,许多人就不知如何作答了。有人或',
                    'summary': '详细摘要内容...',
                    'siteName': '网易', 
                    'siteIcon': 'https://th.bochaai.com/favicon?domain_url=https://www.163.com/dy/article/JSG1D0ED0511A3AG.html?f=post1603_tab_news', 
                    'datePublished': '2025-04-06T19:17:00+08:00', 
                    'dateLastCrawled': '2025-04-06T19:17:00Z'
                }
            ], 
            'someResultsRemoved': True
        }, 
        'images': {
            'id': None, 
            'readLink': None, 
            'webSearchUrl': None, 
            'value': [
                {
                    'thumbnailUrl': 'https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2025%2F0406%2F5e196d3bj00suana5001gd000u000irm.jpg&thumbnail=660x2147483647&quality=80&type=jpg', 
                    'contentUrl': 'https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2025%2F0406%2F5e196d3bj00suana5001gd000u000irm.jpg&thumbnail=660x2147483647&quality=80&type=jpg', 
                    'hostPageUrl': 'https://www.163.com/dy/article/JSG1D0ED0511A3AG.html?f=post1603_tab_news', 
                    'hostPageDisplayUrl': 'https://www.163.com/dy/article/JSG1D0ED0511A3AG.html?f=post1603_tab_news', 
                    'width': 0, 
                    'height': 0
                }
            ]
        }
    }
}

def test_bocha_response():
    """测试BochaResponse类能否正确解析API响应"""
    try:
        response = BochaResponse.model_validate(example_response)
        print("成功解析API响应")
        print(f"查询: {response.data.queryContext.originalQuery}")
        print(f"搜索结果数量: {len(response.data.webPages.value) if response.data.webPages else 0}")
        print(f"图片数量: {len(response.data.images.value) if response.data.images else 0}")
        return True
    except Exception as e:
        print(f"解析失败: {e}")
        return False

if __name__ == "__main__":
    test_bocha_response() 