from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views import generic
from django.contrib.staticfiles import finders
from .models import Customer


class CustomerListView(generic.ListView):
    template_name = 'main.html'
    queryset = Customer.objects.all()


def customer_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    customer = get_object_or_404(Customer, pk=pk)
    template_path = 'pdf2.html'
    context = {'customer': customer, 'name' : 'মোহাম্মদ লোকমান হোসেন মিশু'}

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    # if download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # if display
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response, encoding="UTF-8")
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def render_pdf_view(request):
    template_path = 'pdf1.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if display
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
