from django.contrib import admin
# <HINT> Import any new Models here
#modified in lab 2 step 4
from .models import Course, Lesson, Instructor, Learner, Question, Choice

# <HINT> Register QuestionInline and ChoiceInline classes here
#LAB 2 STEP 4
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 5
#LAB 2 STEP 4    
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 5


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

#LAB 2 STEP 4
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'grade']

#LAB 2 STEP 4
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice_text', 'is_correct']

# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
#LAB 2 STEP 4
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)