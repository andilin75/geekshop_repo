from basket.models import Basket


def basket_status(request):
    user = request.user
    if user.is_authenticated:
        user_baskets = Basket.objects.filter(user=user)
        total_quantity = sum(basket.quantity for basket in user_baskets)
        return {'basket_status': total_quantity}
    return {'basket_status': None}
