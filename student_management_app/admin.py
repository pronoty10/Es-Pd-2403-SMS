from django.contrib import admin
from .models import Student
# Register your models here.




class StudentAdmin(admin.ModelAdmin):
    list_display = ["prime_id","name", "email", "image","religion","gender"]
    search_fields=["name", "email", "image","religion"]

  



admin.site.register(Student,StudentAdmin)