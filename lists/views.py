#from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item, List

# Create your views here.
def add_item(request, list_id):
	list_ = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))

def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))

def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)	
#	items = Item.objects.filter(id=list_id)

	item_label = ''
	if Item.objects.filter(list_id = list_id).count() == 0:
		item_label = 'yey, waktunya berlibur'
	elif Item.objects.filter(list_id = list_id).count() < 5:
		item_label = 'sibuk tapi santai'
	elif Item.objects.filter(list_id = list_id).count() >= 5:
		item_label = 'oh tidak'
	return render(request, 'list.html', {'list': list_, 'item_label':item_label})

def home_page(request):
#	if request.method == 'POST':
#		Item.objects.create(text=request.POST['item_text'])
#		return redirect('/lists/the-only-list-in-the-world/')
	
#	items = Item.objects.all()
	
	item_label = ''
	if Item.objects.count() == 0:
		item_label = 'yey, waktunya berlibur'
	elif Item.objects.count() < 5:
		item_label = 'sibuk tapi santai'
	elif Item.objects.count() >= 5:
		item_label = 'oh tidak'
	return render(request, 'home.html', {'item_label': item_label})
