import os
import logging

logger = logging.getLogger(__name__)

def get_bocha_api_key() -> str:
    api_key = os.environ.get("BOCHA_API_KEY")
    if not api_key:
        logger.error("BOCHA_API_KEY not found in environment variables")
        return ""
    return api_key

def get_silicon_flow_api_key() -> str:
    api_key = os.environ.get("SILICON_FLOW_API_KEY")
    if not api_key:
        logger.error("SILICON_FLOW_API_KEY not found in environment variables")
        return ""
    return api_key
