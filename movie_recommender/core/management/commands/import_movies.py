from django.core.management.base import BaseCommand
from core.models import Movie
import pickle
import os

class Command(BaseCommand):
    help = 'Import movie titles from similarity matrix'

    def handle(self, *args, **kwargs):
        path = os.path.join('core', 'recommendation', 'item_similarity.pkl')
        with open(path, 'rb') as f:
            similarity_df = pickle.load(f)

        movie_titles = list(similarity_df.columns)

        count = 0
        for title in movie_titles:
            if not Movie.objects.filter(title=title).exists():
                Movie.objects.create(title=title)
                count += 1

        self.stdout.write(self.style.SUCCESS(f"{count} movies imported successfully."))
