from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "description", "price"]







# class BookForm(forms.Form):
#     title = forms.CharField(max_length=200)
#     author = forms.CharField(max_length=200)
#     description = forms.Textarea()
#     publication_date = forms.DateField()
#
#
