from apps.user_messages.models import Conversations


def unread_message_count(request):
    if request.user.is_authenticated:
        messages = Conversations.objects.filter(to_user_id=request.user, read=False)
        return {
            'unread_message_count': len(messages)
        }
    return {}
