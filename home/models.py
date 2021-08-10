from django.db import models

# Create your models here.

class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)


class news(models.Model):
    image=models.ImageField(upload_to='pics')
    date=models.DateField()
    title=models.TextField()
    category=models.TextField()
    content=models.TextField()