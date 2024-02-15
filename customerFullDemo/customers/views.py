from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Customers
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import login, authenticate
from .forms import CustomerForm
from django.contrib.auth.decorators import login_required

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class CreateCustomerView(CreateView):
    redirect_field_name = 'customers/customers_list.html'
    form_class = CustomerForm
    model = Customers
    success_url = reverse_lazy('customer_list')

    def form_valid(self, form):
        form.instance.assign_to = self.request.user
        return super().form_valid(form)

class CustomerListView(ListView):
    model = Customers
    context_object_name = 'customers'
    queryset = model.objects.all()


class CustomerDetailView(DetailView):
    model = Customers

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('customer_list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def next(request):
    return redirect('customer_list')
