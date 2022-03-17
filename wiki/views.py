from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_protect
from wiki.models import Page
from wiki.helper.context import get_sidebar_context


# Create your views here.
def page_index(request):
    sidebar = get_sidebar_context()
    context = {
        'sidebar': sidebar,
    }
    return render(request, 'main.html', context)


def page_edit(request, slug):
    return page_view(
        request=request,
        slug=slug,
        edit_mode=True,
    )


def page_view(request, slug, edit_mode=False):
    sidebar = get_sidebar_context()
    context = {
        'mode': 'view' if edit_mode == False else 'edit',
        'slug': slug,
        'sidebar': sidebar,        
        'page': {},
        'auth': request.user.is_authenticated,
    }

    try:
        page = Page.objects.get(slug=slug)
        context.update({
            'page': page
        })

    except ObjectDoesNotExist:
        context.update({
            'mode': 'create'
        })
        return render(request, 'page_edit.html', context)

    if edit_mode:
        return render(request, 'page_edit.html', context)

    else:
        page.view_count += 1
        page.save()

    return render(request, 'page_view.html', context)


@csrf_protect
def page_save(request, slug):
    data = request.POST
    page, page_create = Page.objects.update_or_create(
        slug=slug,
        defaults={
            'title': data.get('title', ''),
            'content': data.get('content', ''),
        }
    )
        
    to = reverse('wiki:page_view', kwargs={
        'slug': slug,
    })
    
    return redirect(to=to)