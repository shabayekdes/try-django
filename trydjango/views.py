"""
To render html web pages
"""
import random
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from articles.models import Article


def home_view(request):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    # first method to create data in model
    # TODO: remove comment below to create data in model
    # obj = Article(title='Hello World', content='This is awesome')
    # obj.save()
    # second method to create data in model
    # Remove comment below to create data in model
    # Article.objects.create(title='Hello World Again', content='This is awesome')

    name = "Shabayek"
    random_id = random.randint(1, 4) # pseudo random

    # fetch one by id
    article_obj = Article.objects.get(id=random_id)
    # fetch all articles
    articles = Article.objects.all()

    # context will be passed to view
    context = {
        'articles': articles,
        'id': article_obj.id,
        'title': article_obj.title,
        'content': article_obj.content,
    }

    # Django Templates
    # First method using get_template
    # TODO: remove comment below to use get_template
    # temp = get_template('home_view.html')
    # HTML_STRING = temp.render(context=context)

    # Second method using render_to_string
    # TODO: remove comment below to use render_to_string
    HTML_STRING = render_to_string('home_view.html', context=context)

    return HttpResponse(HTML_STRING)
