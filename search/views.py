from .models import Product, Favorite
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, ParagraphError
from django.http import HttpResponseRedirect
from django.shortcuts import render


def singup(request):
    """view return form sing up"""
    if request.method == 'POST':
        form = SignUpForm(request.POST, error_class=ParagraphError)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'search/index.html')
        else:
            context = {
                'errors': form.errors.items(),
                'form': form

            }

    else:
        form = SignUpForm()
        context = {
            'form': form

        }
    return render(request, 'search/signup.html', context)


def login_page(request):
    """view for login"""
    return render(request, 'search/login.html')


def post(request):
    """form post login and check user"""
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'search/login.html')


def index(request):
    """view return home page"""
    return render(request, 'search/index.html')


def search(request):
    """view allowing you to search for a product in the data base"""
    if request.user.is_authenticated:
        try:
            id_user = Favorite.objects.get(user=request.user.id)
            fav_product = Product.objects.filter(favorites=id_user.id)
        except ObjectDoesNotExist:
            fav_product = "1"

        query = request.GET.get('query')
        if not query:
            product = Product.objects.all()
        else:
            product = Product.objects.filter(name__icontains=query)

        context = {
            'product': product,
            'fav': fav_product
        }
        return render(request, 'search/search.html', context)
    else:
        return render(request, 'search/index.html')


def detail(request, product_id):
    """view allowing you to see all information for  product selected"""
    try:
        id_user = Favorite.objects.get(user=request.user.id)
        fav_product = Product.objects.filter(favorites=id_user.id)
    except ObjectDoesNotExist:
        fav_product = "1"
    product_selected = Product.objects.get(id=product_id)
    product_sub = Product.objects.filter(category_product=product_selected.category_product.id,
                                         score__lt=product_selected.score)

    paginator = Paginator(product_sub, 6)
    page = request.GET.get('page')

    try:
        product_sub = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        product_sub = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        product_sub = paginator.page(paginator.num_pages)
    context = {
        'product_selected': product_selected,
        'product_sub': product_sub,
        'fav': fav_product
    }
    return render(request, 'search/detail.html', context)


def fav(request, product_id):
    """view allowing add a prodcut in you favorites items"""
    product = Product.objects.get(id=product_id)
    try:
        favorite = Favorite.objects.get(user=request.user.id)
        favorite.products.add(product)
        favorite.save()
    except ObjectDoesNotExist:
        favorite = Favorite(user=request.user.id)
        favorite.save()
        favorite.products.add(product)

    return render(request, 'search/myfood.html')


def fav_delete(request, product_id):
    """view allowing delete a prodcut in you favorites items"""
    product = Product.objects.get(id=product_id)
    favorite = Favorite.objects.get(user=request.user.id, products=product)
    favorite.products.remove(product)
    return render(request, 'search/myfood.html')


def my_food(request):
    """view allowing show your favorites product"""
    if request.user.is_authenticated:
        try:
            id_user = Favorite.objects.get(user=request.user.id)
            fav_product = Product.objects.filter(favorites=id_user.id)
            context = {
                'product_selected': fav_product,
            }
        except ObjectDoesNotExist:
            context = {

            }
        return render(request, 'search/myfood.html', context)
    else:
        return render(request, 'search/index.html')


def account(request):
    """view allowing show your account info"""
    if request.user.is_authenticated:
        return render(request, 'search/account.html')
    else:
        return render(request, 'search/index.html')


def legal_notice(request):
    """view return legal info"""
    return render(request, 'search/legal_notice.html')

