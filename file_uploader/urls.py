from django.urls import path

from . import views

app_name = 'file_uploader'
urlpatterns = [
    path('', views.fileUploaderView),
]
