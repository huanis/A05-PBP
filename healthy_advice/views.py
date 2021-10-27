from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.http import response
from django.http.response import HttpResponseRedirect,  HttpResponse, JsonResponse
from healthy_advice.models import CommentHealthy
from healthy_advice.forms import NoteForm
from django.http import HttpResponse, JsonResponse
from django.core import serializers
# from healthy_advice.models import Rating

# Create your views here.
def healthy_advice(request):
    notes = CommentHealthy.objects.all()
    flag = False
    form = NoteForm()
    for note in notes:
        print(note.commentator_name)
        print("user adalah " + str(request.user))
        print(str(note.commentator_name) == str(request.user))
        if (str(note.commentator_name) == str(request.user)):
            flag=True
            print("HALOOOOOOOOOOOO")
            break
    if request.is_ajax():
        form = NoteForm(request.POST)
        if form.is_valid():
            print(request.user)
            obj = form.save(commit=False)
            obj.commentator_name = request.user
            # print(obj)
            obj.save()
            print(obj.commentator_name)
            return HttpResponseRedirect("/healthy_advice")
        
    response = {'notes' : notes, 'form' : form, 'flag': flag}
    return render(request, 'healthy_advice.html', response)

def get_all_comment(request):
    all_comment = CommentHealthy.objects.all()
    data = serializers.serialize('json', all_comment)
    return HttpResponse(data, content_type="application/json")

def delete_comment(request, id):
    obj = get_object_or_404(CommentHealthy, id = id)
    
    if request.method == "POST":
        # delete object
        obj.delete()
        
    data = serializers.serialize('json', CommentHealthy.objects.all())

    return HttpResponse(data, content_type='application/json')

def edit_comment(request, id):
    obj = get_object_or_404(CommentHealthy, id = id)
    if request.is_ajax():
        new_comment = request.POST.get('comment_field')
        obj.comment_field = new_comment
        obj.save()
    data = serializers.serialize('json', [obj, ])    
    return HttpResponse(data, content_type = 'application/json')


def manfaat_istirahat(request):
    return render(request, 'manfaat_istirahat.html')
