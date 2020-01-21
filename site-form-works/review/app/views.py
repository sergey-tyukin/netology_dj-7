import uuid

from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)

    form = ReviewForm()

    context = {
        'form': form,
        'product': product,
    }

    if Review.objects.filter(user_id=request.session.session_key).count() > 0:
        context['is_review_exist'] = True
    elif request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if not review_form.is_valid():
            context['errors'] = review_form.errors
            return render(request, template, context)

        review = review_form.save(commit=False)
        review.product = product
        review.user_id = request.session.session_key
        review.save()
        context['is_review_exist'] = True

    context['reviews'] = Review.objects.filter(product=pk)

    return render(request, template, context)
