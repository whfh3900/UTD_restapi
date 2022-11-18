from django.db import models

# Create your models here.
class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=45)
    tran_dt = models.TextField()
    code = models.IntegerField()
    md_type = models.IntegerField()
    wd_code = models.IntegerField()
    net_code = models.IntegerField()
    tran_amt = models.IntegerField(default=0)
    result = models.CharField(max_length=4, null=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.id


class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=45, unique=True)
    c0 = models.IntegerField(default=0)
    c1 = models.IntegerField(default=0)
    c2 = models.IntegerField(default=0)
    c3 = models.IntegerField(default=0)
    c4 = models.IntegerField(default=0)
    c5 = models.IntegerField(default=0)
    c6 = models.IntegerField(default=0)
    c7 = models.IntegerField(default=0)
    c8 = models.IntegerField(default=0)
    c9 = models.IntegerField(default=0)
    c10 = models.IntegerField(default=0)
    c11 = models.IntegerField(default=0)
    c12 = models.IntegerField(default=0)
    c13 = models.IntegerField(default=0)
    c14 = models.IntegerField(default=0)
    c15 = models.IntegerField(default=0)
    c16 = models.IntegerField(default=0)
    c17 = models.IntegerField(default=0)
    c18 = models.IntegerField(default=0)
    c19 = models.IntegerField(default=0)
    c20 = models.IntegerField(default=0)
    c21 = models.IntegerField(default=0)
    c22 = models.IntegerField(default=0)
    c23 = models.IntegerField(default=0)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.id
