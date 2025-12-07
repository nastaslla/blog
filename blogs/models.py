from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_added"]

    def __str__(self):
        return self.title

