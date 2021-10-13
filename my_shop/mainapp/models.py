from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='Имя',
        unique=True,
    )

    description = models.TextField(
        verbose_name='описание',
        blank=True,

    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name

class Product(models.Model):
    objects = None
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE
    )

    name = models.CharField(
        verbose_name='имя продукта',
        max_length=128,
    )

    image = models.ImageField(
        upload_to='product_image',
        blank=True
    )

    shot_desc = models.CharField(
        verbose_name='краткое описание',
        max_length=60,
        blank=True
    )

    description = models.TextField(
        verbose_name='описание продукта',
        blank=True
    )

    price = models.DecimalField(
        verbose_name='цена',
        max_digits=8,
        decimal_places=2
    )

    quantity = models.PositiveIntegerField(
        verbose_name='количество на складе',
        default=0
    )

    def __str__(self):
        return f'{self.name} ({self.category.name})'
