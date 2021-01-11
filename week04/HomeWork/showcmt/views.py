import re
from django.shortcuts import render
from django.http import HttpResponse
from .models import Comments


# Create your views here.
def show_comments(request, search=''):
    if search:
        search_words = [i.strip() for i in search.split(' ')]
        pattern = ""
        for sw in search_words:
            pattern += fr'{sw}|'
        pattern = pattern.rstrip('|')
        results = Comments.objects.filter(stars__gt=3, content__regex=pattern)
        show_words = ' '.join(search_words)
    else:
        results = Comments.objects.filter(stars__gt=3)
        show_words = None
    count = results.count()
    return render(request, 'index.html', locals())
