from django.db import models

# Create your models here.


class Post (models.Model):

    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="images/")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    # def get_absolute_url(self):
    #     return reverse('blog:post_detail',
    #                    args=[self.publish.year,
    #                          self.publish.month,
    #                          self.publish.day, self.slug])

    def __str__(self):
        return self.title
