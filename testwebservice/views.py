from http import HTTPStatus

import requests
from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from licenses.models import Licence
from owners.models import Owner
from repositories.models import Repository

PAGE_SIZE = 20


def get_data(request, url):
    response = requests.get(url)
    if response.status_code == HTTPStatus.NOT_FOUND:
        return render(
            request,
            '404.html',
            {'path': request.path},
            status=HTTPStatus.NOT_FOUND)

    for repository in response.json():
        owner = repository.get('owner')
        owner = Owner.objects.get_or_create(
            login=owner['login'], type=owner['type'])[0]
        license = repository.get('license')
        if license is not None:
            key = license.get('key')
            name = license.get('name')
            license = Licence.objects.get_or_create(key=key, name=name)[0]
        Repository.objects.update_or_create(
            git_id=repository.get('id'),
            name=repository.get('name', ''),
            private=repository.get('private', ''),
            owner=owner,
            full_name=repository.get('full_name', ''),
            html_url=repository.get('html_url', ''),
            language=repository.get('language', ''),
            forks_count=repository.get('forks_count', 0),
            size=repository.get('size', 0),
            is_template=repository.get('is_template', False),
            pushed_at=repository.get('pushed_at', 0),
            created_at=repository.get('created_at', 0),
            updated_at=repository.get('updated_at', 0),
            license=license)
    return redirect('repositories')


def get_org_data(request, owner):
    url = f'https://api.github.com/orgs/{owner}/repos'
    return get_data(request, url)


def get_user_data(request, owner):
    url = f'https://api.github.com/users/{owner}/repos'
    return get_data(request, url)


def repositories(request):
    repos = Repository.objects.all()
    paginator = Paginator(repos, PAGE_SIZE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'repos.html', {'page': page})
