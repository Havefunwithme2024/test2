from django import template
from pages.models import FavoriteItems

register = template.Library()


@register.simple_tag()
def check_favorite_status(item_id, user_id):
    is_favorite = FavoriteItems.objects.filter(item_id=item_id, author_id=user_id).exists()
    return "В избранном" if is_favorite else "Не в избранном"