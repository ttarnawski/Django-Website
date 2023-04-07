from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50, unique=True)
    author = models.CharField(max_length=35, null=True)
    GENRE_CHOICES = (
        ('FA', 'Fantasy'),
        ('AD', 'Adventure'),
        ('RO', 'Romance'),
        ('CO', 'Contemporary'),
        ('DY', 'Dystopian'),
        ('MY', 'Mystery'),
        ('HO', 'Horror'),
        ('TH', 'Thriller'),
        ('PA', 'Paranormal'),
        ('HF', 'Historical Fiction'),
        ('SF', 'Science Fiction'),
        ('CH', "Children's"),
        ('OT', 'Other'),
    )
    genre = models.CharField(max_length=25, choices=GENRE_CHOICES, null=True)
    language = models.CharField(max_length=25, null=True)
    description = models.TextField(max_length=200)
    isbn = models.PositiveBigIntegerField(max_length=13, unique=True, validators=[MaxValueValidator(9999999999999)])

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return f'{self.name} by {self.author}\n'


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    giver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='given_books')
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='borrowed_books')
    AVAILABILITY_CHOICES = (
         ('Y', 'Yes'),
         ('N', 'No')
    )
    availability = models.CharField(max_length=3, choices=AVAILABILITY_CHOICES, default='Y')
    borrow_the_book = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        current_user = kwargs.pop('current_user', None) or User.objects.first()
        is_already_created = not self.pk
        if is_already_created:
            self.giver = current_user
        else:
            self.borrower = current_user

        if self.borrow_the_book:
            self.availability = 'N'
        else:
            self.availability = 'Y'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.book}'
