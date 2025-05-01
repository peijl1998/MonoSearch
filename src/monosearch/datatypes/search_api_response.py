from typing import List, Optional, Any
from pydantic import BaseModel

class WebPage(BaseModel):
    id: str
    name: str
    url: str
    displayUrl: str
    snippet: str
    summary: Optional[str] = None
    siteName: Optional[str] = None
    siteIcon: Optional[str] = None
    datePublished: Optional[str] = None
    dateLastCrawled: Optional[str] = None
    cachedPageUrl: Optional[str] = None
    language: Optional[str] = None
    isFamilyFriendly: Optional[bool] = None
    isNavigational: Optional[bool] = None


class WebPages(BaseModel):
    webSearchUrl: str
    totalEstimatedMatches: Optional[int] = None
    value: List[WebPage]
    someResultsRemoved: Optional[bool] = None


class QueryContext(BaseModel):
    originalQuery: str


class ImageThumbnail(BaseModel):
    width: Optional[int] = None
    height: Optional[int] = None


class Image(BaseModel):
    webSearchUrl: Optional[str] = None
    name: Optional[str] = None
    thumbnailUrl: str
    datePublished: Optional[str] = None
    contentUrl: str
    hostPageUrl: str
    contentSize: Optional[str] = None
    encodingFormat: Optional[str] = None
    hostPageDisplayUrl: str
    width: int = 0
    height: int = 0
    thumbnail: Optional[ImageThumbnail] = None


class Images(BaseModel):
    id: Optional[str] = None
    readLink: Optional[str] = None
    webSearchUrl: Optional[str] = None
    value: List[Image]
    isFamilyFriendly: Optional[bool] = None


class SearchResponseData(BaseModel):
    _type: str = "SearchResponse"
    queryContext: QueryContext
    webPages: Optional[WebPages] = None
    images: Optional[Images] = None
    videos: Optional[Any] = None


class BochaResponse(BaseModel):
    code: int
    log_id: str
    msg: Optional[str] = None
    data: SearchResponseData