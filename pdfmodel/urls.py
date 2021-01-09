from django.urls import path
from .views import render_pdf_view, CustomerListView,customer_render_pdf_view

app_name = 'pdfmodel'

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer-list'),
    path('pdf/<int:pk>/', customer_render_pdf_view, name='customer-pdf-view'),
    path('test/', render_pdf_view, name='test-pdf'),
]