from django.contrib import admin
from .models import Users
from .models import Cash
from .models import Card
from .models import Home,Sneak,Access,Apparel,Supp,Kits,Equip
# Register your models here.
admin.site.register(Users)
admin.site.register(Cash)
admin.site.register(Card)
admin.site.register(Home)
admin.site.register(Sneak)
admin.site.register(Access)
admin.site.register(Apparel)
admin.site.register(Supp)
admin.site.register(Kits)
admin.site.register(Equip)
