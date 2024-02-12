from django.shortcuts import render
from django.http import HttpResponse

from . import util
from django import forms


class NewSearchForm(forms.Form):
    task = forms.CharField(label="Search")


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})
    # return HttpResponse("HELLO WORLD")


def display(request, title):
    # TODO: find the appropiate place to return an error if the entry does not exist
    # TODO: If an entry is requested that does not exist, the user should be presented with an error page indicating that their requested page was not found.
    # TODO: find out how display the markdown content as html
    return render(
        request,
        "encyclopedia/page.html",
        {"entry": util.get_entry(title), "title": title},
    )


def search(request):
    if request.method == "POST":
        # Get the form data
        search_query = request.POST.get("query", "")
        print("Search query:", search_query)
        return HttpResponse("Search query:", search_query)
    # if request.method == "POST":
    #     search_form = NewSearchForm(request.POST)
    #     print(search_form)
    #     if search_form.is_valid():
    #         search = search_form.cleaned_data["form"]
    #         display(request, search_form)
    # elif request.method == "GET":
    #     search_form = NewSearchForm()
    #     return render(request, "encyclopedia/layout.html", {"search_form": search_form})
    # else:
    #     return HttpResponse("ERROR")


# Basic function for debugging as I understand django
def micla(request):
    return HttpResponse("MICLA")
