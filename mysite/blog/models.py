from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.


class Post (models.Model):

    COLOR_CHOICES = (
        ('#00A056', 'Verde bosque'),
        ('#FFA1A1', 'Rosa'),
        ('#9CD484', 'Verde manzana'),
        ('#FDAE00', 'Amarillo'),
        ('#68735D', 'Musgo'),
    )

    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="images/", blank=True)
    body = RichTextField(blank=True, null=True)
    background_color = models.CharField(
        max_length=30, choices=COLOR_CHOICES, default='Verde bosque')
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, blank=True, unique_for_date='created')

    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.created.year,
                             self.created.month,
                             self.created.day, self.slug])

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
    
    
