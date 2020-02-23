from django.db import models


class FoodOptions(models.Model):
    food = models.CharField(max_length=30)

    def __str__(self):
        """
        For admin to show what' inside of the column
        """
        return self.food
