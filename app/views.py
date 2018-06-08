from django.views.generic import CreateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import About, Work, Service, WhyChooseUs, AboutSlider, Numbers, Pricing, PriceContent, \
    Testimonial, Team, Blog, ContactUs, SendMessage
from .forms import ContactForm


# Create your views here.


class IndexView(LoginRequiredMixin, FormView):
    login_url = reverse_lazy('account_login')
    redirect_field_name = 'redirect_to'
    form_class = ContactForm
    success_url = reverse_lazy('app:index_view')
    template_name = 'app/index.html'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['about_list'] = About.objects.all()
        context['work_list'] = Work.objects.all()
        context['service_list'] = Service.objects.all()
        context['why_choose_us_list'] = WhyChooseUs.objects.all()
        context['about_slider_list'] = AboutSlider.objects.all()
        context['numbers_list'] = Numbers.objects.all()
        context['pricing_list'] = Pricing.objects.all()
        context['pricing_content_list'] = PriceContent.objects.all()
        context['testimonial_list'] = Testimonial.objects.all()
        context['team_list'] = Team.objects.all()
        context['blog_list'] = Blog.objects.all()
        context['contact_us_list'] = ContactUs.objects.all()

        return context


class BlogView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('account_login')
    redirect_field_name = 'redirect_to'
    model = Blog
    fields = ['author', 'image', 'title', 'text', 'publish_datetime']
    success_url = reverse_lazy('app:blog_view')
    template_name = 'app/blog.html'


class ContactView(FormView):
    template_name = 'app/contact_form.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
