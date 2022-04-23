from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.db.models import Q

from .models import Article
from .forms import ArticleForm

# Create your views here.
def articles_search(request):
    # query dictionary from get request
    query = request.GET.get('q')

    article = None
    # if query is not None:
    if query is not None:
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        articles = Article.objects.filter(lookups)
    context = {
        'articles': articles,
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
