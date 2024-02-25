from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_name = request.GET.get('sort')
    if sort_name == 'min_price':
        context = {'phones': Phone.objects.all().order_by('price')}
        return render(request, template, context)
    elif sort_name == 'max_price':
        context = {'phones': Phone.objects.all().order_by('-price')}
        return render(request, template, context)
    elif sort_name == 'name':
        context = {'phones': Phone.objects.all().order_by('name')}
        return render(request, template, context)
    context = {'phones': Phone.objects.all()}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    a = Phone.objects.get(slug=slug)
    context = {'phone': a}
    return render(request, template, context)
