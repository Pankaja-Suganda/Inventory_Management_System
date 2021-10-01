from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.core.paginator import Paginator
from .models import Materials
from .filters import MaterialFilter
from .forms import *

from bootstrap_modal_forms.generic import (
  BSModalCreateView,
  BSModalUpdateView,
  BSModalDeleteView
)

# materials list wth pagination
class MaterialsList(generic.ListView):
    model = Materials
    paginate_by = 7
    context_object_name = "materials"
    template_name = 'pages/materials.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        count = Materials.objects.count()
        context['segment'] = 'materials'
        context['num_of_objects'] = count
        context['c_material'] = Materials.objects.first()
        context['material_filter'] = MaterialFilter(self.request.GET, queryset=Materials.objects.all())
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
        
        material_paginator = Paginator(context['material_filter'].qs, 7)
        page_number = self.request.GET.get('page')

        if type(page_number) is str:
            page_number = int(page_number)
        else:
            page_number = 1

        count = Materials.objects.count()
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
    success_message = 'Success: Selected Material was deleted.'
    success_url = reverse_lazy('materials')
    failure_url = reverse_lazy('materials')

# category Create
class CategoryCreateView(BSModalCreateView):
    template_name = 'pages/modals/materials/category-create.html'
    form_class = CategoryCreate
    success_message = 'Success: New Materials was created.'
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
    success_message = 'Success: Selected Material was updated.'
    success_url = reverse_lazy('materials')
    failure_url = reverse_lazy('materials')

# category Delete
class CategoryDeleteView(BSModalDeleteView):
    model = Categories
    template_name = 'pages/modals/materials/category-delete.html'
    success_message = 'Success: Selected Material was deleted.'
    success_url = reverse_lazy('materials')
    failure_url = reverse_lazy('materials')