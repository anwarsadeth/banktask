from django.contrib import admin

# Register your models here.
from persons.models import Branch, District, Person,Account_type,Gender

admin.site.register(Branch)
admin.site.register(District)
admin.site.register(Person)
admin.site.register(Gender)
admin.site.register(Account_type)

