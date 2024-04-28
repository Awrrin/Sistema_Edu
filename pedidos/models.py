from django.db import models


# Create your models here.
# class Category(models.Model):
# name = models.CharField(max_length=100, null=False, blank=False)

# class Product(models.Model):
# product = models.CharField(max_length=400, null=False, blank=False)
# descrition = models.CharField(max_length=200, null=False, blank=False)
# category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Pedidos(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(null=True)
    obser = models.CharField(max_length=300, null=True)
    finished_at = models.DateTimeField(null=True)

    # Outros campos do modelo...
