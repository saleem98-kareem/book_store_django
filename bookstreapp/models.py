from django.db import models





class Books(models.Model):
    title  = models.CharField(max_length=70)
  ##  author = models.ForeignKey(Author, related_name='auther', on_delete=models.CASCADE)
    name_authr= models.CharField(max_length=40, null=True)
    published_date = models.DateField(blank=True, null=True)
    price = models.DecimalField( max_digits=5, decimal_places=2)
    stock_quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    



class Author(models.Model):
    name = models.CharField(max_length=40, null=True)
    biography = models.TextField(null=True)
    book = models.ForeignKey(Books, related_name='auther', on_delete=models.CASCADE)
    


    def __str__(self):
        return self.name




    
class Publisher(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


      
