from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import GeneralFile
from .forms import GeneralFileForm



class GeneralFileListView(ListView):
    model = GeneralFile
    template_name = "generalfile_list.html"
    context_object_name = "files"
    paginate_by = 20

    def get_queryset(self):
        qs = GeneralFile.objects.all()

        last_name = self.request.GET.get("last_name")
        phone = self.request.GET.get("phone_number")
        national_code = self.request.GET.get("national_code")

        if last_name:
            qs = qs.filter(last_name__icontains=last_name)

        if phone:
            qs = qs.filter(phone_number__icontains=phone)

        if national_code:
            qs = qs.filter(national_code__icontains=national_code)

        return qs

class GeneralFileCreateView(CreateView):
    model = GeneralFile
    form_class = GeneralFileForm
    template_name = "generalfile_form.html"
    success_url = reverse_lazy("generalfile_list")


class GeneralFileUpdateView(UpdateView):
    model = GeneralFile
    form_class = GeneralFileForm
    template_name = "generalfile_form.html"
    success_url = reverse_lazy("generalfile_list")


class GeneralFileDeleteView(DeleteView):
    model = GeneralFile
    template_name = "generalfile_confirm_delete.html"
    success_url = reverse_lazy("generalfile_list")
