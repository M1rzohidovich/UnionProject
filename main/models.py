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


class MainNews(models.Model):
    title = models.CharField(max_length=170)
    img1 = models.ImageField(upload_to=slugify_upload)
    img2 = models.ImageField(upload_to=slugify_upload, blank=True)
    img3 = models.ImageField(upload_to=slugify_upload, blank=True)
    description = models.TextField()
    video = models.FileField(upload_to=slugify_upload, null=True, blank=True)
    upload_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "MainNews"
        verbose_name_plural = "Yangiliklar"

    def __str__(self):
        return self.title


class Announcements(models.Model):
    title = models.CharField(max_length=170)
    image = models.ImageField(upload_to=slugify_upload)
    image2 = models.ImageField(upload_to=slugify_upload, blank=True)
    description = models.TextField()
    video = models.FileField(upload_to=slugify_upload, blank=True, null=True)
    upload_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Announcements"
        verbose_name_plural ="E'lonlar"

    def __str__(self):
        return self.title


class Articles(models.Model):
    title = models.CharField(max_length=170)
    description = models.TextField()
    image = models.ImageField(upload_to=slugify_upload, blank=True)
    after = models.CharField(max_length=170)
    file = models.FileField(blank=True, null=True)
    upload_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Articles"
        verbose_name_plural = "Maqola va She'rlar"

    def __str__(self):
        return self.title


class OwnersOfGreatHearts(models.Model):
    title = models.CharField(max_length=170)
    image1 = models.ImageField(upload_to=slugify_upload)
    image2 = models.ImageField(upload_to=slugify_upload, blank=True)
    image3 = models.ImageField(upload_to=slugify_upload, blank=True)
    description = models.TextField()
    video = models.FileField(null=True, blank=True)
    upload_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "OwnersOfGreatHearts"
        verbose_name_plural = "Muvafaqqiyat Hikoyasi"

    def __str__(self):
        return self.title


class Privileges(models.Model):
    title = models.CharField(max_length=170)
    image = models.ImageField(upload_to=slugify_upload, blank=True)
    description = models.TextField()
    upload_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Privileges"
        verbose_name_plural = "Imtiyozlar"

    def __str__(self):
        return self.title


class YoungReception(models.Model):
    title = models.CharField(max_length=170)
    image = models.ImageField(upload_to=slugify_upload)
    image1 = models.ImageField(upload_to=slugify_upload, blank=True)
    image2 = models.ImageField(upload_to=slugify_upload, blank=True)
    description = models.TextField()
    video = models.FileField(upload_to=slugify_upload, blank=True)
    upload_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "YoungReception"
        verbose_name_plural = "Yoshlar qabulxonasi"

    def __str__(self):
        return self.title





