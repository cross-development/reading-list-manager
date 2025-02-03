from django.core.validators import MinValueValidator
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __repr__(self) -> str:
        return f"<Author pk={self.pk}, Name={self.first_name} {self.last_name}"


class Book(BaseModel):
    STATUS_CHOICES = [
        ('to_read', "Plan to read"),
        ('reading', "Reading"),
        ('read', 'Read'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    publication_year = models.PositiveIntegerField(validators=[MinValueValidator(1970)])
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='to_read')
    notes = models.TextField(blank=True, null=True)
    rating = models.PositiveIntegerField(blank=True, null=True, choices=[(i, i) for i in range(1, 6)])
    authors = models.ManyToManyField(Author, related_name='books')

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f'<Book pk={self.pk}, title={self.title}>'
