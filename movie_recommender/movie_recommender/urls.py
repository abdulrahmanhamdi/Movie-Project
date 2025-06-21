# movie_recommender/urls.py

from django.contrib import admin
from django.urls import path
from core.views import recommend_movie_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', recommend_movie_view, name='home'),
]
