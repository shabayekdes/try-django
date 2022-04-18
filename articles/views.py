from django.shortcuts import render

from .models import Article

# Create your views here.
def view_article(request, id=None):
    article = None
    if id is not None:
        article = Article.objects.get(id=id)
        
    context = {
        'article': article,
    }
    return render(request, 'articles/view.html', context=context)
