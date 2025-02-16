from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('portfolio/',views.portfolio,name='portfolio'),  # add a new path for portfolio page  # 'portfolio' is the name of the URL pattern, 'views.portfolio' is the corresponding view function.   # 'name' is a unique identifier for this URL pattern, it's used in templates and URL reverse function.   # 'path' is a function provided by Django's URLconf module that takes a URL pattern and a corresponding view function, and returns a URL
   path('about/',views.about,name='about'),
   path('resume/',views.resume,name='resume'),
   path('contact/',views.contact,name='contact'),
   path('skills/',views.skills,name='skills'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)