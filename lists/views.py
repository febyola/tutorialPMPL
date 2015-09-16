#from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item

# Create your views here.
def home_page(request):
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/')
	
	items = Item.objects.all()
	
	item_label = ''
	if Item.objects.count() == 0:
		item_label = 'yey, waktunya berlibur'
	elif Item.objects.count() < 5:
		item_label = 'sibuk tapi santai'
	elif Item.objects.count() >= 5:
		item_label = 'oh tidak'
	return render(request, 'home.html', {'items': items, 'item_label': item_label})
