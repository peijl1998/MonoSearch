from typing import List

from monosearch.datatypes.common import Document, DocumentSource, QueryDocuments
from monosearch.ability.search.bocha_search import BochaResponse


def bocha_to_query_documents(bocha_response: BochaResponse, handle_image: bool = False) -> List[Document]:
    """
    将BochaResponse转换为Document列表
    
    Args:
        query: 用户查询
        bocha_response: Bocha搜索API的响应
        handle_image: 是否处理图片结果
        
    Returns:
        Document对象列表
    """
    documents = []
    
    if bocha_response and bocha_response.data:
        # 处理网页搜索结果
        if bocha_response.data.webPages and bocha_response.data.webPages.value:
            for page in bocha_response.data.webPages.value:
                doc = Document(
                    id=page.id,
                    content=page.summary,
                    metadata={
                        "raw_page": page
                    },
                    source=DocumentSource.BOCHA,
                    url=page.url,
                    title=page.name
                )
                documents.append(doc)
        
        # 处理图片搜索结果
        if handle_image and bocha_response.data.images and bocha_response.data.images.value:
            for image in bocha_response.data.images.value:
                doc = Document(
                    id=f"img-{image.contentUrl}",
                    content=image.name or "",
                    metadata={
                        "width": image.width,
                        "height": image.height,
                        "thumbnail_url": image.thumbnailUrl,
                        "date_published": image.datePublished,
                        "encoding_format": image.encodingFormat,
                        "host_page_url": image.hostPageUrl,
                        "host_page_display_url": image.hostPageDisplayUrl,
                    },
                    source=DocumentSource.BOCHA,
                    url=image.contentUrl,
                    title=image.name
                )
                documents.append(doc)
    
    return documents
