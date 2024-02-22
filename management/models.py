from django.db import models
from os.path import splitext

from django.utils.text import slugify


def slugify_upload(instance, filename):
    folder = instance._meta.model.__name__
    name, ext = splitext(filename)
    try:
        name_t = slugify(name)
        if name_t is None:
            name_t = name
        path = folder + "/" + name_t + ext
    except:
        path = folder + "/deflaut" + ext

    return path


class Directors(models.Model):
    fullname = models.CharField(max_length=180)
    position = models.CharField(max_length=300)
    image = models.ImageField(upload_to=slugify_upload)
    phone_number = models.CharField(max_length=18, blank=True)
    admission_days = models.CharField(max_length=180, blank=True, null=True)
    email = models.EmailField()

    class Meta:
        verbose_name = "Directors"
        verbose_name_plural = "Rahbariyat"

    def __str__(self):
        return self.fullname


class Employees(models.Model):
    fullname = models.CharField(max_length=180)
    position = models.CharField(max_length=300)
    image = models.ImageField(upload_to=slugify_upload)
    phone_number = models.CharField(max_length=18, blank=True)
    admission_days = models.CharField(max_length=180, blank=True, null=True)
    email = models.EmailField(blank=True)

    class Meta:
        verbose_name = "Employees"
        verbose_name_plural = "Viloyat kengashi"

    def __str__(self):
        return self.fullname


class OTMLeaders(models.Model):
    fullname = models.CharField(max_length=180)
    position = models.CharField(max_length=300)
    image = models.ImageField(upload_to=slugify_upload)
    phone_number = models.CharField(max_length=18, blank=True)
    admission_days = models.CharField(max_length=180, blank=True, null=True)
    email = models.EmailField(blank=True)

    class Meta:
        verbose_name = "OTMLeaders"
        verbose_name_plural = "OTM yetakchilari"

    def __str__(self):
        return self.fullname


class PELeaders(models.Model):
    fullname = models.CharField(max_length=180)
    position = models.CharField(max_length=300)
    image = models.ImageField(upload_to=slugify_upload)
    phone_number = models.CharField(max_length=18, blank=True)
    admission_days = models.CharField(max_length=180, blank=True, null=True)
    email = models.EmailField(blank=True)

    class Meta:
        verbose_name = "PELeaders"
        verbose_name_plural = "Professional talim yetakchilari"

    def __str__(self):
        return self.fullname


class EOLeaders(models.Model):
    fullname = models.CharField(max_length=180)
    position = models.CharField(max_length=300)
    image = models.ImageField(upload_to=slugify_upload)
    phone_number = models.CharField(max_length=18, blank=True)
    admission_days = models.CharField(max_length=180, blank=True, null=True)
    email = models.EmailField(blank=True)

    class Meta:
        verbose_name = "EOLeaders"
        verbose_name_plural = "Korxona Tashkilot Yetakchilari"

    def __str__(self):
        return self.fullname











