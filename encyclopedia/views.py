from django.shortcuts import render
from django.http import HttpResponse
from markdown2 import markdown

from . import util
from django import forms


class NewSearchForm(forms.Form):
    task = forms.CharField(label="Search")


def index(request):
    return render(
        request,
        "encyclopedia/index.html",
        {"entries": util.list_entries(), "title": "Home Page"},
    )
    # return HttpResponse("HELLO WORLD")


def display_entery_page(request, title):
    # TODO: find the appropiate place to return an error if the entry does not exist
    # TODO: If an entry is requested that does not exist, the user should be presented with an error page indicating that their requested page was not found.
    # TODO: find out how display the markdown content as html
    markdown_content = markdown(util.get_entry(title))
    if title not in util.list_entries():
        # TODO: find out if you should render an error page or jsut  this http response
        return HttpResponse("ERROR: Entry not found")
    return render(
        request,
        "encyclopedia/page.html",
        {"entry": markdown_content, "title": title},
    )


# should this be a django form or a simple html form?
def search(request):
    if request.method == "POST":
        # Get the form data
        search_query = request.POST.get("query", "")
        if search_query in util.list_entries():
            return display_entery_page(request, search_query)
        else:
            return render(
                request,
                "encyclopedia/index.html",
                {
                    "entries": [
                        element
                        for element in util.list_entries()
                        if search_query in element
                    ],
                    "title": "Search Results",
                },
            )


# NOTE: this could also be achieved by repurposing the search function or maybe having a load page function which is called by both
def random_page(request):
    #  TODO: edit this to be a random page
    random_page = "CSS"
    return display_entery_page(request, random_page)
