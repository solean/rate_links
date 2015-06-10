from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rate.models import Link


def index(request):
	context_dict = {}
	query = request.GET.get('q')
	if query:
		query.strip()
		context_dict['query'] = query

		if query.startswith('http://') or query.startswith('https://'):
			link = find_link(query)
		else:
			query = 'http://' + query
			link = find_link(query)

		if not link:
			return HttpResponseRedirect('create_link')

		link = link[0]
		context_dict['link'] = link
		return render(request, 'rate/link.html', context_dict)

	highest_rated = Link.objects.all().order_by('-avg_rating')[:10]
	most_liked = Link.objects.all().order_by('-likes')[:10]
	context_dict['highest_rated'] = highest_rated
	context_dict['most_liked'] = most_liked

	return render(request, 'rate/index2.html', context_dict)


def find_link(query):
	link = Link.objects.all().filter(url=query)
	if not link:
		if query.endswith('/'):
			query = query[:-1]
			link = Link.objects.all().filter(url=query)
		else:
			query = query + '/'
			link = Link.objects.all().filter(url=query)
	return link


def about(request):
	return render(request, 'rate/about.html', {})


def link(request, link_title_slug):
	context_dict = {}
	link = Link.objects.get(title_slug=link_title_slug)

	if not link:
		return HttpResponse("Invalid link")

	if request.method == 'POST':
		if request.POST.get('rating'):
			r = int(request.POST.get('rating'))

			num_ratings = link.num_ratings
			avg_rating = link.avg_rating

			new_rating = round(((avg_rating * num_ratings) + r) / (num_ratings + 1), 2)
			link.avg_rating = new_rating
			link.num_ratings = num_ratings + 1
		elif request.POST.get('like'):
			link.likes += 1

		link.save()

	like_rank = list(Link.objects.all().order_by('-likes')).index(link) + 1
	context_dict['like_rank'] = like_rank
	context_dict['link'] = link
	context_dict['link_title_slug'] = link.title_slug

	return render(request, 'rate/link.html', context_dict)


def create_link(request):
	context_dict = {}
	if request.method == 'POST':
		title = request.POST.get('title')
		url = request.POST.get('url')
		if title and url:
			if not url.startswith('http://'):
				url = 'http://' + url
			link = Link(title=title, url=url)
			link.save()
			return HttpResponseRedirect('/rate/link/' + link.title_slug)
		else:
			context_dict['errors'] = 'Please enter both a title and url for your link.'

	return render(request, 'rate/create_link.html', context_dict)



