from pydantic import BaseModel

class ProductReport(BaseModel):
    product_name: str
    mention_count: int

class ChannelActivity(BaseModel):
    channel_name: str
    total_messages: int

class SearchResult(BaseModel):
    message_id: int
    message_text: str

class VisualContent(BaseModel):
    detected_class: str
    total: int
