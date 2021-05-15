from django.shortcuts import render, redirect
from .models import User, Book
from django.contrib import messages

# Create your views here.
def books(request):
    if not request.session['user_id']:
        return redirect('/')
    context={
        'user':User.objects.get(id=request.session['user_id']),
        'books':Book.objects.all(),
        
    }
    return render(request,'books.html', context)

def create(request):
    if request.method=='POST':
        errors=Book.objects.validator(request.POST)
        print(errors)
        if errors:
            for value in errors.values():
                messages.error(request, value)
            return redirect('/books')
        new_book=Book.objects.create(
            title=request.POST['title'],
            desc=request.POST['desc'],
            added_by=User.objects.get(id=request.session['user_id'])
        )
        User.objects.get(id=request.session['user_id']).books_liked.add(new_book)
    return redirect('/books')

def show(request, book_id):
    context={
        'user': User.objects.get(id=request.session['user_id']),
        'book': Book.objects.get(id=book_id),
        'users': Book.objects.get(id=book_id).users_liked_by.all()
    }
    print(context['users'])
    return render(request,'show.html', context)

def add_fav(request, book_id):

    user=User.objects.get(id=request.session['user_id'])
    book=Book.objects.get(id=book_id)
    book.users_liked_by.add(user)
    return redirect('/books')

def remove(request, book_id):

    user=User.objects.get(id=request.session['user_id'])
    book=Book.objects.get(id=book_id)
    book.users_liked_by.remove(user)
    return redirect('/books')

def delete(request, book_id):
    book=Book.objects.get(id=book_id)
    book.delete()
    return redirect('/books')

def edit(request, book_id):
    if request.method=='POST':
        book=Book.objects.get(id=book_id)
        book.title=request.POST['title']
        book.desc=request.POST['desc']
        book.save()
    return redirect('/books')