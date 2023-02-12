from django.db import models

# Create your models here.
class users(models.Model):
    # added manually
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    # given in database
    account_id = models.IntegerField()
    reputation = models.IntegerField(null=False)
    views = models.IntegerField()
    down_votes = models.IntegerField()
    up_votes = models.IntegerField()
    display_name = models.CharField(max_length=255,null=False)
    location = models.CharField(max_length=512)
    profile_image_url = models.CharField(max_length=255)
    website_url = models.CharField(max_length=255)
    about_me = models.TextField()
    creation_date = models.DateTimeField(null=False)
    last_access_date = models.DateTimeField(null= False)


    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.Name
