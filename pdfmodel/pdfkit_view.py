from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
import pdfkit
from xhtml2pdf import pisa
from django.views import generic
from django.contrib.staticfiles import finders
from .models import Customer, CustomerPdf
import requests
from django.core.files.base import ContentFile
import PyPDF2

def sendfile(filestring):
    url = 'https://boardingbay-files.paywithconnect.com/api/v1/upload-file-base64/'
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        'file_type': "pdf",
        'extension': "pdf",
        'file_base64': filestring
    }

    # url = '{}/api/v1/upload-file-base64/'.format(url)
    response = requests.request("POST", url, headers=headers, json=payload, timeout=10)
    return response


def pdf(request):
    person = Customer.objects.get(id=1)
    template = get_template('pdfkit.html')

    obtain_token = requests.post('https://boardingbay-back.paywithconnect.com/api/v1/auth/mobileUserToken/',
                                 json={"employee_id": "admin", "password": "Test@34546"})
    headers = {'Authorization': "Circle " + obtain_token.json().get('data').get('token')}

    resp = requests.get('https://boardingbay-back.paywithconnect.com/api/v1/boarding/admin/users/17/', headers=headers)
    data = resp.json().get('data', None)

    html = template.render({'data': data})

    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
    }
    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment';
    response['Content-Disposition'] = 'filename="report.pdf"'


    entity = CustomerPdf()
    entity.save()

    entity.pdf_file.save('invoice.pdf', ContentFile(response.getvalue()), save=True)
    import base64
    bb = base64.b64encode(response.getvalue())
    inv_path = sendfile(bb.decode('utf-8'))

    return response
