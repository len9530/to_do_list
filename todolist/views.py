from django.shortcuts import render,redirect

# Create your views here.

LIST = []
def home(request):
	# global LIST
	if request.method == 'POST':
		if request.POST['item'] == '':
			return render(request,'todolist/home.html',{'warn':'请输入内容！','itemlist':LIST})
		else:
			DICT = { 'item':request.POST['item'],'finish':False }
			LIST.append(DICT)
			di = request.POST['item']
			return render(request,'todolist/home.html',{'itemlist':LIST,'msg':'添加成功！','delitem':di})
	else:
		return render(request,'todolist/home.html',{'itemlist':LIST})

def about(request):
	return render(request,'todolist/about.html')


def edit(request,forloop_counter):
	item = LIST[int(forloop_counter) - 1]['item']
	return render(request,'todolist/edit.html',{'nowitem':item,'forloop':forloop_counter})


def delete(request,forloop_counter):
	LIST.pop(int(forloop_counter) - 1)
	return redirect('todolist:主页')


def finish(request,forloop_counter):
	if request.POST['已完成'] == 'F':
		LIST[int(forloop_counter) - 1]['finish'] = False
		return redirect('todolist:主页')
	elif request.POST['已完成'] == 'T':
		LIST[int(forloop_counter) - 1]['finish'] = True
		return redirect('todolist:主页')


def reset(request,forloop_counter):
	LIST[int(forloop_counter) - 1]['item'] = request.POST.get('edit')
	return redirect('todolist:主页')