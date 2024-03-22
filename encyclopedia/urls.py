from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("<str:title>", views.display_entery_page, name="display"),
    path("random", views.random_page, name="random"),
]
# TODO: find out how to actually call random page, I am not sure you want a seperate url
