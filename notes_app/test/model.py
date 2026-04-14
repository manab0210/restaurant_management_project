from django.db import models
class Restaurant(models.Model):
    name=models.CharField(max_length=200)
    address=models.TextField()
    operating_days=models.CharField(
        max_length=100,
        default="Mon, Tue, Wed, Thu, Fri",
        help_text="Enter days separated by commas (e.g., Mon, Tue, Wed)"
    )
    def __str__(self):
        return self.name