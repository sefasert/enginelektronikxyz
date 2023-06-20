from django.shortcuts import render, get_object_or_404, redirect

from .models import Product, Related_Product

from category.models import Category

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from django.db.models import Q

from category.models import Setting

from django.http import JsonResponse

from .filters import ProductFilter

# Create your views here.

def store(request, category_slug=None):
    categories = None
    products = None
    setting = Setting.objects.get(pk=1)


    if category_slug !=None:
        categories     = get_object_or_404(Category, slug=category_slug)
        products       = Product.objects.filter(category=categories, is_available=True).order_by("-id")
        #filter
        myFilter       = ProductFilter(request.GET, queryset=products)
        products       = myFilter.qs
        paginator      = Paginator(products, 30)
        page           = request.GET.get("page")
        paged_products = paginator.get_page(page)
        product_count  = products.count()

    else:
        products       = Product.objects.all().filter(is_available=True).order_by("-id")
        #filter
        myFilter       = ProductFilter(request.GET, queryset=products)
        products       = myFilter.qs
        paginator      = Paginator(products, 30)
        page           = request.GET.get("page")
        paged_products = paginator.get_page(page)
        product_count  = products.count()

    context = {
        "products"      : paged_products,
        "product_count" : product_count,
        "categories"    : categories,
        "setting"       : setting,
        "myFilter"      : myFilter,
    }
    return render(request, "store/store.html", context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        products = Product.objects.filter(category=single_product.category, is_available=True)
        categories     = get_object_or_404(Category, slug=category_slug)
    except Exception as e:
        raise e


    related_product = Related_Product.objects.filter(product_id=single_product.id)


    context = {
        "single_product" : single_product,
        "categories"     : categories,
        "related_product": related_product,
        "products": products #benzer ürün
    }
    return render(request, "store/product_detail.html", context)


def search(request):
    products = Product.objects.filter(is_available=True).order_by("-created_date")

    if "keyword" in request.GET:
        keyword = request.GET["keyword"]
        if keyword:
            products       = Product.objects.filter(is_available=True).order_by("-created_date").filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            #filter
            myFilter       = ProductFilter(request.GET, queryset=products)
            products       = myFilter.qs
            product_count  = products.count()
        else:
            return redirect("store")


    context = {
        "products"      : products,
        "product_count" : product_count,
        "myFilter"      : myFilter,
    }
    return render(request, "store/store.html", context)


def home(request, category_slug=None):
    categories = None
    products = None
    setting = Setting.objects.get(pk=1)

#    show_cookie_policy = False
#    if not request.COOKIES.get('cookie_policy_accepted'):
#        show_cookie_policy = True

    if category_slug !=None:
        categories     = get_object_or_404(Category, slug=category_slug)
        products       = Product.objects.filter(category=categories, is_available=True)
        #filter
        myFilter       = ProductFilter(request.GET, queryset=products)
        products       = myFilter.qs
        paginator      = Paginator(products, 18)
        page           = request.GET.get("page")
        paged_products = paginator.get_page(page)


    else:
        products       = Product.objects.all().filter(is_available=True).order_by("-id")
        #filter
        myFilter       = ProductFilter(request.GET, queryset=products)
        products       = myFilter.qs
        paginator      = Paginator(products, 18)
        page           = request.GET.get("page")
        paged_products = paginator.get_page(page)

#    if request.method == 'POST' and 'cookie_accept' in request.POST:
#        response = redirect('home')
#        response.set_cookie('cookie_policy_accepted', 'true')
#        return response

    context = {
        "products"      : paged_products,
        "categories"    : categories,
        "setting"       : setting,
        "myFilter"      : myFilter,
#        'show_cookie_policy': show_cookie_policy
    }

    if request.htmx:
        return render(request, 'list.html', context)
    return render(request, "index.html", context)

def otoyazi(request):
    query_original = request.GET.get("term")
    queryset = Product.objects.filter(product_name__icontains=query_original, is_available=True)
    mylist = []
    mylist += [x.product_name for x in queryset]

    return JsonResponse(mylist, safe=False)


def filter_results(request):
    products       = Product.objects.filter(is_available=True).order_by("-id")
    #filter
    myFilter       = ProductFilter(request.GET, queryset=products)
    products       = myFilter.qs
    paginator      = Paginator(products, 33)
    page           = request.GET.get("page")
    try:
        paged_products = paginator.page(page)
    except PageNotAnInteger:
        paged_products = paginator.page(1)
    except EmptyPage:
        paged_products = paginator.page(paginator.num_pages)

    page_obj=paginator.get_page(page)

    context = {
        'products':products,
        'myFilter':myFilter,
        'page_obj':page_obj
    }
    return render(request, 'store/store.html', context)
