from cotidia.metadata.conf import settings


def metadata_settings(request):

    return {
        "METADATA_FACEBOOK_APP_ID": settings.METADATA_FACEBOOK_APP_ID,
    }
