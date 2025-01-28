from django.core.validators import MinValueValidator
from django.db import models


class Book(models.Model):
    STATUS_CHOICES = [
        ('to_read', "Plan to read"),
        ('reading', "Reading"),
        ('read', 'Read'),
    ]

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    publication_year = models.PositiveIntegerField(validators=[MinValueValidator(1970)])
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='to_read')
    notes = models.TextField(blank=True, null=True)
    rating = models.PositiveIntegerField(blank=True, null=True, choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f'<Book pk={self.pk}, title={self.title}>'
