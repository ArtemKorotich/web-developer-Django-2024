from django.db import models
from tasks.models import Project, Task


class BugReport(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    STATUS_CHOICES = [
        ('New', 'Новая'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершена'),
    ]
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New',
    )
    priority = models.IntegerField((1, 2, 3, 4, 5))
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class FeatureRequest(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    STATUS_CHOICES = [('Consideration', "Рассмотрение"),
                      ('Accepted', "Принято"),
                      ('Rejected', "Отклонено")]
    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        default="Рассмотрение"
    )
    priority = models.IntegerField((1, 2, 3, 4, 5))
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)