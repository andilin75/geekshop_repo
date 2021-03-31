from basket.models import Basket


def basket_status(request):
    user = request.user
    if user.is_authenticated:
        counter = Basket.objects.filter(user=user).count()
    else:
        counter = 0
    return {'basket_status': counter}
