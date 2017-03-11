from django.shortcuts import render

# Create your views here.

def concepto_pago(request):
    return render(request, 'core/home.html', {})

def provedor(request):
    return render(request, 'core/rol.html', {})

def factura(request):
    return render(request, 'core/permiso.html', {})