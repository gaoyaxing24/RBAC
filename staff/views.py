# coding: utf-8
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse


def test_page(request, page):
    """RBAC Test Pages"""
    page_dict = dict(zip("1234", "一二三四"))
    return render(request, "test/page.html", {"pages": page_dict[str(page)]})

