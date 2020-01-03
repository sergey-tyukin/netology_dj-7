from django.shortcuts import render

from phones.models import Phone

def show_catalog(request):
    template = 'catalog.html'
    sort_by = request.GET.get('sort', 'name')
    if sort_by == 'minprice':
        phones = Phone.objects.order_by('price')
    elif sort_by == 'maxprice':
        phones = Phone.objects.order_by('-price')
    else:
        phones = Phone.objects.order_by('name')
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.filter(slug=slug).get()}
    return render(request, template, context)
