from django.contrib import admin
from .models import Author,Genre,Language,Book,BookInstance

# Django範本管理介面
# Register your models here.
# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)


class BookInline(admin.TabularInline):
  model = Book
# 寫法1-自訂管理介面
class AuthorAdmin(admin.ModelAdmin):
  list_display = ('last_name','first_name','date_of_birth','date_of_death')
  # fields = ['first_name','last_name',('date_of_birth','date_of_death')]
  exclude = ['first_name']
  inlines = [BookInline]

admin.site.register(Author,AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
  model = BookInstance

# 寫法2
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  list_display = ('title','author','display_genre','language')
  inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
  list_display = ('id','book','due_back','status','display_status')
  list_filter = ('status','due_back')
  fieldsets = (
    (None , {
      'fields':('book','imprint','id')
    }),
    ('Availability',{
      'fields':('status','due_back')
    }),
  )