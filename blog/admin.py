from django.contrib import admin

from blog.models import Article, Reviews, Users_type, Users, Tur, Client

admin.site.register(Article)
admin.site.register(Reviews)
admin.site.register(Users)
admin.site.register(Users_type)
admin.site.register(Tur)
admin.site.register(Client)