from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.


class Tags(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

class Blogs(models.Model):
    title = models.CharField(max_length=50)
    body = CKEditor5Field('Text', config_name='extends', blank=True)
    slug = models.SlugField(unique=True, blank=True,null=True)
    time_read = models.IntegerField()
    tags = models.ManyToManyField(Tags)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blogs, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"



