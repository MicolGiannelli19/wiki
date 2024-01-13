from django.shortcuts import render
from django.http import HttpResponse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})
    # return HttpResponse("HELLO WORLD")


def display(request, title):
    return render(
        request,
        "encyclopedia/index.html",
        {"entries": util.list_entries(), "title": title},
    )
