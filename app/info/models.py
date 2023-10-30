from django.db import models
from django.utils.text import slugify

# Create your models here.


class Position(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
      return f"{self.name}"
    


class Employees(models.Model):
    name = models.CharField(max_length=50)
    position = models.ForeignKey(Position, on_delete=models.CASCADE,)
    office = models.CharField(max_length=50)
    age = models.IntegerField()
    startdate = models.DateField()
    salary = models.IntegerField()
    slug = models.SlugField(max_length=50, unique=True, blank=True, editable=False,)
    
    def __str__(self):
      return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)



