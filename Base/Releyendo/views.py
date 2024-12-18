from django.shortcuts import render
from django.http import HttpResponse

def inicio(request) :
    return HttpResponse ("Vista inicio")

def libros(request) :
    return  HttpResponse ("Vista libros")

def sobremi(request) :
    return  HttpResponse ("Vista sobremi")