from django.shortcuts import render

from .models import Article

# Create your views here.
def articles_list(request):
    
    # query dictionary from get request
    query_dict = request.GET # this is a dictionary

    try:
        # get the value of the key 'q'
        query = int(query_dict.get('q'))
    except:
        query = None

    article = None
    # if query is not None:
    if query is not None:
        article = Article.objects.get(id=query)
    
    context = {
        'article': article,
    }
    return render(request, 'articles/search.html', context=context)

def view_article(request, id=None):
    article = None
    if id is not None:
        article = Article.objects.get(id=id)
        
    context = {
        'article': article,
    }
    return render(request, 'articles/view.html', context=context)
