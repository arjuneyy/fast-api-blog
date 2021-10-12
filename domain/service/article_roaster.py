from abc import ABC, abstractmethod
from typing import List
from domain.model import ArticleSchema
from domain.model.article import CreateArticleSchema


class IArticleRoaster(ABC):

    @abstractmethod
    def all(self) -> List[ArticleSchema]:
        pass

    @abstractmethod
    def add(self, article: CreateArticleSchema) -> None:
        pass

    @abstractmethod
    def update(self, id: int, article: CreateArticleSchema) -> bool:
        pass

    @abstractmethod
    def delete(self, id: int) -> bool:
        pass


class ArticleRoaster(IArticleRoaster):

    def __init__(self, articles: List[ArticleSchema] = []) -> None:
        self._articles: List[ArticleSchema] = articles

    def all(self) -> List[ArticleSchema]:
        return self._articles

    def add(self, article: CreateArticleSchema) -> None:
        id = self._articles[-1].id + 1 if self._articles else 1
        art = ArticleSchema(**article.dict(), id=id)

        self._articles.append(art)

    def update(self, id: int, article: CreateArticleSchema) -> bool:
        found = False
        for idx, data in enumerate(self._articles):
            if data.id == id:
                self._articles[idx] = ArticleSchema(**article.dict(), id=id)
                found = True
                break

        return found

    def delete(self, id: int) -> bool:
        found = False
        for idx, data in enumerate(self._articles):
            if data.id == id:
                del self._articles[idx]
                found = True
                break

        return found
