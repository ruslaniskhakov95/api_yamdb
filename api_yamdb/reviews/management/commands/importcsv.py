import csv

from django.core.management.base import BaseCommand

from reviews.models import (
    Category,
    Comment,
    Genre,
    GenreTitle,
    Review,
    Title,
    User,
)


class Command(BaseCommand):
    def handle_users(self, *args, **kwargs):
        with open('static/data/users.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            objs = [
                User(
                    id=row['id'],
                    username=row['username'],
                    email=row['email'],
                    role=row['role'],
                    bio=row['bio'],
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                )
                for row in reader
            ]
            User.objects.bulk_create(objs)

    def handle_category(self, *args, **kwargs):
        with open(
            'static/data/category.csv', 'r', encoding='utf-8'
        ) as csvfile:
            reader = csv.DictReader(csvfile)
            objs = [
                Category(
                    id=row['id'],
                    name=row['name'],
                    slug=row['slug'],
                )
                for row in reader
            ]
            Category.objects.bulk_create(objs)

    def handle_genre(self, *args, **kwargs):
        with open('static/data/genre.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            objs = [
                Genre(
                    id=row['id'],
                    name=row['name'],
                    slug=row['slug'],
                )
                for row in reader
            ]
            Genre.objects.bulk_create(objs)

    def handle_titles(self, *args, **kwargs):
        with open('static/data/titles.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            objs = [
                Title(
                    id=row['id'],
                    name=row['name'],
                    year=row['year'],
                    category_id=row['category'],
                )
                for row in reader
            ]
            Title.objects.bulk_create(objs)

    def handle_genre_title(self, *args, **kwargs):
        with open(
            'static/data/genre_title.csv', 'r', encoding='utf-8'
        ) as csvfile:
            reader = csv.DictReader(csvfile)
            objs = [
                GenreTitle(
                    id=row['id'],
                    genre_id=row['genre_id'],
                    title_id=row['title_id'],
                )
                for row in reader
            ]
            GenreTitle.objects.bulk_create(objs)

    def handle_review(self, *args, **kwargs):
        with open('static/data/review.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            objs = [
                Review(
                    id=row['id'],
                    text=row['text'],
                    score=row['score'],
                    pub_date=row['pub_date'],
                    author_id=row['author'],
                    title_id=row['title_id'],
                )
                for row in reader
            ]
            Review.objects.bulk_create(objs)

    def handle_comments(self, *args, **kwargs):
        with open(
            'static/data/comments.csv', 'r', encoding='utf-8'
        ) as csvfile:
            reader = csv.DictReader(csvfile)
            objs = [
                Comment(
                    id=row['id'],
                    review_id=row['review_id'],
                    text=row['text'],
                    author_id=row['author'],
                    pub_date=row['pub_date'],
                )
                for row in reader
            ]
            Comment.objects.bulk_create(objs)

    def main(self, *args, **kwargs):
        self.handle_users()
        self.handle_category()
        self.handle_genre()
        self.handle_titles()
        self.handle_genre_title()
        self.handle_review()
        self.handle_comments()
