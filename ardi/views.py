from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
from django.conf import settings
import os


def custom_404(request, exception):
    return render(request, 'front/404.html', {}, status=404)

class TermsAndConditionsView(TemplateView):
    template_name = 'front/terms_and_conditions.html'

class PrivacyView(TemplateView):
    template_name = 'front/privacy.html'

class FAQView(TemplateView):
    template_name = 'front/faq.html'

class WarrantyView(TemplateView):
    template_name = 'front/warranty.html'

class CareAndMaintenanceView(TemplateView):
    template_name = 'front/care_and_maintenance.html'

class About(View):
    def get(self, request):
        return render(request, 'front/about.html')
    
class Index(View):
    template_name = 'front/index.html'  # Remove the 'front/' prefix

    def get(self, request):
        testimonials = Testimonial.objects.all().order_by('-id')[:3]
        print(f"Template path being searched: {self.template_name}")
        return render(request, self.template_name, {'testimonials': testimonials})



class Galleries(View):
    def get(self, request):
        categories = Gallery.objects.values_list('category', flat=True).distinct()
        categorized_galleries = {}
        for categor in categories:
            categorized_galleries[categor] = Gallery.objects.filter(category=categor).order_by('id')

        context = {
            'categories': categories,
            'categorized_galleries': categorized_galleries,
        }
        return render(request, 'front/gallery.html', context)
    

class ProductDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'front/product_detail.html', {'product': product})
    
class ProductSearchView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('query')
        if query:
            products = Product.objects.filter(name__icontains=query)
            results = []
            for product in products:
                results.append({
                    'name': product.name,
                    'url': product.get_absolute_url(),  # Corrected attribute
                    'image': product.images.first().image.url if product.images.exists() else '',  # Adjust as needed
                })
            return JsonResponse(results, safe=False)
        return JsonResponse([], safe=False)

class Products(View):
    def get(self, request):
        categories = Product.objects.values_list('category', flat=True).distinct()
        categorized_products = {}
        for category in categories:
            categorized_products[category] = Product.objects.filter(category=category).order_by('id')

        context = {
            'categories': categories,
            'categorized_products': categorized_products,
        }

        return render(request, 'front/product.html', context)
    
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'front/product_detail.html', {'product': product})

class Testimonials(View):
    def get(self, request):
        testimonials = Testimonial.objects.all().order_by('id')
        return render(request, 'front/testimonial.html', {'testimonials':testimonials} )
    
class Service(View):
    def get(self, request):
        return render(request, 'front/service.html')
    
class Dashboard(LoginRequiredMixin, View):
    login_url = '/useracc/login/'
    def get(self, request):
    # Get data counts
        product_count = Product.objects.count()
        image_count = Image.objects.count()
        gallery_count = Gallery.objects.count()
        testimonial_count = Testimonial.objects.count()
        contact_count = Contact.objects.count()

        # Get distinct product areas
        Distinct_categories = Gallery.objects.values('category').distinct().count()

        context = {
            'product_count': product_count,
            'image_count': image_count,
            'gallery_count': gallery_count,
            'testimonial_count': testimonial_count,
            'contact_count': contact_count,
            'Distinct_categories': Distinct_categories,
        }

        return render(request, 'back/dashboard.html', context)


class ListProduct(LoginRequiredMixin, View):
    def get(self, request):
        products = Product.objects.all().order_by('id')
        return render(request, 'back/list_product.html', {'products': products})

class AddProduct(LoginRequiredMixin, View):
    def get(self, request):
        form = ProductForm()
        image_form = ProductImageForm()
        return render(request, 'back/add_product.html', {'form': form, 'image_form':image_form})

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            images = request.FILES.getlist('images')
            for image in images:
                ProductImage.objects.create(product=product, image=image)

            messages.success(request, 'you have added products successfully')
            return redirect(reverse('list_product'))
        image_form = ProductImageForm()
        return render(request, 'back/add_product.html', {'form': form, 'image_form':image_form})

class EditProduct(LoginRequiredMixin, View):
    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        form = ProductForm(instance=product)
        image_form = ProductImageForm()
        return render(request, 'back/add_product.html', {'form': form, 'product': product, 'image_form':image_form})

    def post(self, request, id):
        product = get_object_or_404(Product, id=id)
        form = ProductForm(request.POST,  instance=product)
        image_form = ProductImageForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            images = request.FILES.getlist('images')
            for image in images:
                ProductImage.objects.create(product=product, image=image)

            messages.success(request, 'you have edited Product successfully')
            return redirect(reverse('list_product'))
        return render(request, 'back/add_product.html', {'form': form, 'product': product, 'image_form':image_form})

class DeleteProduct(LoginRequiredMixin, View):
    def delete(self, request, id):
        product = get_object_or_404(Product, id=id)
        product.delete()
        return JsonResponse({'message': 'Product deleted successfully'}, status=200)

class DeleteProductImage(LoginRequiredMixin, View):
    def post(self, request, id):
        try:
            image = get_object_or_404(ProductImage, id=id)
            image.delete()
            messages.success(request, 'Image deleted successfully!')
        except ProductImage.DoesNotExist:
            messages.error(request, 'Image not found!')  # Inform user if image is missing
        return redirect('list_product')


class ListGallery(LoginRequiredMixin, View):
    def get(self, request):
        galleries = Gallery.objects.all().order_by('id')
        return render(request, 'back/list_gallery.html', {'galleries': galleries})

class AddGallery(View):
    def get(self, request):
        gallery_form = GalleryForm()
        image_form = ImageForm()
        return render(request, 'back/add_gallery.html', {'gallery_form': gallery_form, 'image_form': image_form})
    def post(self, request):
        gallery_form = GalleryForm(request.POST)
        
        if gallery_form.is_valid():
            gallery = gallery_form.save()
            images = request.FILES.getlist('images')
            for image_file in images:
                Image.objects.create(gallery=gallery, image=image_file)

            messages.success(request, 'Gallery and images added successfully!')  
            return redirect('list_gallery')
        image_form = ImageForm()
        return render(request, 'back/add_gallery.html', {'gallery_form': gallery_form, 'image_form': image_form})

class EditGallery(LoginRequiredMixin, View):
    def get(self, request, id):
        gallery = get_object_or_404(Gallery, id=id)
        gallery_form = GalleryForm(instance=gallery)
        image_form = ImageForm()
        return render(request, 'back/add_gallery.html', {'gallery_form': gallery_form, 'image_form': image_form, 'gallery': gallery})

    def post(self, request, id):
        gallery = get_object_or_404(Gallery, id=id)
        form = GalleryForm(request.POST, instance=gallery)
        image_form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            gallery = form.save()
            for image_file in request.FILES.getlist('images'):
                Image.objects.create(gallery=gallery, image=image_file)
            
            messages.success(request, 'Home and images added successfully!')
            return redirect(reverse_lazy('list_gallery'))
        
        context = {'form': form, 'image_form': image_form, 'gallery': gallery}
        return render(request, 'back/add_gallery.html', context)

class DeleteGallery(LoginRequiredMixin, View):
    def delete(self, request, id):
        try:
            gallery = Gallery.objects.get(id=id)
            gallery.delete()
            return JsonResponse({'success': True})
        except Gallery.DoesNotExist:
            return JsonResponse({'success': False}, status=404)

class DeleteImage(LoginRequiredMixin, View):
    def post(self, request, id):
        image = get_object_or_404(Image, id=id)
        image.delete()
        messages.success(request, 'Image deleted successfully!')
        return redirect('list_gallery')
        

class ListTestimonial(LoginRequiredMixin, View):
    def get(self, request):
        testimonials = Testimonial.objects.all().order_by('id')
        return render(request, 'back/list_testimonial.html', {'testimonials': testimonials})

class AddTestimonial(View):
    def get(self, request):
        form = TestimonialForm()
        return render(request, 'back/add_testimonial.html', {'form': form})

    def post(self, request):
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('list_testimonial'))
        return render(request, 'back/add_testimonial.html', {'form': form})

import logging

logger = logging.getLogger(__name__)

class EditTestimonial(LoginRequiredMixin, View):
    def get(self, request, id):
        testimonial = get_object_or_404(Testimonial, id=id)
        form = TestimonialForm(instance=testimonial)
        return render(request, 'back/add_testimonial.html', {'form': form, 'testimonial': testimonial})

    def post(self, request, id):
        testimonial = get_object_or_404(Testimonial, id=id)
        form = TestimonialForm(request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            logger.debug(f"Saving Testimonial with ID: {testimonial.id}")
            form.save()
            logger.debug(f"Testimonial with ID: {testimonial.id} saved successfully.")
            return redirect(reverse('list_testimonial'))
        logger.debug(f"Form is not valid. Testimonial ID: {testimonial.id}")
        return render(request, 'back/add_testimonial.html', {'form': form, 'testimonial': testimonial})
class DeleteTestimonial(LoginRequiredMixin, View):
    def delete(self, request, id):
        testimonial = get_object_or_404(Testimonial, id=id)
        testimonial.delete()
        return JsonResponse({'message': 'Testimonial deleted successfully'}, status=200)
        
class ListContact(LoginRequiredMixin, View):
    def get(self, request):
        contacts = Contact.objects.all()
        return render(request, 'back/list_contact.html', {'contacts': contacts})

class AddContact(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'front/contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully")
            return redirect(reverse('add_contact'))
        return render(request, 'front/contact.html', {'form': form})

class DeleteContact(LoginRequiredMixin, View):
    def delete(self, request, id):
        contact = get_object_or_404(Contact, id=id)
        contact.delete()
        return JsonResponse({'message': 'Contact deleted successfully'}, status=200)

#
#
#

class ListHome(LoginRequiredMixin, View):
    def get(self, request):
        homes = Home.objects.all()
        return render(request, 'back/list_home.html', {'homes': homes})

class AddHome(LoginRequiredMixin, View):
    def get(self, request):
        form = HomeForm()
        image_form = HomeImageForm()
        return render(request, 'back/add_edit_home.html', {'form': form, 'image_form': image_form, 'home': None})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            home = form.save()

            images = request.FILES.getlist('images')
            for image in images:
                HomeImage.objects.create(home=home, image=image)

            messages.success(request, 'Home and images added successfully!')
            return redirect('list_home')

        image_form = HomeImageForm()
        return render(request, 'back/add_edit_home.html', {'form': form, 'image_form': image_form, 'home': None})

class EditHome(LoginRequiredMixin, View):
    def get(self, request, id):
        home = get_object_or_404(Home, id=id)
        form = HomeForm(instance=home)
        image_form = HomeImageForm(instance= home)
        return render(request, 'back/add_edit_home.html', {'form': form, 'image_form': image_form, 'home': home})

    def post(self, request, id):
        home = get_object_or_404(Home, id=id)
        form = HomeForm(request.POST, instance=home)
        if form.is_valid():
            home = form.save()

            images = request.FILES.getlist('images')
            for image in images:
                HomeImage.objects.create(home=home, image=image)

            messages.success(request, 'Home and images updated successfully!')
            return redirect('list_home')

        image_form = HomeImageForm()
        return render(request, 'back/add_edit_home.html', {'form': form, 'image_form': image_form, 'home': home})


class DeleteHome(LoginRequiredMixin, View):
    def post(self, request, id):
        home = get_object_or_404(Home, id=id)
        home.delete()
        messages.success(request, 'Home deleted successfully!')
        return redirect('list_home')

class DeleteHomeImage(LoginRequiredMixin, View):
    def post(self, request, id):
        image = get_object_or_404(HomeImage, id=id)
        image.delete()
        messages.success(request, 'Image deleted successfully!')
        return redirect('list_home')