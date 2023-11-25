from django.urls import path
from .views import get_session_id, buy_item, success_payment

urlpatterns = [
    path("api/buy/<int:item_id>/", get_session_id, name="get-session-id"),
    path("item/<int:item_id>/", buy_item, name="buy-item"),
    path("success/", success_payment, name="success-payment"),
]
