import imp
from xml.dom.minidom import Document
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render


def main(request):
    return render(request, 'main.html')