from django.db import models

class Category(models.Model):          # Category model for Many-to-One relationship with Product
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Tag(models.Model):               # TAG Model 2 many to many with Product
    name = models.CharField(max_length=50, unique=True)


    def __str__(self):
        return self.name


class Product(models.Model):           # Product model with Many-to-One relationship to Category and Many-to-Many relationship to Tag
    category    = models.ForeignKey(Category, on_delete=models.CASCADE,
                                    related_name='products')   # MANY-TO-ONE
    tags        = models.ManyToManyField(Tag, blank=True)       # MANY-TO-MANY
    name        = models.CharField(max_length=200)  
    slug        = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    stock       = models.PositiveIntegerField(default=0)
    image       = models.ImageField(upload_to='products/', blank=True)
    available   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
