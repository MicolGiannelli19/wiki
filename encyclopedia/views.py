from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from markdown2 import markdown

from . import util
from django import forms

# TODO: the search functionality should definetly not be case sensitive 
# BUG: editing  a page does not delete the old one 

def index(request):
    return render(
        request,
        "encyclopedia/index.html",
        {"entries": util.list_entries(), "title": "Home Page"},
    )


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
                        if search_query.lower() in element.lower()
                    ],
                    "title": "Search Results",
                },
            )


import random


# NOTE: this could also be achieved by repurposing the search function or maybe having a load page function which is called by both

def random_page(request):
    random_page = random.choice(util.list_entries())
    return display_entery_page(request, random_page)


class EntryForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(widget=forms.Textarea(), label="Content")


def new_page(request):
    # Subitting a new form
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form = EntryForm(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the task from the 'cleaned' version of form data
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            # Append title to the content
            content = f"#{title}\n\n{content}"

            # TODO: Maybe shoudl catch it in a nicer way
            if title in util.list_entries():
                return HttpResponse("ERROR: Entry already exists")

            # Save the new entry
            util.save_entry(title, content)

            # line for debugging outupt
            # return HttpResponse(f"Title: {title} Content: {content}, {typecontent} ")

            # Redirect user to list of tasks
            return HttpResponseRedirect(reverse("encyclopedia:index"))
        else:
            # If the form is invalid, re-render the page with existing information.
            return render(request, "encyclopedia/new_page.html", {"form": form})
    else:
        return render(
            request,
            "encyclopedia/new_page.html",
            {"form": EntryForm()},
        )


def edit_page(request, title):
    if request.method == "POST":
        # Take in the data the user submitted and save it as form
        form = EntryForm(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the entry from the 'cleaned' version of form data
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            # Append title to the content
            util.save_entry(title, content)

        return display_entery_page(request, title)

    else:
        entry = util.get_entry(title)

        entry_form = EntryForm({"title": title, "content": entry})
        # return HttpResponse(f"calling the edit page function for title: {title}")
        return render(
            request, "encyclopedia/edit.html", {"title": title, "form": entry_form}
        )
        # return render("encyclopedia/new_page.html", {"form": entry_form})
