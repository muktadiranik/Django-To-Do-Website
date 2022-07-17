from django.db import models
from django.contrib.auth.models import User


class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField()
    date_end = models.DateField()

    Completed = "Completed"
    Pending = "Pending"

    status_choices = [
        (Completed, "Completed"),
        (Pending, "Pending")
    ]

    status = models.CharField(choices=status_choices, max_length=10, default=Pending)

    def __str__(self):
        return self.user.username + ", " + self.name + ", " + self.status
