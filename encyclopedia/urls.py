from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("micla", views.micla, name="micla"),
    path("search", views.search, name="search"),
    path("<str:title>", views.display_entery_page, name="display"),
]
