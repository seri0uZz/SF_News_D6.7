from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Good(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    price = models.PositiveSmallIntegerField(verbose_name='Цена')
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-price']


class Course(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=15)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.name
