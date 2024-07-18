from django import forms
from django.forms import ModelMultipleChoiceField
from .models import *
from django.forms.widgets import FileInput

    
class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'inter your title'}),
            'category':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'inter category'})
        }

class ImageForm(forms.Form):
    class Meta:
        model = Image
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'quantity', 'area', 'price', 'description', 'category']
        widgets = {
            'category':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the category'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity'}),
            'area': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter area'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description', 'rows': 4}),
        }

class ProductImageForm(forms.Form):
    class Meta:
        model = ProductImage
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'content', 'date', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter testimonial content', 'rows': 4}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={ 'placeholder': 'Enter your name'}),
            'phone': forms.TextInput(attrs={ 'placeholder': 'Enter your phone number (optional)'}),
            'email': forms.EmailInput(attrs={ 'type': 'email', 'placeholder': 'Enter your email'}),
            'message': forms.Textarea(attrs={ 'placeholder': 'Enter message', 'rows': 4}),
        }




#
#
#
from django import forms
from django.forms import modelformset_factory
from .models import Home, HomeImage

class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = ['title', 'address', 'description', 'price']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter home title'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description', 'rows': 4}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
        }

class HomeImageForm(forms.ModelForm):
    class Meta:
        model = HomeImage
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }