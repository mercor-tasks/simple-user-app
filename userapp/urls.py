from django.urls import path

from . import views

urlpatterns = [
    path('get-user', views.UserView.as_view()),
]
