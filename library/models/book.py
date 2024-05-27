from django.db import models
import uuid

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    publisher = models.CharField(max_length=150)
    gender = models.CharField(max_length=150)
    publish_date = models.DateField(null=True)
    checkin_date = models.DateField(auto_now_add=True)
    is_avaiable = models.BooleanField()

    def __str__(self) -> str:
        status = "Disponível" if self.is_avaiable else "Reservado"
        return f"{self.title} escrito por {self.author} (Publicado por {self.publisher} em {self.publish_date}) - {status.upper()}"
