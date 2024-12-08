from django.contrib import admin
from .models import School, Teacher, Student, BehaviorLog  

# Register your models here
admin.site.register(School)  
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(BehaviorLog)

