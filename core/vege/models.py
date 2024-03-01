from django.db import models

# Create your models here.
class Recipe(models.Model):
    #id = models.UUIDField(primary_key=True)
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to="recipe", null=True)
