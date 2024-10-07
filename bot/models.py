from django.db import models

class Conversation(models.Model):
    user_id = models.CharField(max_length=255)
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id} - {self.message[:50]}"
    
