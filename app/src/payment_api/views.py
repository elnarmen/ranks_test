from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
import stripe
from .models import Item
from django.conf import settings
from django.shortcuts import render
from django.urls import reverse


@api_view(["GET"])
def get_session_id(request, item_id: int) -> Response:
    stripe.api_key = settings.STRIPE_SECRET_KEY
    item = get_object_or_404(Item, pk=item_id)

    session = stripe.checkout.Session.create(
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "unit_amount": int(item.price * 100),
                    "product_data": {
                        "name": item.name,
                        "description": item.description,
                    },
                },
                "quantity": 1,
            }
        ],
        mode="payment",
        success_url=request.build_absolute_uri(reverse("success-payment")),
        cancel_url="https://example.com/cancel",
    )
    return Response({"session_id": session.id})


def buy_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    publishable_key = settings.STRIPE_PUBLISHABLE_KEY
    return render(
        request,
        "payment_api/buy.html",
        {"item": item, "pub_key": publishable_key},
    )


def success_payment(request):
    return render(request, "payment_api/success.html")
