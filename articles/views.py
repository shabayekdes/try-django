from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

from .models import Article
from .forms import ArticleForm
from rest_framework import generics
from .serializers import ArticleSerializer

# Create your views here.
def article_search_view(request):
    # query dictionary from get request
    query = request.GET.get('q')
    articles = Article.objects.search(query=query)

    context = {
        'articles': articles,
    }
    return render(request, 'articles/search.html', context=context)

@login_required
def article_create_view(request):
    # print(request.POST)
    form = ArticleForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        article_object = form.save()
        context['form'] = ArticleForm()
        return redirect(article_object.get_absolute_url())

    return render(request, "articles/create.html", context=context)


def article_detail_view(request, slug=None):
    article_obj = None
    if slug is not None:
        try:
            article_obj = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            article_obj = Article.objects.filter(slug=slug).first()
        except:
            raise Http404
    context = {
        'article': article_obj,
    }
    return render(request, 'articles/view.html', context=context)


class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.public()
    serializer_class = ArticleSerializer

class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.public()
    serializer_class = ArticleSerializer
