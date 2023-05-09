from django.db import models

# Create your models here.

class Librarian(models.Model):
    username = models.CharField(max_length=100,primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Member(models.Model):
    username = models.CharField(max_length=100,primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    registration_time = models.DateTimeField('Created Time', auto_now_add=True, null=True)

class Book(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='book_covers')
    pdf_file = models.FileField(upload_to='pdf_files')

    borrower = models.ForeignKey(Member, on_delete=models.CASCADE)

