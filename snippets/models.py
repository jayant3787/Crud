from django.db import models

class Snippet(models.Model):
    name = models.CharField(max_length=100)
    stream = models.TextField()
    login_time = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name
    
    def body_preview(self):
        return self.stream[:50]
    
    def test(self):
        return "test"

    
