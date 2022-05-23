from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register


from .models import Article


@register(Article)
class ArtcileIndex(AlgoliaIndex):
    should_index = 'is_public'
    fields = [
        'title',
        'content',
        'user',
        'published_at',
        'path',
        'endpoint',
    ]
    settings = {
        'searchableAttributes': ['title', 'content'],
        'attributesForFaceting': ['user'],
        'ranking': ['asc(published_at)']
    }
    tags = 'get_tags_list'
