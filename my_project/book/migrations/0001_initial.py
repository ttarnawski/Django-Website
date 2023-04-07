# Generated by Django 4.1 on 2023-04-06 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=25)),
                ("last_name", models.CharField(max_length=25)),
                ("country", models.CharField(max_length=25)),
                ("birth", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("description", models.TextField(max_length=200)),
                (
                    "isbn",
                    models.CharField(max_length=13, unique=True, verbose_name="ISBN"),
                ),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="book.author",
                    ),
                ),
            ],
            options={"ordering": ["name"],},
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("genre", models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name="Language",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("language", models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name="BookInstance",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("due_back", models.DateField(blank=True, null=True)),
                (
                    "availability",
                    models.CharField(
                        choices=[("Y", "Yes"), ("N", "No")], default="Y", max_length=2
                    ),
                ),
                (
                    "book",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="book.book",
                    ),
                ),
                (
                    "borrower",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="borrowed_books",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "giver",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="given_books",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="book",
            name="genre",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="book.genre"
            ),
        ),
        migrations.AddField(
            model_name="book",
            name="language",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="book.language",
            ),
        ),
    ]
