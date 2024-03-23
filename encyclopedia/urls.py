from django.urls import path

from . import views

# NOTE: when you search for a url it will go thorugh them in the order they appear in here
app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("random", views.random_page, name="random"),
    path("new_page", views.new_page, name="new_page"),
    path("<str:title>", views.display_entery_page, name="display"),
    path("<str:title>/edit", views.edit_page, name="edit"),
    # path("random", views.random_page, name="random"),
]
# TODO: find out how to actually call random page, I am not sure you want a seperate url
