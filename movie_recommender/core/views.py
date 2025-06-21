from django.shortcuts import render
from core.models import Movie
from core.recommendation.utils import load_similarity_matrix, recommend
import os
from django.conf import settings

pkl_path = os.path.join(settings.BASE_DIR, 'core', 'recommendation', 'item_similarity.pkl')
similarity_df = load_similarity_matrix(pkl_path)

def recommend_movie_view(request):
    movies = Movie.objects.all().order_by("title")
    movie_title = ""
    recommendations = []

    if request.method == "POST":
        movie_title = request.POST.get("movie_title")
        recommendations = recommend(movie_title, similarity_df)

    return render(request, "recommend.html", {
        "movies": movies,
        "movie_title": movie_title,
        "recommendations": recommendations,
    })
