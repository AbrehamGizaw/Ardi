from django.urls import path
from .views import *

urlpatterns = [
    path('terms-conditions/', TermsAndConditionsView.as_view(), name='terms_conditions'),
    path('privacy/', PrivacyView.as_view(), name='privacy'),
    path('faq/', FAQView.as_view(), name='faq'),
    path('warranty/', WarrantyView.as_view(), name='warranty'),
    path('care-maintenance/', CareAndMaintenanceView.as_view(), name='care_maintenance'),

    path('', Index.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('gallery/', Galleries.as_view(), name='gallery'),
    path('products/', Products.as_view(), name='products'),
    path('products/<int:id>/', product_detail, name='product_detail'),
    path('testimonial/', Testimonials.as_view(), name='testimonials'),
    path('service/', Service.as_view(), name='service'),
    path('admin/', Dashboard.as_view(), name='dashboard'),

    path('product/', ListProduct.as_view(), name='list_product'),
    path('products/add/', AddProduct.as_view(), name='add_product'),
    path('products/edit/<int:id>/', EditProduct.as_view(), name='edit_product'),
    path('products/delete/<int:id>/', DeleteProduct.as_view(), name='delete_product'),
    path('products/image/delete/<int:id>/', DeleteProductImage.as_view(), name='delete_product_image'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('search/', ProductSearchView.as_view(), name='product_search'),


    path('galleries/', ListGallery.as_view(), name='list_gallery'),
    path('galleries/add/', AddGallery.as_view(), name='add_gallery'),
    path('galleries/edit/<int:id>/', EditGallery.as_view(), name='edit_gallery'),
    path('galleries/delete/<int:id>/', DeleteGallery.as_view(), name='delete_gallery'),
    path('galleries/image/delete/<int:id>/', DeleteImage.as_view(), name='delete_image'),

    path('testimonials/', ListTestimonial.as_view(), name='list_testimonial'),
    path('testimonials/add/', AddTestimonial.as_view(), name='add_testimonial'),
    path('testimonials/edit/<int:id>/', EditTestimonial.as_view(), name='edit_testimonial'),
    path('testimonials/delete/<int:id>/', DeleteTestimonial.as_view(), name='delete_testimonial'),

    path('contacts/', ListContact.as_view(), name='list_contact'),
    path('contacts/add/', AddContact.as_view(), name='add_contact'),
    path('contacts/delete/<int:id>/', DeleteContact.as_view(), name='delete_contact'),





    #
    #
    #
    path('homes/', ListHome.as_view(), name='list_home'),
    path('homes/add/', AddHome.as_view(), name='add_home'),
    path('homes/edit/<int:id>/', EditHome.as_view(), name='edit_home'),
    path('homes/delete/<int:id>/', DeleteHome.as_view(), name='delete_home'),
    path('homes/image/delete/<int:id>/', DeleteHomeImage.as_view(), name='delete_home_image'),
]
