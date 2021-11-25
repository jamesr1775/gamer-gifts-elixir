from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'created_at_date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag',
                       'stripe_pid')

    fields = ('order_number', 'created_at_date', 'status',
              'full_name', 'phone_number', 'email', 
              'street_address1', 'street_address2', 'city', 
              'county', 'postcode', 'country',
              'order_total', 'delivery_cost', 'grand_total',
              'original_bag', 'stripe_pid')

    list_display = ('order_number', 'created_at_date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-created_at_date',)

admin.site.register(Order, OrderAdmin)