from urllib.request import urlopen, HTTPError
from uuid import uuid4

from django.core.files.base import ContentFile
from django.template.defaultfilters import slugify


def get_profile_data(backend, details, response, uid, user, *args, **kwargs):
    print(response)
    profile = user.profile
    if backend.__class__.__name__ == 'FacebookOAuth2':
        if not profile.login_type:
            profile.login_type = 'Facebook'
        # if not profile.display_name:
        #     profile.display_name = user.first_name.lower() + response.get('id')[:5]
        if not profile.gender and response.get('gender'):
            profile.gender = response.get('gender')
        if not profile.locale and response.get('locale'):
            profile.locale = response.get('locale')
        if not profile.social_id and response.get('id'):
            profile.social_id = response.get('id')
        user.save()
    if backend.__class__.__name__ == 'GoogleOAuth2':
        if not profile.login_type:
            profile.login_type = 'Google'
        # if not profile.display_name:
        #     profile.display_name = user.first_name.lower() + response.get('id')[:5]
        if not profile.gender and response.get('gender'):
            profile.gender = response.get('gender')
        if not profile.locale and response.get('locale'):
            profile.locale = response.get('locale')
        if not profile.social_id and response.get('id'):
            profile.social_id = response.get('id')
        user.save()


# TODO: change this algorithm to look better


def get_profile_avatar(backend, details, response,
                       uid, user, *args, **kwargs):
    url = None
    profile = user.profile
    if not profile.profile_photo:
        if backend.__class__.__name__ == 'FacebookOAuth2':
            url = "http://graph.facebook.com/%s/picture?type=large" % \
                  response.get('id')

        if backend.__class__.__name__ == 'GoogleOAuth2':
            url = response.get('image').get('url')
            url = url.replace('sz=50', 'sz=200')
        if url:
            try:
                avatar = urlopen(url)
                rstring = uuid4().hex
                profile.profile_photo.save(slugify(rstring + '_p') + '.jpg',
                                           ContentFile(avatar.read()))
                profile.save()
            except HTTPError:
                pass
