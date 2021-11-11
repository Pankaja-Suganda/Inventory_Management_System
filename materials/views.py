from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.core.paginator import Paginator
from .models import Materials
from .filters import CategoryFilter, MaterialFilter, ShellFilter
from .forms import *
import json

from bootstrap_modal_forms.generic import (
  BSModalCreateView,
  BSModalReadView,
  BSModalUpdateView,
  BSModalDeleteView
)

# materials list wth pagination
class ShellsList(generic.ListView):
    model = Shell
    context_object_name = "shells"
    template_name = 'pages/shells.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        count = Shell.objects.count()
        context['total_shells'] = count
        if count != 0:
            context['empty_shells'] = {
                    'count' : Shell.objects.filter(status=0).count(),
                    'persentage': count_persentage(Shell, 0)
                }
            context['pfilled_shells'] = {
                    'count' : Shell.objects.filter(status=1).count(),
                    'persentage': count_persentage(Shell, 1)
                }
            context['filled_shells'] = {
                    'count' : Shell.objects.filter(status=2).count(),
                    'persentage': count_persentage(Shell, 2)
                }


        context['segment'] = 'shells'
        context['shell_filter'] = ShellFilter(self.request.GET, queryset=Shell.objects.all())
        context['shells'] = context['shell_filter'].qs

        shell_table = []
        for i, shell in enumerate(Shell.objects.all()):
            materials = Materials.objects.filter(shell_id =shell.id)
            shell_table.append({
                'id':shell.id,
                'shell': shell,
                'row' : shell.row,
                'column' : shell.column,
                'materials' : materials
            })
        page_number = self.request.GET.get('page')
        

        if type(page_number) is str:
            page_number = int(page_number)
        else:
            page_number = 1
            
        table = []
        for i in range(4):
            row = []
            for j in range(page_number-1, page_number+4):
                for shell in shell_table:
                    data = None
                    if shell['row'] == i and shell['column'] == j:
                        data = shell
                        break
                    else:
                        data = {'id':1}
                row.append(data)
            table.append(row)

        context['shell_table'] = table
        context['page_number'] = page_number
        context['page_next'] = page_number + 1
        context['page_previous'] = page_number - 1
        context['index_table'] = [0,1,2,3]
        return context

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
        material_paginator = Paginator(context['material_filter'].qs, 1)
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

# shell Create
class ShellCreateView(BSModalCreateView):
    template_name = 'pages/modals/materials/shell-create.html'
    form_class = ShellCreate
    success_message = 'Success: New Shell was created.'
    success_url = reverse_lazy('shells')
    failure_url = reverse_lazy('shells')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['generated_id'] = Shell.category_id()
        return context

# shell Update
class ShellUpdateView(BSModalUpdateView):
    model = Shell
    template_name = 'pages/modals/materials/shell-update.html'
    form_class = ShellUpdate
    success_message = 'Success: Selected Shell was updated.'
    success_url = reverse_lazy('shells')
    failure_url = reverse_lazy('shells')

# shell Delete
class ShellDeleteView(BSModalDeleteView):
    model = Shell
    template_name = 'pages/modals/materials/shell-delete.html'
    success_message = 'Success: Selected Shell was deleted.'
    success_url = reverse_lazy('shells')
    failure_url = reverse_lazy('shells')