from django.db import models


# Create your models here.
# Need to discuss about Work details or External Link, Why choose us, Section titles, PriceContent, purchase now button.


class HomeCustomization(models.Model):
    logo_top = models.ImageField()
    logo_bottom = models.ImageField()
    banner_heading = models.CharField(max_length=255)
    banner_text = models.TextField()
    welcome_note = models.CharField(max_length=255)
    featured_works_heading = models.CharField(max_length=255)
    services_heading = models.CharField(max_length=255)
    why_choose_us_heading = models.CharField(max_length=255)
    why_choose_us_text = models.TextField()
    pricing_table_heading = models.CharField(max_length=255)
    our_team_heading = models.CharField(max_length=255)
    recent_news_heading = models.CharField(max_length=255)
    get_in_touch_heading = models.CharField(max_length=255)

    def __str__(self):
        return "Home Customization"


class About(models.Model):
    icon = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Work(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Work'

    def __str__(self):
        return self.title


class Service(models.Model):
    icon = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class WhyChooseUs(models.Model):
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'Why Choose Us'

    def __str__(self):
        return self.text


class AboutSlider(models.Model):
    image = models.ImageField()

    def __str__(self):
        return "Slider Image " + str(self.id)


class Numbers(models.Model):
    icon = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    number = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Numbers'
        verbose_name_plural = 'Numbers'

    def __str__(self):
        return self.title


class Pricing(models.Model):
    title = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class PriceContent(models.Model):
    pricing = models.ForeignKey(Pricing, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return "%s - %s" % (self.pricing.title, self.title)


class Testimonial(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.name


class Team(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    facebook_url = models.URLField()
    google_url = models.URLField()
    twitter_url = models.URLField()

    def __str__(self):
        return self.name


class BlogAuthor(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField()
    bio = models.TextField()
    facebook = models.URLField()
    google = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField()

    def __str__(self):
        return self.name


class Blog(models.Model):
    author = models.ForeignKey(BlogAuthor, on_delete=models.CASCADE)
    image = models.ImageField()
    title = models.CharField(max_length=255)
    text = models.TextField()
    publish_datetime = models.DateTimeField()  # Need to discuss about edit/update DateTime field.

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()
    publish_datetime = models.DateTimeField()

    def __str__(self):
        return self.email


class ContactUs(models.Model):
    icon = models.ImageField(null=True, blank=True)
    contact_title = models.CharField(max_length=255)
    contact_detail = models.TextField()

    class Meta:
        verbose_name_plural = 'Contact Us'

    def __str__(self):
        return self.contact_title


class SendMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email


class FooterSocial(models.Model):
    title = models.CharField(max_length=255)
    icon = models.ImageField()
    url = models.URLField()

    def __str__(self):
        return self.title

