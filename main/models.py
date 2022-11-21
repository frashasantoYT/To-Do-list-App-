from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=250) 
    complete = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    
 
    
    
    def __str__(self) -> str:
        return self.title 
    
    class Meta:
        order_with_respect_to = 'complete'
    
    