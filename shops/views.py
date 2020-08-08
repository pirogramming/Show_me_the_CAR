from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from shops import models as shops_models
from cars import models as cars_models


def home(request):
    return render(request, "base.html")


def shop_detail(request, id):
    # POST 방식
    # 나의 평점을 POST 방식으로 추가하면 rating query에 평점이 등록됨
    if request.method == "POST":
        my_rating = request.POST.get("rating", None)
        if my_rating:
            shop = shops_models.Shop.objects.get(id=id)
            shops_models.Rating.objects.create(shop=shop, rating=my_rating)

        return redirect(reverse("shops:shop_detail", kwargs={"id": id}))

    # GET 방식
    shop = get_object_or_404(shops_models.Shop, id=id)

    # 특정 샵의 Pk로 먼저 필터링 후 그 샵의 rating field 값만 불러와서 리스트 생성
    ratings = shops_models.Rating.objects.filter(shop=id).values("rating")

    # 생성한 ratings 딕셔너리에서 value 값만 추출해서 평균 구하는 루프
    rating_sum = 0
    for r in ratings:
        r_value = list(r.values())
        rating_sum = rating_sum + sum(r_value)
    try:
        average = rating_sum / len(ratings)
    except:
        average = 0

    return render(request, "shops/shop_detail.html", {"shop": shop, "average": average})


def shop_list(request):
    # 만약에 검색한 것이 있다면 query 변수로 검색어가 들어감
    # 만약에 검색한 것이 없다면 shop 에서 모든 리스트를 받아와서 shop_list.html 템플릿으로 렌더링
    print(test)
    query = request.GET.get("q", None)
    shops = shops_models.Shop.objects.all()

    # 만약 검색어가 입력되었다면 if 문으로 진입
    if query:
        pk_list = cars_models.Car.objects.filter(model_name__icontains=query).values(
            "id"
        )
        pk = pk_list[0].get("id")
        shops = shops_models.Shop.objects.filter(car=pk)

        # 루프문 돌면서 검색된 자동차가 있는 모든 대리점을 찾아 하나의 쿼리로 묶은 뒤 shops 반환
        for i in range(1, len(pk_list)):
            pk = pk_list[i].get("id")
            shops = shops | shops_models.Shop.objects.filter(car=pk)

    ctx = {"shops": shops}
    return render(request, "shops/shop_list.html", ctx)


def shop_like(request, shop_id):
    shop = get_object_or_404(shops_models.Shop, id=shop_id)
    user = request.user
    query = request.GET.get("q", None)
    print(query)
    # 좋아요 기능, user가heart를 눌렀을 때, 대리점의 like_users list에 있으면 list에서 삭제되고 없으면 추가된다
    if user in shop.like_users.all():
        shop.like_users.remove(user)
    else:
        shop.like_users.add(user)
    return redirect("shops:shop_list")
