from wiki.models import Page


def get_sidebar_context():
    query =  Page.objects.exclude(
        title='',
    ).order_by('-title')
    return query