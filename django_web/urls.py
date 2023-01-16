"""django_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from home import views as home
# from polls import views as polls
from user_auth import views as user_auth
# from django.views.generic import TemplateView

# extra_patterns = [
#     path('register', user_auth.test_code),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.get_home),
    # path('chitiet', home.get_chitiet),
    # path('kiemtra', polls.kiemtra),
    # path('polls/', polls.index, name='index'),
    # path('polls/<int:question_id>/', polls.detail),
    # path('polls/<int:question_id>/results/', polls.results),
    # path('polls/<int:question_id>/vote/', polls.vote),
    # path('user-auth/', include(extra_patterns)),
    # path('user-auth/register/', user_auth.register),
    path('polls/', include('polls.urls', namespace='author-polls')),
    path('user-auth/', include('user_auth.urls', namespace='user-auth')),
    path('file-upload/', include('file_uploader.urls', namespace='file-uploader')),
    path('pagination/', include('pagination.urls')),
]
