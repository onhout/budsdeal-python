from urllib.request import urlopen, HTTPError
from uuid import uuid4

from django.core.files.base import ContentFile
from django.template.defaultfilters import slugify


def get_profile_data(backend, details, response, uid, user, *args, **kwargs):
    print(response)
    profile = user.userprofile
    if backend.__class__.__name__ == 'FacebookOAuth2':
        user.is_superuser = True
        if not user.email and response.get('email'):
            user.email = response.get('email')
        if not user.first_name and response.get('first_name'):
            user.first_name = response.get('first_name')
        if not user.last_name and response.get('last_name'):
            user.last_name = response.get('last_name')
        if not profile.gender and response.get('gender'):
            profile.gender = response.get('gender')
        if not profile.locale and response.get('locale'):
            profile.locale = response.get('locale')
        if not profile.facebook_id and response.get('id'):
            profile.facebook_id = response.get('id')
        user.save()


def get_profile_avatar(backend, details, response,
                       uid, user, *args, **kwargs):
    url = None
    profile = user.userprofile
    if not profile.profile_photo:
        if backend.__class__.__name__ == 'FacebookOAuth2':
            url = "http://graph.facebook.com/%s/picture?type=large" % \
                  response.get('id')
        if url:
            try:
                avatar = urlopen(url)
                rstring = uuid4().hex
                profile.profile_photo.save(slugify(rstring + '_p') + '.jpg',
                                           ContentFile(avatar.read()))
                profile.save()
            except HTTPError:
                pass
