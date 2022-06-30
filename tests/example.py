from request_methods import post_request, patch_request, \
        get_request, delete_request
import pytest
from hw3.Post import Post
import requests


def create_post():
    post_dict = {'id': 46, 'title': 'aut quo modi neque nostrum ducimus',
            'body': 'voluptatem quisquam iste\nvoluptatibus natus officiis facilis dolorem\nquis quas ipsam\nvel et voluptatum in aliquid',
            'userId': 5}
    post = Post(**post_dict)
    return post

def test_post_created(create_post: Post):
    # создать объект поста
    # отправить запрос на создание
    url = 'https://jsonplaceholder.typicode.com/posts'
    payload = create_post.dict(exclude={'id'})
    returned_post = post_request(url, payload)
    print('create', returned_post.status_code)
    # если запрос вернёт созданную сущность - сравнить, если нет - вызвать get и сравнить


def test_post_updated(create_post):
# изменить объект
    create_post.body = 'new post body'
# отправить изменённые данные
    url = 'https://jsonplaceholder.typicode.com/posts'.format(create_post.id)
    payload = create_post.dict(exclude={'id'})
    returned_post = patch_request(url, payload)
    print('update', returned_post)
# сравнить что данные совпадают

def test_post_getted(create_post):
    url = 'https://jsonplaceholder.typicode.com/posts/{}'.format(create_post.id)
    returned_post = get_request(url)
    print('get', returned_post)
    created_post = create_post.dict()

def test_post_deleted(create_post):
    url = 'https://jsonplaceholder.typicode.com/posts'.format(create_post.id)
    returned_post = delete_request(url)
    print('delete', returned_post)


def test_url_code(url, expected_code):
    r = requests.get(url)
    print(r.status_code)
    assert r.status_code == int(expected_code)

test_url_code('https://ya.ru/sfhfhfhfhfhfhfhfh', 404)
