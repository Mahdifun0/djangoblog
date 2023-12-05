from django.shortcuts import render
from . import models


def articleslist(request):
    articles = models.Article.objects.all().order_by("date")

    args = {"articles": articles}

    return render(request, "articles/articleslist.html", args)
