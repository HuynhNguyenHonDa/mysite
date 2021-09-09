from django.contrib import admin
from firstapp.models import Tenmien,AuthUser,Donvi,QLTB

# Register your models here.
class TenmienAmin(admin.ModelAdmin):
    list_display = ('Thoigian', 'Ip_nguon', 'Ip_dich', 'MAC_TB', 'MAC_dich', 'DNS_string', 'Dactinh', )
    list_filter = ['Thoigian']
admin.site.register(Tenmien, TenmienAmin)

class AuthUserAmin(admin.ModelAdmin):
    list_display = ('password', 'last_login', 'is_superuser', 'username', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 'first_name', 'images', 'TenDonVi', )
    list_filter = ['username']
admin.site.register(AuthUser, AuthUserAmin)

class DonviAmin(admin.ModelAdmin):
    list_display = ('MaDonvi', 'TenDonVi', )
    list_filter = ['TenDonVi']
admin.site.register(Donvi, DonviAmin)

class QLTBAmin(admin.ModelAdmin):
    list_display = ('MAC_TB', 'Ten_TB', 'Ten_Nguoidung', 'MaDonvi', )
    list_filter = ['Ten_TB']
admin.site.register(QLTB, QLTBAmin)