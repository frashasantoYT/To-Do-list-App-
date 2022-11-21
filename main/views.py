from django.shortcuts import render,redirect
from django.contrib import messages
from main.models import ToDo
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy









def home(request):
    todos = ToDo.objects.order_by('id')
    
    context = {'todo_list': todos}
    
    if request.method == 'POST':
        todo = request.POST['task']
        if len(todo) == 0:
            messages.error(request, "Enter a task kindly")
            return redirect('home')

        add_task = ToDo(title = todo, complete = False) 
       
    
        
        if ToDo.objects.filter(title = add_task):
            messages.error(request, f'The task: {add_task} already exists')
            return redirect('home')
        
        ToDo.save(add_task)
  
    return render(request, 'main/index.html', context)




def TodoComplete(request, todo_id):
    todo = ToDo.objects.get(pk = todo_id) 
    todo.complete = True 
    todo.save()
    
    return redirect('home')

def deleteAllTodo(request):
    all_todo = ToDo.objects.all() 
    all_todo.delete()
    
    return redirect('home')


class DeleteTask(DeleteView):
    model = ToDo
    template_name = 'main/delete.html'
    context_object_name = 'todo' 
    success_url = reverse_lazy('home')



