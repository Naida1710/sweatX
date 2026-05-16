from decimal import Decimal
from django.conf import settings
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():

        try:
            product = Product.objects.get(pk=item_id)
        except Product.DoesNotExist:
            continue

        if isinstance(item_data, int):
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })

        else:
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    if total > 0 and total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = Decimal(settings.STANDARD_DELIVERY_FEE)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total_before_discount = delivery + total
    member_discount = 0
    is_member = False

    if request.user.is_authenticated:
        is_member = True
        member_discount = round(
            grand_total_before_discount
            * Decimal(settings.MEMBER_DISCOUNT_PERCENTAGE)
            / Decimal(100),
            2
        )

    grand_total = grand_total_before_discount - member_discount

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'is_member': is_member,
        'member_discount': member_discount,
        'grand_total_before_discount': grand_total_before_discount,
    }

    return context
