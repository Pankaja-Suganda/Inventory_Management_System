from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.core.paginator import Paginator
from customer.models import Customer
from .models import Product, ProductCategories, Color, Size, Product_Material
from materials.models import Categories, Materials
from .filters import CategoryFilter, SizeFilter, ColorFilter, ProductFilter
from .forms import CategoryForm, SizeForm, ColorForm, ProductForm, ProductUpdateForm, MaterialFormSet, ProductMaterialForm
import json
import datetime

from bootstrap_modal_forms.generic import (
  BSModalCreateView,
  BSModalReadView,
  BSModalUpdateView,
  BSModalDeleteView
)

# materials list wth pagination
class ProdcutsList(generic.ListView):
    model = Product
    template_name = 'pages/items.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['segment'] = 'items'
        context['tab'] = 0

        if self.request.method == 'GET':
            if self.request.GET.get('tab') != None:
                context['tab'] = int(self.request.GET.get('tab'))
            elif self.request.GET.get('value') != None:
                context['tab'] = int(self.request.GET.get('value'))
        
        if self.request.GET.get('product-filter') == None :
            context['Product_filter'] = ProductFilter(None, queryset=Product.objects.all())
            if context['tab'] == 0:
                context['Category_filter'] = CategoryFilter(self.request.GET or None, queryset=ProductCategories.objects.all())
                context['Color_filter'] = ColorFilter(None, queryset=Color.objects.all())
                context['Size_filter'] = SizeFilter( None, queryset=Size.objects.all())

            elif context['tab'] == 1:
                context['Category_filter'] = CategoryFilter(None, queryset=ProductCategories.objects.all())
                context['Color_filter'] = ColorFilter(None, queryset=Color.objects.all())
                context['Size_filter'] = SizeFilter(self.request.GET or None, queryset=Size.objects.all())

            elif context['tab'] == 2:
                context['Category_filter'] = CategoryFilter(None, queryset=ProductCategories.objects.all())
                context['Color_filter'] = ColorFilter(self.request.GET or None, queryset=Color.objects.all())
                context['Size_filter'] = SizeFilter(None, queryset=Size.objects.all())
        else:
            context['Product_filter'] = ProductFilter(self.request.GET or None, queryset=Product.objects.all())
            context['Category_filter'] = CategoryFilter(None, queryset=ProductCategories.objects.all())
            context['Color_filter'] = ColorFilter(None, queryset=Color.objects.all())
            context['Size_filter'] = SizeFilter(None, queryset=Size.objects.all())

        context['In_Stock'] = Product.objects.filter(status=0).count()
        context['Out_Stock'] = Product.objects.filter(status=1).count()
        context['Category_count'] = ProductCategories.objects.all().count()
        context['Sizes_count'] = Size.objects.all().count()

        context['Categories'] = context['Category_filter'].qs
        context['Colors'] = context['Color_filter'].qs
        context['Sizes'] = context['Size_filter'].qs
        

        paginator = Paginator(context['Product_filter'].qs, 6)
        page_number = self.request.GET.get('page')
        

        if type(page_number) is str:
            page_number = int(page_number)
        else:
            page_number = 1

        context['page_obj'] = paginator.get_page(page_number)
        context['Products'] = paginator.page(page_number)
        context['num_of_objects'] = Product.objects.count()

        return context


# Category Create
class ProductCategoryCreateView(BSModalCreateView):
    model = ProductCategories
    template_name = 'pages/modals/product/category-create.html'
    form_class = CategoryForm
    success_message = 'Success: New Product Category was created.'
    success_url = '/items/?tab=0'
    failure_url = reverse_lazy('items')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['generated_id'] = ProductCategories.category_id()
        return context

# Category Update
class ProductCategoryUpdateView(BSModalUpdateView):
    model = ProductCategories
    template_name = 'pages/modals/product/category-update.html'
    form_class = CategoryForm
    success_message = 'Success: Selected Shell was updated.'
    success_url = '/items/?tab=0'
    failure_url = reverse_lazy('items')

# Category Delete
class ProductCategoryDeleteView(BSModalDeleteView):
    model = ProductCategories
    template_name = 'pages/modals/product/category-delete.html'
    success_message = 'Success: Selected Shell was deleted.'
    success_url = '/items/?tab=0'
    failure_url = reverse_lazy('items')

# size Create
class SizeCreateView(BSModalCreateView):
    model = Size
    template_name = 'pages/modals/product/size-create.html'
    form_class = SizeForm
    success_message = 'Success: New Size was created.'
    success_url = '/items/?tab=1'
    failure_url = reverse_lazy('items')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['generated_id'] = Size.size_id()
        return context

# size Update
class SizeUpdateView(BSModalUpdateView):
    model = Size
    template_name = 'pages/modals/product/size-update.html'
    form_class = SizeForm
    success_message = 'Success: Selected Size was updated.'
    success_url = '/items/?tab=1'
    failure_url = reverse_lazy('items')

# size Delete
class SizeDeleteView(BSModalDeleteView):
    model = Size
    template_name = 'pages/modals/product/size-delete.html'
    success_message = 'Success: Selected Size was deleted.'
    success_url = '/items/?tab=1'
    failure_url = reverse_lazy('items')


# Color Create
class ColorCreateView(BSModalCreateView):
    model = Color
    template_name = 'pages/modals/product/color-create.html'
    form_class = ColorForm
    success_message = 'Success: New Color was created.'
    success_url = '/items/?tab=2'
    failure_url = reverse_lazy('items')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['generated_id'] = Color.color_id()
        return context

# Color Update
class ColorUpdateView(BSModalUpdateView):
    model = Color
    template_name = 'pages/modals/product/color-update.html'
    form_class = ColorForm
    success_message = 'Success: Selected Color was updated.'
    success_url = '/items/?tab=2'
    failure_url = reverse_lazy('items')

# Color Delete
class ColorDeleteView(BSModalDeleteView):
    model = Color
    template_name = 'pages/modals/product/color-delete.html'
    success_message = 'Success: Selected Color was deleted.'
    success_url = '/items/?tab=2'
    failure_url = reverse_lazy('items')

# Product Create
class ProductCreateView(BSModalCreateView):
    model = Product
    template_name = 'pages/modals/product/product-create.html'
    form_class = ProductForm
    success_message = 'Success: New Product was created.'
    success_url = reverse_lazy('items')
    failure_url = reverse_lazy('items')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['generated_id'] = Product.prodcut_id()
        context['form_set'] = MaterialFormSet() 
        return context

    def post(self, request, *args, **kwargs):
        form = ProductForm(self.request.POST or None)
        form_set = MaterialFormSet(self.request.POST or None)

        if form.is_valid():
            product = Product(
                id = form.cleaned_data['id'],
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                unit_price = form.cleaned_data['unit_price'],
                stock_margin = form.cleaned_data['stock_margin'],
                category_id = ProductCategories.objects.filter(name=form.cleaned_data['category_id']).first(),
                color_id = Color.objects.filter(name=form.cleaned_data['color_id']).first(),
                Size_id = Size.objects.filter(name=form.cleaned_data['Size_id']).first(),
                added_date = datetime.datetime.now()
            )
            product.make_stock_status()
            product.save()
            print('product id : ', product, product.id, form.cleaned_data['category_id'])
            
            for form_material in form_set:
                if form_material.is_valid():
                    material_id = Materials.objects.filter(name=form_material.cleaned_data['material_id']).first()
                    quantity = int(form_material.cleaned_data['quantity'])
                    if material_id != None and quantity > 0:
                        p_material = Product_Material(material_id=material_id, quantity=quantity)
                        p_material.product_id = product
                        p_material.save()
                        product.material_ids.add(p_material)

            product.save()

        return redirect(self.success_url)

# Product Update
class ProductUpdateView(BSModalUpdateView):
    model = Product
    template_name = 'pages/modals/product/product-update.html'
    form_class = ProductUpdateForm
    form_set = MaterialFormSet() 
    success_message = 'Success: Selected Product was updated.'
    success_url = reverse_lazy('items')
    failure_url = reverse_lazy('items')

# Product Delete
class ProductDeleteView(BSModalDeleteView):
    model = Product
    template_name = 'pages/modals/product/product-delete.html'
    success_message = 'Success: Selected Product was deleted.'
    success_url = reverse_lazy('items')
    failure_url = reverse_lazy('items')