from django.shortcuts import render
from .models import Article

# Create your views here.

def articles_list(request):
    # Whatever logic we need to write in our view.
    articles = Article.objects.all()
    context = {
        "articles" : articles,
    }
    return render(request, "articles_list.html", context)

