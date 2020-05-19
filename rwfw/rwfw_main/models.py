from django.db import models

# Create your models here.
class rwfw_item_table(models.Model):
    item_icon = models.ImageField(upload_to='images/')
    item_head = models.CharField(max_length=30, default='Manager')
    item_desc = models.CharField(max_length=200)

    def __str__(self):
        return self.item_head
        
