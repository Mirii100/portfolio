
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('portfolio/',views.portfolio,name='portfolio'),  # add a new path for portfolio page  # 'portfolio' is the name of the URL pattern, 'views.portfolio' is the corresponding view function.   # 'name' is a unique identifier for this URL pattern, it's used in templates and URL reverse function.   # 'path' is a function provided by Django's URLconf module that takes a URL pattern and a corresponding view function, and returns a URL
   
]