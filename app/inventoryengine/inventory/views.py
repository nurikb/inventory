from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import AdmissionSerializer, AdmissionDetailSerializer, EquipmentWorkerSerializer,EquipmentWorkerDetailSerializer, AdmissionCreateSerializer, TypeEquipmentListSerializer, EquipmentWorkerCreateSerializer

from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import View
from .utils import Export_xlsMixin

from .forms import *
from qrcode import *
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class AdmissionListView(APIView):
    """вывод поступлений"""

    def get(self, request):
        admission = Admission.objects.all()
        serializer = AdmissionSerializer(admission, many=True)
        return Response(serializer.data)


class AdmissionDetailView(APIView):
    """вывод поступлений"""

    def get(self, request, pk):
        admission = Admission.objects.get(id=pk)
        serializer = AdmissionDetailSerializer(admission)
        return Response(serializer.data)


class AddAdmissionView(APIView):
    """добавление записей о приоде"""

    def post(self, request):
        addadmission = AdmissionCreateSerializer(data=request.data)
        if addadmission.is_valid():
            addadmission.save()
        return Response(status=201)


class EquipmentWorkerListView(generics.ListAPIView):
    """вывод поступлений"""

    # def get(self, request):
    #     equipment = EquipmentWorker.objects.all()
    #     serializer = EquipmentWorkerSerializer(equipment, many=True)
    #     return Response(serializer.data)
    queryset = EquipmentWorker.objects.all()
    serializer_class = EquipmentWorkerSerializer


class EquipmentWorkerDetailView(APIView):
    """вывод поступлений"""

    def get(self, request, pk):
        equipment = EquipmentWorker.objects.get(id=pk)
        serializer = EquipmentWorkerDetailSerializer(equipment)
        return Response(serializer.data)


class TypeEquipmentListView(APIView):
    """вывод типа оборудования"""
    def get(self, request):
        type = Type.objects.all()
        serializer = TypeEquipmentListSerializer(type, many=True)
        return Response(serializer.data)


class EquipmentWorkerCreateView(APIView):
    """добавление записей закрепленных оборудований"""

    def get_id(self, request):
        e_id = request.data['inven_num']
        return e_id

    def post(self, request):
        addequipment = EquipmentWorkerCreateSerializer(data=request.data)
        if addequipment.is_valid():
            addequipment.save(inven_num=self.get_id(request))
            return Response(status=201)
        else:
            return Response(status=400)



def relocation_list(request):
    search_query = request.GET.get('search', '')

    if search_query:
        relocation = Relocation.objects.filter(Q(eq_name__icontains=search_query) |
                                               Q(movereason__icontains=search_query) |
                                               Q(previous_user__icontains=search_query) |
                                               Q(id_type__icontains=search_query) |
                                               Q(current_user__icontains=search_query) |
                                               Q(id_previous_room__icontains=search_query) |
                                               Q(id_current_room__icontains=search_query))
    else:
        relocation = Relocation.objects.all().order_by('-id')

    paginator = Paginator(relocation, 10)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
    'page_object': page,
    'is_paginated': is_paginated,
    'next_url': next_url,
    'prev_url': prev_url
    }

    return render(request, 'inventory/relocation.html', context=context)


class UploadView(View):
    def get(self, request):
        search_query = request.GET.get('search', '')

        if search_query:
            admission = Upload.objects.filter(name__icontains=search_query)
        else:
            admission = Upload.objects.all().order_by('-id')

        paginator = Paginator(admission, 10)

        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)

        is_paginated = page.has_other_pages()

        if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
        else:
            prev_url = ''

        if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
        else:
            next_url = ''
        form = UploadForm()
        context = {
        'form': form,
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
        }

        return render(request, 'inventory/upload.html', context=context)

    def post(self, request):
        search_query = request.GET.get('search', '')

        if search_query:
            admission = Upload.objects.filter(name__icontains=search_query)
        else:
            admission = Upload.objects.all().order_by('-id')
        paginator = Paginator(admission, 10)

        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)

        is_paginated = page.has_other_pages()

        if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
        else:
            prev_url = ''

        if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
        else:
            next_url = ''
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('upload_url'))

        return render(request, 'inventory/upload.html', context={'form': form,'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url})
#
def upload_delete(request):
    if request.method == 'POST':
        data = request.POST['delete']
        upload = Upload.objects.filter(id=data)
        upload.delete()

        return redirect(reverse('admissions_url'))


class EquipmentViewDelete(View):
    def get(self, request):

        search_query = request.GET.get('search', '')

        if search_query:
            equipments = EquipmentWorker.objects.filter(Q(eq_name__name__icontains=search_query) | Q(id_room__number__icontains=search_query) | Q(id_workers__full_name__icontains=search_query) | Q(id_type__name__icontains=search_query))
        else:
            equipments = EquipmentWorker.objects.all().order_by('-id')

        paginator = Paginator(equipments, 10)

        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)

        is_paginated = page.has_other_pages()

        if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
        else:
            prev_url = ''

        if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
        else:
            next_url = ''

        context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
        }
        return render(request, 'inventory/equipmentsForWorkers.html', context=context)

    def post(self, request):
        if request.method == 'POST':

            data = request.POST['delete']
            decommission = EquipmentWorker.objects.get(id=data)
            a_id = decommission.eq_name.id
            admission = Admission.objects.get(id=a_id)
            admission_decommission = admission.decommission+1
            admission.decommission = admission_decommission

            relocation = Relocation()
            relocation.count = 1
            relocation.upload = decommission.upload.name
            relocation.inven_num = decommission.inven_num
            relocation.relocation_date = datetime.datetime.now()
            relocation.movereason = 'списание'
            relocation.id_type = decommission.id_type.name
            relocation.eq_name = decommission.eq_name.name
            relocation.current_user = 'списанный обьект'
            relocation.id_current_room = 'списанный обьект'
            relocation.id_previous_room = decommission.id_room.number
            relocation.previous_user = decommission.id_workers.full_name

            relocation.save()
            decommission.delete()
            admission.save()

            return redirect(reverse('equipmentsForWorkers_url'))


class AdmissionView(View):
    def get(self, request):
        search_query = request.GET.get('search', '')

        if search_query:
            admission = Admission.objects.filter(Q(name__icontains=search_query) | Q(id_type__name__icontains=search_query))
        else:
            admission = Admission.objects.all().order_by('-id')

        paginator = Paginator(admission, 10)

        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)

        is_paginated = page.has_other_pages()

        if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
        else:
            prev_url = ''

        if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
        else:
            next_url = ''

        context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
        }

        return render(request, 'inventory/index.html', context=context)

    def post(self, request):
        if request.method == 'POST':
            data = request.POST['delete']
            admission = Admission.objects.get(id=data)
            equipments = EquipmentWorker.objects.filter(eq_name=admission.id)
            equipments.delete()
            admission.delete()
            return redirect(reverse('admissions_url'))


class AdmissionCreate(LoginRequiredMixin, View):
    def get (self, request):
        form = AdmissionForm()
        return render(request, 'inventory/addAdmissions.html', context={'form': form})

    def post(self, request):
        form = AdmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('admissions_url'))
    raise_exception = True


class AssignToWorker(LoginRequiredMixin, View):
    def get(self, request, admission_id):
        admission = Admission.objects.get(id=admission_id)
        form = EquipmentWorkersForm()
        return render(request, 'inventory/assignToWorker.html',
        context={'form': form,
        'admission': admission
        })

    def post(self, request, admission_id):
        admission = Admission.objects.get(id=admission_id)
        form = EquipmentWorkersForm(request.POST)

        if form.is_valid():

            out_of_stock = admission.out_of_stock
            out_of_stock += 1
            in_stock = admission.in_stock-1
            admission.out_of_stock = out_of_stock
            admission.in_stock = in_stock

            relocation=Relocation()
            relocation.count = 1
            relocation.inven_num = form.cleaned_data['inven_num']
            relocation.relocation_date = form.cleaned_data['date']
            relocation.movereason = 'закрепление'
            relocation.id_type = form.cleaned_data['id_type']
            relocation.eq_name = form.cleaned_data['eq_name']
            relocation.current_user = form.cleaned_data['id_workers']
            relocation.id_current_room = form.cleaned_data['id_room']
            relocation.id_previous_room = 'склад'
            relocation.previous_user = ' '
            relocation.upload = form.cleaned_data['upload']

            relocation.save()
            admission.save()
            form.save()
            return redirect(reverse('equipmentsForWorkers_url'))
        else:
            return render(request, 'inventory/assignToWorker.html',
        context={'form': form,
        'admission': admission})


class AssignToWorkerUpdate(LoginRequiredMixin, View):
    def get(self, request, admission_id):
        eq = EquipmentWorker.objects.get(id=admission_id)
        form = EquipmentWorkersUpdateForm(instance=eq)
        relocation_form=RelocationForm(request.POST)
        return render(request, 'inventory/update.html',
        context={
        'form': form,
        'eq': eq,
        'relocation_form': relocation_form,
        })

    def post(self, request, admission_id):
        eq = EquipmentWorker.objects.get(id=admission_id)
        # form = EquipmentWorkersForm(instance=eq)
        admission = eq.eq_name
        bound_form = EquipmentWorkersUpdateForm(request.POST, instance=eq)
        relocation_form = RelocationForm(request.POST)
        if bound_form.is_valid() and relocation_form.is_valid():
            out_of_stock = admission.out_of_stock
            in_stock = admission.in_stock

            admission.out_of_stock = out_of_stock
            admission.in_stock = in_stock

            relocation=Relocation()
            relocation.count = 1
            relocation.upload = bound_form.cleaned_data['upload']
            relocation.inven_num = bound_form.cleaned_data['inven_num']
            relocation.relocation_date = bound_form.cleaned_data['date']
            relocation.movereason = relocation_form.cleaned_data['movereason']
            relocation.id_type = bound_form.cleaned_data['id_type']
            relocation.eq_name = bound_form.cleaned_data['eq_name']
            relocation.current_user = bound_form.cleaned_data['id_workers']
            relocation.id_current_room = bound_form.cleaned_data['id_room']
            relocation.id_previous_room = relocation_form.cleaned_data['id_previous_room']
            relocation.previous_user = relocation_form.cleaned_data['previous_user']

            relocation.save()
            admission.save()
            bound_form.save()
            return redirect(reverse('equipmentsForWorkers_url'))
        else:
            return render(request, 'inventory/update.html',
                          context={
                              'form': bound_form,
                              'eq': eq,
                              'relocation_form': relocation_form,
                          })


class QrCreate(LoginRequiredMixin, View):
    def get(self, request, admission_id):
        eq = EquipmentWorker.objects.get(id=admission_id)
        return render(request, 'inventory/qr_detail.html',context={'eq': eq})

    def post(self, request, admission_id):
        eq = EquipmentWorker.objects.get(id=admission_id)

        if request.method == 'POST':
            data = request.POST['data']
            img = make(data)
            img.save("inventory/static/images/test.png")

        else:
            pass
        return render(request, 'inventory/qr_detail.html',context={'eq': eq, 'data': data})


class WorkersCreate(View):
    def get(self, request):
        form = WorkersForm()
        return render(request, 'inventory/addWorkers.html', context={'form': form})

    def post(self, request):
        form = WorkersForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse('workers_url'))


class Export_xls(Export_xlsMixin, View):

    column = ['дата', 'тип', 'наименование', 'приход', 'расход', 'остаток']
    row_date = Admission.objects.all().values_list('date')

    row = Admission.objects.all().values_list('id_type__name', 'name', 'admission', 'out_of_stock', 'in_stock')


class Export_xls_workers(Export_xlsMixin, View):

    column = ['дата', 'тип', 'наименование', 'сотрудник', 'кабинет', 'инвен-ый номер']
    row_date = EquipmentWorker.objects.all().values_list('date')

    row = EquipmentWorker.objects.all().values_list('id_type__name', 'eq_name__name', 'id_workers__full_name', 'id_room__number', 'inven_num')


class Export_xls_history(Export_xlsMixin, View):

    column = ['дата', 'тип', 'наименование', 'инвен-ый номер', 'Откуда', 'Куда', 'Предыдущий владелец', 'Новый владелец', 'Причина']
    row_date = Relocation.objects.all().values_list('relocation_date')

    row = Relocation.objects.all().values_list('id_type', 'eq_name', 'inven_num', 'id_previous_room', 'id_current_room', 'previous_user', 'current_user', 'movereason')

# Create your views here.
