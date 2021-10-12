from typing import List, Dict
from fastapi import APIRouter, Depends
from domain.model import ArticleSchema, CreateArticleSchema
from domain.model.exception import NotFoundException
from domain.service import IArticleRoaster, ArticleRoaster


router = APIRouter(
    prefix='/article',
    tags=['article']
)

# Initialize fake article repository
articles: List[ArticleSchema] = []


@router.get('/')
def get_articles(
    roaster: IArticleRoaster = Depends(lambda: ArticleRoaster(articles)))\
        -> List[ArticleSchema]:
    return roaster.all()


@router.patch('/{id}')
def update_article(
    id: int,
    article: CreateArticleSchema,
    roaster: IArticleRoaster = Depends(lambda: ArticleRoaster(articles)))\
        -> Dict[str, str]:
    if not roaster.update(id, article):
        raise NotFoundException(f'Article with id \'{id}\' not found.')

    return {'message': 'Article has been updated.'}


@router.post('/')
def add_article(article: CreateArticleSchema,
                roaster: IArticleRoaster = Depends(
                    lambda: ArticleRoaster(articles))) -> Dict[str, str]:
    roaster.add(article)
    return {'message': 'New article has been added.'}


@router.delete('/{id}')
def delete_article(id: int,
                   roaster: IArticleRoaster = Depends(
                       lambda: ArticleRoaster(articles))) -> Dict[str, str]:
    if not roaster.delete(id):
        raise NotFoundException(f'Article with id \'{id}\' not found.')
    return {'message': 'Article has been deleted.'}
