from django.views.generic import CreateView, TemplateView, ListView  #imported cbv
from .models import post #imported post
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.

class postListAndCreate(CreateView, LoginRequiredMixin):
    model = post
    template_name = "profile.html"
    fields = ['attach_file', 'description',]

    def get_context_data(self, **kwargs):
        context = super(postListAndCreate, self).get_context_data(**kwargs)
        context["posts"] = post.objects.filter(author=self.request.user)
        return context

    def form_valid(self, form):
        form.instance.author= self.request.user
        return super().form_valid(form)

class home(TemplateView):
    template_name = "home.html"

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'