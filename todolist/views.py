from django.shortcuts import render,redirect
from .models import Todo
# Create your views here.


def home(request):
	if request.method == 'POST':
		if request.POST['item'] == '':
			return render(request,'todolist/home.html',{'warn':'请输入内容！','itemlist':Todo.objects.all()})
		else:
			a = Todo(thing = request.POST['item'])
			a.save()
			return render(request,'todolist/home.html',{'itemlist':Todo.objects.all(),'msg':'添加成功！'})
	else:
		return render(request,'todolist/home.html',{'itemlist':Todo.objects.all()})

def about(request):
	return render(request,'todolist/about.html')


def edit(request,i_id):
	ni = Todo.objects.get(id = i_id).thing
	return render(request,'todolist/edit.html',{'nowitem':ni,'d':i_id})


def delete(request,i_id):
	a = Todo.objects.get(id = i_id)
	a.delete()
	return redirect('todolist:主页')


def finish(request,i_id):
	if request.POST['已完成'] == 'T':
		f = Todo.objects.get(id = i_id)
		f.done = True
		f.save()
		return redirect('todolist:主页')
	elif request.POST['已完成'] == 'F':
		f = Todo.objects.get(id = i_id)
		f.done = False
		f.save()
		return redirect('todolist:主页')


def reset(request,d):
	if request.POST['reset'] == '':
		print(123)
		print(d)
		return render(request,'todolist/edit.html',{'warn':'请输入内容','d':d})
	else:
		a = Todo.objects.get(id = d)
		a.thing = request.POST.get('reset')
		a.save()
		return redirect('todolist:主页')


