from django.urls import path
from .views import ShowDetailView, create_comment_anonymous, create_comment_authenticated, favorite_logic, favorite_view, EditItemView, CreateItemView, delete_item, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),
    path('item/<slug:slug_item>/', ShowDetailView.as_view(), name='item_detail'),
    path('item/<int:pk_item>/comment_anonymous/', create_comment_anonymous, name='create_comment_anonymous'),
    path('item/<int:pk_item>/comment_authenticated/', create_comment_authenticated, name='create_comment_authenticated'),
    path('item/<int:pk_item>/favorite/', favorite_logic, name='favorite_logic'),
    path('favorites/', favorite_view, name='favorite_view'),
    path('item/<int:pk_item>/edit/', EditItemView.as_view(), name='edit_item'),
    path('item/create/', CreateItemView.as_view(), name='create_item'),
    path('item/<int:pk_item>/delete/', delete_item, name='delete_item'),
]