from django.urls import path
from . import views

# 進入 <catalog/> 後 , 依 <catalog.urls> 作URL對應
urlpatterns = [
  path('',views.index , name='index'),
  path('note',views.showImage , name='note'),
  path('books/',views.BookListView.as_view(),name = 'books'),
]