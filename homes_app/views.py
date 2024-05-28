from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, DeleteView, CreateView, ListView
from hitcount.utils import get_hitcount_model

from .models import Homes, Category
from .forms import ContactForm, CommentForm
from uy_joy_savdo.custom_permissions import OnlyLoggedSuperUser



def homes_list(request):
    homes_list = Homes.objects.all().filter(status=Homes.Status.Published)
    catigory = Category.objects.all()
    context = {
        'homes_list': homes_list,
        'catigory': catigory
    }
    return render(request, "homes_list.html", context)

from hitcount.views import HitCountDetailView, HitCountMixin


def homes_detail(request, id):
    homes = get_object_or_404(Homes, id=id, status=Homes.Status.Published)
    context = {}
    #hitcount logic
    hit_count = get_hitcount_model().objects.get_for_object(homes)
    hits = hit_count.hits
    hitcontext = context['hitcount'] = {'pk': hit_count.pk}
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    if hit_count_response.hit_counted:
        hits = hits + 1
        hitcontext['hit_counted'] = hit_count_response.hit_counted
        hitcontext['hit_message'] = hit_count_response.hit_message
        hitcontext['total_hits'] = hits


    comments = homes.comments.filter(active=True)
    new_comment = None
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.homes = homes
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    context = {
        'homes': homes,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form

    }

    return render(request, 'homes_detail.html', context)



def homePageView(request):
    homes = Homes.objects.all().filter(status=Homes.Status.Published)
    maxsus = Homes.objects.all().filter(status=Homes.Status.Published).filter(tarifi=Homes.Tariff.maxsus)[:1]
    orta = Homes.objects.all().filter(status=Homes.Status.Published).filter(tarifi=Homes.Tariff.orta)[:6]
    catigory = Category.objects.all()
    context = {
        'homes': homes,
        'catigory': catigory,
        'maxsus': maxsus,
        'orta': orta,
    }
    return render(request, 'home_page.html', context)


# def contactPageView(request):
#     print(request.POST)
#     form = ContactForm(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         form.save()
#
#
#     context = {
#         'form': form
#     }
#     return render(request, 'contact.html')


class ContactPageView(TemplateView):
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2>biz bilanbog'langaniz uchun raxmat</h2>")
        context = {
            'form': form
        }

        return render(request, 'contact.html', context)

class HomesUpdateView(OnlyLoggedSuperUser, UpdateView):
    model = Homes
    fields = ('title', 'maydoni', 'xona_soni', 'tamiri', 'narxi', 'tel', 'image', 'manzil')
    template_name = 'crud/homes_edit.html'
    success_url = reverse_lazy('homes_list')

class HomesDeleteView(OnlyLoggedSuperUser, DeleteView):
    model = Homes
    template_name = 'crud/homes_delete.html'
    success_url = reverse_lazy('home_page')

class HomesCreateView(OnlyLoggedSuperUser,CreateView):
    model = Homes
    template_name = 'crud/homes_create.html'
    fields = '__all__'
    success_url = reverse_lazy('homes_list')
@login_required
@user_passes_test(lambda u:u.is_superuser)
def admin_page_view(request):
    admin_users = User.objects.filter(is_superuser=True)

    context = {
        'admin_users': admin_users
    }
    return render(request, 'pages/admin_page.html', context)



class SearchResultsView(ListView):
    model = Homes
    template_name = 'homes/search_result.html'
    context_object_name = 'barcha_homes'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Homes.objects.filter(
            Q(title__icontains=query) | Q(manzil__icontains=query) |Q(narxi__icontains=query)


        )