from apps.user_messages.models import Conversations
from apps.products.models import Category


def unread_message_count(request):
    if request.user.is_authenticated:
        messages = Conversations.objects.filter(to_user_id=request.user, read=False)
        return {
            'unread_message_count': len(messages)
        }
    return {}


def category_list(request):
    parent_category = Category.objects.exclude(parent_category__isnull=False)
    child_category = Category.objects.exclude(parent_category__isnull=True)
    return {
        'parent_category': parent_category,
        'child_category': child_category,
    }
