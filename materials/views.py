from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.core.paginator import Paginator
from .models import Materials
from .filters import CategoryFilter, MaterialFilter
from .forms import *

from bootstrap_modal_forms.generic import (
  BSModalCreateView,
  BSModalReadView,
  BSModalUpdateView,
  BSModalDeleteView
)

# get material count
def count_persentage(obj, value):
    persentage = "0"
    count = obj.objects.count()
    stock = obj.objects.filter(status=value).count()
    if not count == 0 and not stock == 0:
        persentage = "{:.2f}".format(round((stock/ count) * 100, 2))

    return persentage

# materials list wth pagination
class MaterialsList(generic.ListView):
    model = Materials
    paginate_by = 6
    context_object_name = "materials"
    template_name = 'pages/materials.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        count = Materials.objects.count()
        context['total_materials'] = count
        if count != 0:
            context['instock_materials'] = {
                    'count' : Materials.objects.filter(status=0).count(),
                    'persentage': count_persentage(Materials, 0)
                }
            context['outstock_materials'] = {
                    'count' : Materials.objects.filter(status=1).count(),
                    'persentage': count_persentage(Materials, 1)
                }
        context['total_categories'] = Categories.objects.count()


        context['segment'] = 'materials'
        context['num_of_objects'] = count
        context['c_material'] = Materials.objects.first()
        context['c_category'] = Categories.objects.first()
        context['material_filter'] = MaterialFilter(self.request.GET, queryset=Materials.objects.all())
        context['category_filter'] = CategoryFilter()
        context['categories'] = Categories.objects.all()
        return context

# material Details
class MaterialsDetails(generic.detail.DetailView):
    model = Materials
    context_object_name = "c_material"
    template_name = 'pages/materials.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['material_filter'] = MaterialFilter(self.request.GET, queryset=Materials.objects.all())
        context['category_filter'] = CategoryFilter()
        count = Materials.objects.count()
        context['total_materials'] = count
        if count != 0:
            context['instock_materials'] = {
                    'count' : Materials.objects.filter(status=0).count(),
                    'persentage': count_persentage(Materials, 0)
                }
            context['outstock_materials'] = {
                    'count' : Materials.objects.filter(status=1).count(),
                    'persentage': count_persentage(Materials, 1)
                }
        context['total_categories'] = Categories.objects.count()
        material_paginator = Paginator(context['material_filter'].qs, 6)
        page_number = self.request.GET.get('page')

        if type(page_number) is str:
            page_number = int(page_number)
        else:
            page_number = 1

        count = Materials.objects.count()
        context['categories'] = Categories.objects.all()
        context['page_obj'] = material_paginator.get_page(page_number)
        context['materials'] = material_paginator.page(page_number)
        context['c_category'] = Categories.objects.first()
        context['num_of_objects'] = context['material_filter'].qs.count()
        context['segment'] = "materials"                  

        return context

# material Details
class CategoriesDetails(generic.detail.DetailView):
    model = Categories
    context_object_name = "c_category"
    template_name = 'pages/materials.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['material_filter'] = MaterialFilter()
        context['category_filter'] = CategoryFilter(self.request.GET, queryset=Categories.objects.all())
        count = Materials.objects.count()
        context['total_materials'] = count
        if count != 0:
            context['instock_materials'] = {
                    'count' : Materials.objects.filter(status=0).count(),
                    'persentage': count_persentage(Materials, 0)
                }
            context['outstock_materials'] = {
                    'count' : Materials.objects.filter(status=1).count(),
                    'persentage': count_persentage(Materials, 1)
                }
        context['total_categories'] = Categories.objects.count()
        context['c_material'] = Materials.objects.first()
        context['categories'] = context['category_filter'].qs
        
        material_paginator = Paginator(Materials.objects.all(), 6)
        page_number = self.request.GET.get('page')

        if type(page_number) is str:
            page_number = int(page_number)
        else:
            page_number = 1
        context['page_obj'] = material_paginator.get_page(page_number)
        context['materials'] = material_paginator.page(page_number)
        context['num_of_objects'] = count
        context['segment'] = "materials"                  

        return context

# material Create
class MaterialCreateView(BSModalCreateView):
    template_name = 'pages/modals/materials/material-create.html'
    form_class = MaterialsCreate
    success_message = 'Success: New Materials was created.'
    success_url = reverse_lazy('materials')
    failure_url = reverse_lazy('materials')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['generated_id'] = Materials.Material_id()
        return context

# material Update
class MaterialUpdateView(BSModalUpdateView):
    model = Materials
    template_name = 'pages/modals/materials/material-update.html'
    form_class = MaterialsUpdate
    success_message = 'Success: Selected Material was updated.'
    success_url = reverse_lazy('materials')
    failure_url = reverse_lazy('materials')

# material Delete
class MaterialDeleteView(BSModalDeleteView):
    model = Materials
    template_name = 'pages/modals/materials/material-delete.html'
    success_message = 'Success: Selected Category was deleted.'
    success_url = reverse_lazy('materials')
    failure_url = reverse_lazy('materials')

# category Create
class CategoryCreateView(BSModalCreateView):
    template_name = 'pages/modals/materials/category-create.html'
    form_class = CategoryCreate
    success_message = 'Success: New Category was created.'
    success_url = reverse_lazy('materials')
    failure_url = reverse_lazy('materials')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['generated_id'] = Categories.category_id()
        return context

# category Update
class CategoryUpdateView(BSModalUpdateView):
    model = Categories
    template_name = 'pages/modals/materials/category-update.html'
    form_class = CategoryUpdate
    success_message = 'Success: Selected Category was updated.'
    success_url = reverse_lazy('materials')
    failure_url = reverse_lazy('materials')

# category Delete
class CategoryDeleteView(BSModalDeleteView):
    model = Categories
    template_name = 'pages/modals/materials/category-delete.html'
    success_message = 'Success: Selected Material was deleted.'
    success_url = reverse_lazy('materials')
    failure_url = reverse_lazy('materials')