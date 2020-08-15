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

                qs = shops_models.Shop.objects.filter(**filter_args).order_by(
                    "created"
                )

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
    # # POST 방식
    # # 나의 평점을 POST 방식으로 추가하면 rating query에 평점이 등록됨

    # shop = get_object_or_404(shops_models.Shop, id=id)
    # print(shop)

    # # 특정 샵의 Pk로 먼저 필터링 후 그 샵의 rating field 값만 불러와서 리스트 생성
    # ratings = shops_models.Rating.objects.filter(shop_id=id).values("rating")
    # print(ratings)

    # # 생성한 ratings 딕셔너리에서 value 값만 추출해서 평균 구하는 루프
    # rating_sum = 0
    # for r in ratings:
    #     r_value = list(r.values())
    #     rating_sum = rating_sum + sum(r_value)
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

    data = {}
    return JsonResponse(data)
