from django.db import models

class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    created_datatime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        verbose_name = "post"
    
    def __str__(self):
        return self.title
