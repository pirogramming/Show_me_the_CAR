from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.urls import reverse
from django.http import Http404, JsonResponse
from . import forms

from shops import models as shops_models
from cars import models as cars_models


def home(request):
    form = forms.SearchForm()
    return render(request, "shops/search_landing.html", {"form": form})


class ShopSearchView(View):

    """ Shop Search View """

    def get(self, request):
        user = request.user
        car_model = request.GET.get("car_model")
        query = car_model
        if car_model:
            form = forms.SearchForm(request.GET)
            if form.is_valid():
                print("valid")
                car_model = form.cleaned_data.get("car_model")
                # city = form.cleaned_data.get("city")

                filter_args = {}
                # if city != "Anywhere":
                #     filter_args["city__startswith"] = city

                if car_model is not None:
                    filter_args["car__model_name__icontains"] = car_model

                qs = shops_models.Shop.objects.filter(**filter_args).order_by("created")

                paginator = Paginator(qs, 30, orphans=5)

                page = request.GET.get("/?page", 1)

                shops = paginator.get_page(page)

        else:
            form = forms.SearchForm()
            shops = shops_models.Shop.objects.all().order_by("created")

        context = {
            "user": user,
            "form": form,
            "shops": shops,
            "query": query,
        }
        return render(request, "shops/search_main.html", context=context)


def shop_detail(request, id):
    try:
        shop = get_object_or_404(shops_models.Shop, id=id)
        average = shop.get_average_rating()
        print(average)
        return render(
            request, "shops/shop_detail.html", {"shop": shop, "average": average}
        )
    except shops_models.Shop.DoesNotExist:
        raise Http404()




class ShopListView(ListView):

    """ ShopListView definition """

    model = shops_models.Shop
    paginate_by = 30
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "shops"


@require_POST
def shop_like_ajax(request):
    user = request.user
    pk = request.POST.get("pk")
    action = request.POST.get("action")
    shop = get_object_or_404(shops_models.Shop, pk=pk)
    if action == "add_like":
        shop.like_users.add(user)

    elif action == "remove_like":
        shop.like_users.remove(user)
    shop.save()
    data = {}
    return JsonResponse(data)


def create_comment(request, id):
    comment = request.POST.get('comment', None)
    if comment:
        shop = get_object_or_404(shops_models.Shop, id=id)
        shops_models.Comment.objects.create(
            shop=shop,
            comment=comment
        )
    return redirect(reverse('shops:shop_detail', kwargs={'id': id}))

