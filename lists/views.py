#from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item

# Create your views here.
def new_list(request):
	Item.objects.create(text=request.POST['item_text'])
	return redirect('/lists/the-only-list-in-the-world/')

def view_list(request):
	
	items = Item.objects.all()

	#item_label = ''
	#if Item.objects.count() == 0:
	#	item_label = 'yey, waktunya berlibur'
	#elif Item.objects.count() < 5:
	#	item_label = 'sibuk tapi santai'
	#elif Item.objects.count() >= 5:
	#	item_label = 'oh tidak'
	return render(request, 'list.html', {'items':items})

def home_page(request):
#	if request.method == 'POST':
#		Item.objects.create(text=request.POST['item_text'])
#		return redirect('/lists/the-only-list-in-the-world/')
	
#	items = Item.objects.all()
	
#	item_label = ''
#	if Item.objects.count() == 0:
#		item_label = 'yey, waktunya berlibur'
#	elif Item.objects.count() < 5:
#		item_label = 'sibuk tapi santai'
#	elif Item.objects.count() >= 5:
#		item_label = 'oh tidak'
	return render(request, 'home.html')
