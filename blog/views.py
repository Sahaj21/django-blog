from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from .models import Post
from django.contrib import messages
from .forms import NewUserForm


# Create your views here.

def single_slug(request,single_slug):
	all_slugs = [c.slug for c in Post.objects.all()]

	if single_slug in all_slugs:
		req_post = Post.objects.get(slug = single_slug) 
		return render(  request = request,
						template_name = 'blog/post_full.html',
						context = {"Post": req_post}
			)
	return HttpResponse(f"'{single_slug}' does not correspond to anything we know of!")
	

def homepage(request):
	return render(request = request,
					template_name = 'blog/home.html',
					context = {"posts" : Post.objects.all}
		)




def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			login(request,user)
			redirect("blog:homepage")
		else:
			for msg in form.error_messages:
				messages.error( request, f"{msg}: {form.error_messages[msg]}")

			return render( request = request,
					template_name = 'blog/register.html',
					context = {"form" : form} )			

	form = NewUserForm(request.POST)
	return render( request = request,
					template_name = 'blog/register.html',
					context = {"form" : form} )





def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request = request,data = request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username = username, password = password)
			if user is not None:
				login(request,user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect('/')
			else:
				messages.error(request, f"Invalid Username or Password")
		else:
			messages.error(request, f"Invalid Uesername or Password.")
	form = AuthenticationForm()
	return render(request = request,
					template_name = 'blog/login.html',
					context = {"form": form})





def logout_request(request):
	logout(request)
	messages.info(request, f"Logged out successfully!")
	return redirect("blog:homepage")





'''

Post.objects.filter(status=1).order_by('-created_on')


class PostDetail(generic.DetailView):
	model = Post
	template_name = 'post_detail.html'
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    '''
