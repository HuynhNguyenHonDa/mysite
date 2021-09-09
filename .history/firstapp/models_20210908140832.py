from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Donvi(models.Model):
    MaDonvi = models.CharField(max_length=30)
    TenDonVi = models.CharField(max_length=250)
    def __str__(self):
        return self.TenDonVi


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField(unique=True, blank=True, null=True, default=None)
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)
    images = models.ImageField(upload_to='firstapp/images')
    TenDonVi = models.ForeignKey(Donvi, on_delete=models.CASCADE)


class QLTB(models.Model):
    MAC_TB = models.CharField(max_length=20)
    Ten_TB = models.CharField(max_length=50)
    Ten_Nguoidung = models.CharField(max_length=50)
    MaDonvi = models.ForeignKey(Donvi, on_delete=models.CASCADE)
    def __str__(self):
        return self.Ten_TB
 

class Tenmien(models.Model):
    Thoigian = models.DateTimeField()
    Ip_nguon = models.CharField(max_length=20)
    Ip_dich = models.CharField(max_length=20)
    MAC_TB = models.ForeignKey(QLTB, on_delete=CASCADE)
    MAC_dich = models.CharField(max_length=25)
    DNS_string = models.CharField(max_length=50)
    Dactinh = models.CharField(max_length=50)
   
      
     