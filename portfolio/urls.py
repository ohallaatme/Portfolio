"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# adding 'include' to import to route user to blog pages
from django.urls import path, include
# this line of code is essentially importing our settings.py file from our portfolio directory
from django.conf import settings
# static is an app included in our settings.py apps that allows us to serve images, files, videos
# Django includes it by default in our INSTALLED_APPS
from django.conf.urls.static import static
# import views from jobs generally so we can specify which view for multiple views
import jobs.views

"""

the +static code after the list of paths is so we can re-route the user to our media files

 - document_root=settings.MEDIA_ROOT = where you should look for the information
 - settings.MEDIA_URL = the url path that should be used for the information

"""

urlpatterns = [
    path('admin/', admin.site.urls),
    # homepage, putting homepage view inside of Job app in project
    # jobs already has a views.py we can write a function to return with
    path('', jobs.views.home, name='home'),
    # path to send along to blog app
    path('blog/', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
