from pydantic import BaseModel
from typing import Optional


class ArticleSchema(BaseModel):
    id: int
    title: str
    description: Optional[str]


class CreateArticleSchema(BaseModel):
    title: str
    description: Optional[str]
