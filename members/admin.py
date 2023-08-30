from django.contrib import admin
from .models import Question_f,Question_g

class Question_football(admin.ModelAdmin):
  list_display = ("question", "correct_answer",)
admin.site.register(Question_f,Question_football)
class Question_general(admin.ModelAdmin):
  list_display = ("question", "correct_answer",)
admin.site.register(Question_g,Question_general)

