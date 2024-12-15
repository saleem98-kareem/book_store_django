from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import *
from django.contrib.auth.forms import UserCreationForm

#from .forms import BooksForm




def home(request) :

 book=Books.objects.all()

 return render(request , 'book/index.html',{'book':book})



#def create(request) :

    #form = BooksForm()
  #  if request.method == 'POST' :
      #  form = BooksForm(request.POST)
      # if form.is_valid() :
        #  form.save()
         # return redirect('/')
 
    #context = {'form',form}

 ## return render(request , 'create.html', context)


def create(request) :
   
 author = Books.objects.all()
 return render(request , 'book/create.html',{'author':author})

def add(request) :
  
  title_book = request.POST.get('namebook')
  author_book = request.POST.get('name_authr')
  price_book= request.POST.get('price')
  Publisher_book = request.POST.get('published_date')
  stack_book= request.POST.get('stack')
   
  book = Books(title = title_book , price = price_book ,name_authr = author_book , stock_quantity = stack_book, published_date = Publisher_book)
  book.save()
  return redirect('dashpord')



def update_form(request ,id ) :
 
 update_book= Books.objects.get(id=id)
 return render(request , 'book/update_book.html',{'update_book':update_book})



def update_data(request ,id) :
 
 update_book= Books.objects.get(id=id)
 
 title_book = request.POST.get('namebook')
 author_book = request.POST.get('name_authr')
 price_book= request.POST.get('price')
 Publisher_book = request.POST.get('published_date')
 stack_book= request.POST.get('stack')

 update_book.title = title_book
 update_book.name_authr = author_book
 update_book.price = price_book
 update_book.published_date = Publisher_book
 update_book.stock_quantity = stack_book

 update_book.save()

 return redirect('dashpord')


def delet_data(request , id ) :
 
 delet_book= Books.objects.get(id=id)

 delet_book.delete()

 return redirect('/')


def info_book(request , id) :
 
 info_data=Books.objects.get(id=id)
 return render(request , 'book\info.html' , {'info_data' : info_data})



def dashprd_bok_stor(request) :
 
 book=Books.objects.all()
 author=Author.objects.all()
 publisher=Publisher.objects.all()
 context = {'book' : book , 'author' : author , 'publisher' : publisher}

 return render(request , 'book\dashpord.html',context )


##def signup(request):
 #if request.method == "POST" :
 #  form = UserCreationForm(request.POST or None)
 #  if form.is_valid() :
 #   form.save()
 #   return redirect('registrations\login')
 #  else :
  #  form = UserCreationForm()
  # return render(request , 'registrations\login' , {'form' : form}) 
    







    
     

  



