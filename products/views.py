from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required 
from .forms import AddReviewForm
from .models import Product, Review
from django.http import HttpResponse


# Create your views here.
@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
 
    if request.method == 'POST':
        form = AddReviewForm(request.POST)
        print(form.data['content'])
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.author = request.user

            review.save()
            return redirect('product_detail', pk=product_id)
    else:
        form = AddReviewForm(initial={'product': product})
 
    return render(request, 'products/review.html', {'form': form})


def productMain(request):
    products = Product.objects.all()
    print(products[0].cost)
    return render(request, 'products/product.html', {'products': products})



def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    print(pk)
    reviews = Review.objects.filter(product=product.id)
    print(Review.objects.all())
    print(reviews)

    # print(reviews)
    return render(request, "products/product_detail.html", {'product': product, 'reviews': reviews})
    # return render(request, "products/product_detail.html", {'product': product})


def home(request):
    return HttpResponse('Hello, World!')