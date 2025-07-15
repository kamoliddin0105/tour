from django.db import models


class Tour(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    duration = models.PositiveIntegerField(help_text='How long should the tour be played')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tours'