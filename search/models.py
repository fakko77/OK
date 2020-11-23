from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True, null=True)
    score = models.CharField(max_length=200, unique=False, null=True)
    img_url = models.URLField()
    url = models.URLField()
    ingredient = models.TextField(null=True)
    category_product = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def categoryName(self):
        return self.category_product.name


class Favorite(models.Model):
    user = models.IntegerField(unique=True, null=True)
    products = models.ManyToManyField(Product, related_name='favorites', blank=True)

    def productName(self):
        return self.products.name

