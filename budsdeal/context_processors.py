from apps.products.models import Category
from apps.user_messages.models import Conversations


def unread_message_count(request):
    if request.user.is_authenticated:
        messages = Conversations.objects.filter(to_user_id=request.user, read=False)
        return {
            'unread_message_count': len(messages)
        }
    return {}


def category_list(request):
    categories = Category.objects.exclude(parent_category__isnull=False)
    # child_category = Category.objects.exclude(parent_category__isnull=True)
    # print(Category.objects.filter(parent_category__in=parent_category))
    for parent in categories:
        parent.menu_bar_all = []
        parent.menu_bar = []
        parent.menu_bar_all.append(Category.objects.filter(parent_category=parent)[4:])
        parent.menu_bar.append(Category.objects.filter(parent_category=parent)[:4])
    return {
        'categories': categories,
        # 'child_category': child_category,
        # 'child_category_menu': child_category[:5]
    }
