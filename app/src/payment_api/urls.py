from django.urls import path
from .views import get_session_id

urlpatterns = [
    path("buy/<int:item_id>/", get_session_id, name="get-session-id"),
]
