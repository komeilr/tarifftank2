from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import BooleanField, CharField, TextField


class User(AbstractUser):
    
    def __str__(self):
        return f"<USER {self.first_name}>"
    
class TestTable(models.Model):
    one = CharField(max_length=100)
    two = CharField(max_length=200)
    

class CA2021(models.Model):
    
    tariff = CharField(max_length=20)
    eff_date = CharField(max_length=40)
    change =  CharField(max_length=20)
    sub_chap = TextField(blank=True, null=True)
    desc1 = TextField(blank=True, null=True)
    desc2 = TextField(blank=True, null=True)
    desc3 = TextField(blank=True, null=True)
    footnote = CharField(max_length=10, blank=True, null=True)
    uom = CharField(max_length=3, blank=True, null=True)
    mfn = CharField(max_length=128, blank=True, null=True)
    gt = CharField(max_length=128, blank=True, null=True)
    aut = CharField(max_length=128, blank=True, null=True)
    nzt = CharField(max_length=128, blank=True, null=True)
    ccct = CharField(max_length=128, blank=True, null=True)
    ldct = CharField(max_length=128, blank=True, null=True)
    gpt = CharField(max_length=128, blank=True, null=True)
    ust = CharField(max_length=128, blank=True, null=True)
    mxt = CharField(max_length=128, blank=True, null=True)
    ciat = CharField(max_length=128, blank=True, null=True)
    ct = CharField(max_length=128, blank=True, null=True)
    ciat = CharField(max_length=128, blank=True, null=True)
    crt = CharField(max_length=128, blank=True, null=True)
    it = CharField(max_length=128, blank=True, null=True)
    nt = CharField(max_length=128, blank=True, null=True)
    slt = CharField(max_length=128, blank=True, null=True)
    pt = CharField(max_length=128, blank=True, null=True)
    colt = CharField(max_length=128, blank=True, null=True)
    jt = CharField(max_length=128, blank=True, null=True)
    pat = CharField(max_length=128, blank=True, null=True)
    hnt = CharField(max_length=128, blank=True, null=True)
    krt = CharField(max_length=128, blank=True, null=True)
    ceut = CharField(max_length=128, blank=True, null=True)
    uat = CharField(max_length=128, blank=True, null=True)
    cptpt = CharField(max_length=128, blank=True, null=True)
    ukt = CharField(max_length=128, blank=True, null=True)
    
    def __str__(self):
        return f"<CA2021 {self.tariff}>"
    
    
class CA2022(models.Model):
    
    tariff = CharField(max_length=20)
    eff_date = CharField(max_length=40)
    change =  CharField(max_length=20)
    sub_chap = TextField(blank=True, null=True)
    desc1 = TextField(blank=True, null=True)
    desc2 = TextField(blank=True, null=True)
    desc3 = TextField(blank=True, null=True)
    footnote = CharField(max_length=10, blank=True, null=True)
    uom = CharField(max_length=3, blank=True, null=True)
    mfn = CharField(max_length=128, blank=True, null=True)    
    aut = CharField(max_length=128, blank=True, null=True)
    nzt = CharField(max_length=128, blank=True, null=True)
    ccct = CharField(max_length=128, blank=True, null=True)
    ldct = CharField(max_length=128, blank=True, null=True)
    gpt = CharField(max_length=128, blank=True, null=True)
    ust = CharField(max_length=128, blank=True, null=True)
    mxt = CharField(max_length=128, blank=True, null=True)
    ciat = CharField(max_length=128, blank=True, null=True)
    ct = CharField(max_length=128, blank=True, null=True)
    ciat = CharField(max_length=128, blank=True, null=True)
    crt = CharField(max_length=128, blank=True, null=True)
    it = CharField(max_length=128, blank=True, null=True)
    nt = CharField(max_length=128, blank=True, null=True)
    slt = CharField(max_length=128, blank=True, null=True)
    pt = CharField(max_length=128, blank=True, null=True)
    colt = CharField(max_length=128, blank=True, null=True)
    jt = CharField(max_length=128, blank=True, null=True)
    pat = CharField(max_length=128, blank=True, null=True)
    hnt = CharField(max_length=128, blank=True, null=True)
    krt = CharField(max_length=128, blank=True, null=True)
    ceut = CharField(max_length=128, blank=True, null=True)
    uat = CharField(max_length=128, blank=True, null=True)
    cptpt = CharField(max_length=128, blank=True, null=True)
    ukt = CharField(max_length=128, blank=True, null=True)
    
    def __str__(self):
        return f"<CA2022 {self.tariff}>"

