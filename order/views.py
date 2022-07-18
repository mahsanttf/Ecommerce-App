from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Orders, OrderDetails
from product.Cart import Cart


class OrderListView(generic.ListView):
    model = Orders
    template_name = 'order/orders.html'

    def get_queryset(self):
        super().get_queryset()
        order_by = self.request.GET.get('order_by')
        direction = self.request.GET.get('direction')
        if direction:
            if direction == 'asc':
                ordering = '{}'.format(order_by)
                order = Orders.objects.all().order_by(ordering)
            else:
                ordering = '-{}'.format(order_by)
                order = Orders.objects.all().order_by(ordering)
        else:
            order = Orders.objects.all()
        return order


class OrderCreateView(generic.CreateView):
    model = Orders
    fields = [
        'name',
    ]

    def get_success_url(self):
        return reverse('order:order_list')


class OrderDetailView(generic.DetailView):
    model = Orders
    template_name = 'order/orderdetails.html'

    def dispatch(self, request, *args, **kwargs):
        obj = get_object_or_404(Orders, pk=self.kwargs['pk'])
        if self.request.user.is_staff:
            return super().dispatch(request, *args, **kwargs)
        else:
            if self.request.user.username == obj.name:
                return super().dispatch(request, *args, **kwargs)
            else:
                raise Http404

    # def get_context_data(self, **kwargs):
    #     context = super(OrderDetailView, self).get_context_data(**kwargs)
    #     context['OrderDetails'] = get_object_or_404(OrderDetails, pk=self.kwargs['pk'])
    #     return context

    # def get_success_url(self):
    #     return reverse('order:order_detail', kwargs={'pk': self.object.order.pk})
