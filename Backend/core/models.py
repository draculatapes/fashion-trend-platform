from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Trend(models.Model):
    CATEGORY_CHOICES = [
        ('men', 'Men'),
        ('women', 'Women'),
        ('unisex', 'Unisex'),
    ]

    STATUS_CHOICES = [
        ('emerging', 'Emerging'),
        ('popular', 'Popular'),
        ('declining', 'Declining'),
    ]

    title = models.CharField(max_length=200)
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name='trends'
    )
    category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

