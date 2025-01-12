from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    
    STATUS_CHOICES = [
    ("todo", "To Do"),
    ("inprogress", "In progress"),
    ("done", "Done"),
    ]

    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
        ("critical", "Critical"),
    ]

    title = models.CharField(max_length=70)
    description = models.TextField()
    status = models.CharField(max_length=150, choices=STATUS_CHOICES, default="todo")
    priority = models.CharField(max_length=150, choices=PRIORITY_CHOICES, default="medium")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    due_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author+"\n"+self.content
    