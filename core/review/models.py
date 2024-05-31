from django.db import models


class ProductReview(models.Model):
    product_id = models.CharField(max_length=100)
    reviewer = models.CharField(max_length=100)
    details = models.CharField(max_length=100)

    def __str__(self):
        return self.product_id

