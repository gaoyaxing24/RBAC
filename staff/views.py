from django.shortcuts import render


def index(request):
	"""RBAC Index Page"""
	return render(request, "index.html")