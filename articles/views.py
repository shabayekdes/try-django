from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Article
from .forms import ArticleForm

# Create your views here.
def articles_search(request):
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

@login_required
def articles_create(request):
    # print(request.POST)
    form = ArticleForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        article_object = form.save()
        context['form'] = ArticleForm()

    return render(request, "articles/create.html", context=context)


def articles_view(request, id=None):
    article = None
    if id is not None:
        article = Article.objects.get(id=id)
        
    context = {
        'article': article,
    }
    return render(request, 'articles/view.html', context=context)
