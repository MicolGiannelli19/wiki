 # Django Wiki 

 This project was done as an assignment to the Harvard CS50W course. 

 With in it I reproduced a basic version of Wikipedia where you can add and edit enteries to showcase my newly aquired Django skills 
# My Project

This is an example project.

![Example GIF](./wiki.gif)



 Here are the objectives I achieved when doing this project> 

1. [X] Entry Page: Visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry, should render a page that displays the contents of that encyclopedia entry.
       [X] The view should get the content of the encyclopedia entry by calling the appropriate util function.
        If an entry is requested that does not exist, the user should be presented with an error page indicating that their requested page was not found.
        [X] If the entry does exist, the user should be presented with a page that displays the content of the entry. The title of the page should include the name of the entry.
        
2. [X] Index Page: Update index.html such that, instead of merely listing the names of all pages in the encyclopedia, user can click on any entry name to be taken directly to that entry page.
    
3. [X] Search: Allow the user to type a query into the search box in the sidebar to search for an encyclopedia entry.
        [X]If the query matches the name of an encyclopedia entry, the user should be redirected to that entry’s page.
        [x]If the query does not match the name of an encyclopedia entry, the user should instead be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring. For example, if the search query were ytho, then Python should appear in the search results.
        [x]Clicking on any of the entry names on the search results page should take the user to that entry’s page.
  
 4. [X] New Page: Clicking “New Page” in the sidebar should take the user to a page where they can create a new encyclopedia entry.
        Users should be able to enter a title for the page and, in a textarea, should be able to enter the Markdown content for the page.
        Users should be able to click a button to save their new page.
        When the page is saved, if an encyclopedia entry already exists with the provided title, the user should be presented with an error message.
        Otherwise, the encyclopedia entry should be saved to disk, and the user should be taken to the new entry’s page.
        
 5. [] Edit Page: On each entry page, the user should be able to click a link to be taken to a page where the user can edit that entry’s Markdown content in a textarea.
        The textarea should be pre-populated with the existing Markdown content of the page. (i.e., the existing content should be the initial value of the textarea).
        The user should be able to click a button to save the changes made to the entry.
        Once the entry is saved, the user should be redirected back to that entry’s page.
        
 6. [X] Random Page: Clicking “Random Page” in the sidebar should take user to a random encyclopedia entry.



will do the following now
[] If the query matches the name of an encyclopedia entry, the user should be redirected to that entry’s page.



Here Are some Essential Django Basics that might end up being usefull when I look back at this project: 

1. Django is a python web framework:

Django basisc commands

To create a new django project run: 
```bash
 django-admin startproject mysite
```

```bash
poetry run python manage.py runserver
```
to add an app to this project run: 

```bash
poetry run python manage.py startapp <name_of_app>
```
then you must add the new app name inside the `INSTALLED_APPS` list found in the `settings.py` file found inside the project directory. (also include the urls in the main url file), this allows us to put specific logic inside specific applications                  