from django.shortcuts import render
from django.http import HttpResponse, response
from catalog.models import Author, Book, BookInstance, Genre
from django.views import generic

class BookListView(generic.ListView):
  model = Book
  context_object_name = 'my_book_list' # my own name for the list as a template variable
  queryset = Book.objects.filter(title__icontains='git')[:5] #Get 5 books containing the title 'git'
  template_name = 'books'

def home_page(request):
  return HttpResponse('hello home page..')

def showImage(request):
  return render(request,'showImage.html')

def index(request):
  
  # Generate counts of some of the main objects
  num_books = Book.objects.all().count()
  num_instances = BookInstance.objects.all().count()
  
  # Available books (status = 'a')
  num_instances_available = BookInstance.objects.filter(status__exact='a').count()

  # The 'all()' is implied by default.
  num_authors = Author.objects.count()

  # Challenge yourself
  num_genres = Genre.objects.count()
  num_booktitle_has_git_wording = Book.objects.filter(title__icontains='git').count()

  context = {
    'num_books':num_books,
    'num_instances':num_instances,
    'num_instances_available':num_instances_available,
    'num_authors':num_authors,
    'num_booktitle_has_git_wording':num_booktitle_has_git_wording,
  }

  return render(request,'index.html',context=context)