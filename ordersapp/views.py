from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from mainapp.mixin import BaseClassContextMixin
from ordersapp.models import Order


class OrderListView(ListView, BaseClassContextMixin):
    model = Order
    title = 'Geekshop | список заказов'


class OrderCreateView(CreateView):
    pass


class OrderUpdateView(UpdateView):
    pass


class OrderDeleteView(DeleteView):
    pass


class OrderDetailView(DetailView):
    pass


def order_forming_complete(request, pk):
    pass


