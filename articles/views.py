from django.shortcuts import render, HttpResponse
from . import models


def articleslist(request):
    articles = models.Article.objects.all().order_by("-date")

    args = {"articles": articles}

    return render(request, "articles/articleslist.html", args)


def article_detail(request, slug):
    article = models.Article.objects.get(slug=slug)
    return render(request, "articles/article_detail.html", {"article": article})
