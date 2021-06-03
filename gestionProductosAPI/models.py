
from django.db import models

# Modelo de la tabla Category en MySQL con los atributos id y name
class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    # Modelo no manipulable managed = False
    class Meta:
        managed = False
        db_table = 'category'
    # Retorno de serialize para transformación a JSON
    def serialize(self):
        return{
            "id": self.id,
            "nombre": self.name
        }

# Modelo de la tabla Product en MySQL con los atributos id, name, url_image, price, discount y category
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    url_image = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete= models.DO_NOTHING, db_column='category', blank=True, null=True)
    
    # Modelo no manipulable managed = False
    class Meta:
        managed = False
        db_table = 'product'

    # Retorno de serialize para transformación a JSON
    def serialize(self):
        return{
            "id": self.id,
            "nombre": self.name,
            "img": self.url_image,
            "precio": self.price,
            "desc": self.discount,
            "categoria": self.category.name
        }