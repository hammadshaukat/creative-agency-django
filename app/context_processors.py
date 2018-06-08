from .models import HomeCustomization, FooterSocial


def home_customization(request):
    return {
        "home_customization": HomeCustomization.objects.get(pk=1)
    }


def footer_social_list(request):
    return {
        "footer_social_list": FooterSocial.objects.all()
    }


