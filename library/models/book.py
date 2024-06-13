from django.db import models
import uuid

class BookModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    publisher = models.CharField(max_length=150)
    gender = models.CharField(max_length=150)
    pages = models.IntegerField()
    publish_date = models.DateField(null=True)
    checkin_date = models.DateField(auto_now_add=True)
    synopsis = models.TextField(max_length=250)
    is_available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.title}, escrito por {self.author} (Publicado por {self.publisher} em {self.publish_date})"
