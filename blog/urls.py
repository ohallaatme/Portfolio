from django.urls import path
# below dot (.) states from current directory import the views
from . import views

"""

the +static code after the list of paths is so we can re-route the user to our media files

 - document_root=settings.MEDIA_ROOT = where you should look for the information
 - settings.MEDIA_URL = the url path that should be used for the information

"""

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    # code below says look for an int after the /blog and we are going
    # to save it as blog_id
    path('<int:blog_id>/', views.detail, name="detail"),
]
