from django.urls import reverse_lazy

from django.generic.views import CreateView

# Create your views here.


class SignUpView(CreateView):
    form_class
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
