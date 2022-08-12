from django.db import models


class TodoItem(models.Model):
    description = models.CharField(max_length=62)
    is_completed = models.BooleanField("выполнено", default=False)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description.lower()

    class Meta:
        ordering = ('-created',)


