from django.db import models

class Recommendation(models.Model):
    CATEGORY_CHOICES = [
        ('film', 'Film'),
        ('music', 'Müzik'),
        ('series', 'Dizi'),
        ('anime', 'Anime'),
        ('documentary', 'Belgesel'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField()
    source_url = models.URLField()

    def __str__(self):
        return f"{self.category} - {self.title}"
