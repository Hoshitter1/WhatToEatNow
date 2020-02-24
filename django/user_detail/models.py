from django.db import models

from users.models import CustomUser

GENDER_CHOICES = [
    ('1', '女性'),
    ('2', '男性'),
]


class UserDetail(models.Model):
    """https://docs.djangoproject.com/en/dev/ref/models/fields/
    Avoid using null on string-based fields such as CharField and TextField. If a string-based field has null=True,
    that means it has two possible values for “no data”: NULL, and the empty string. In most cases,
    it’s redundant to have two possible values for “no data;” the Django convention is to use the empty string, not NULL
    """
    user = models.ForeignKey(CustomUser, verbose_name='user', on_delete=models.CASCADE)
    # For recommending foods that tend to be preferred by certain gender
    gender = models.CharField('gender', max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    # For recommending foods that tend to be preferred by certain age
    age = models.IntegerField('age', blank=True, null=True)

    # If avg of name length is expected to be around 5, CharField can only hold 255(which means only 51 name)
    like_ingredients = models.TextField(verbose_name='like_ingredients', blank=True)
    ok_ingredients = models.TextField(verbose_name='ok_ingredients', blank=True)
    dislike_ingredients = models.TextField(verbose_name='dislike_ingredients', blank=True)

    # If avg of name length is 10, only less than 50 can be registered recipe since tuple is expected to come in
    like_recipe = models.TextField(verbose_name='like_recipe', blank=True)
    ok_recipe = models.TextField(verbose_name='ok_recipe', blank=True)
    dislike_recipe = models.TextField(verbose_name='dislike_recipe', blank=True)

    def __str__(self):
        """
        For admin to show what' inside of the column
        """
        return self.user.username
