from django.db import models

class user(models.Model):

    name = models.TextField()
    user_id = models.AutoField(primary_key=True)
    pw = models.TextField()


class apis(models.Model):

    key = models.TextField()
    api_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey("user", on_delete=models.SET_NULL, null=True)
