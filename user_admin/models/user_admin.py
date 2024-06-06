from django.db import models
import uuid

class UserAdminModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name= models.CharField(max_length=150)
    email = models.EmailField(unique=True, max_length=150,default=True)
    password = models.CharField(max_length=150, default='default_value_here')
    is_admin= models.BooleanField(default=False)
        
    def __str__(self) -> str:
        return f"Usuário: {self.name}, e-mail: {self.email}"
