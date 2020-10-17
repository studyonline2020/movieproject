from django.shortcuts import render

def home_page(request):
	return render(request=request,template_name='movieapp/homepage.html')

from movieapp.forms import MoviedetailsForm
def add_movie(request):
	movie_form=MoviedetailsForm()

	# This is to make the changes of  the data enterted by end user in the database
	if request.method=='POST':
		form_data=MoviedetailsForm(request.POST)
		if form_data.is_valid():
			form_data.save(commit=True)

	# This is used to display the data enterted by end user on Development server
	if request.method=="POST":
		form_data=MoviedetailsForm(request.POST)
		if form_data.is_valid():
			print(f'releasedate:{form_data.cleaned_data["releasedate"]}')
			print(f'moviename:{form_data.cleaned_data["moviename"]}')
			print(f'hero:{form_data.cleaned_data["hero"]}')
			print(f'heroine:{form_data.cleaned_data["heroine"]}')
			print(f'rating:{form_data.cleaned_data["rating"]}')


	my_dict={'movie_form':movie_form}
	return render(request=request,template_name='movieapp/addmovie.html',context=my_dict)


from movieapp.models import Moviedetails
def movie_list(request):
	movie_data=Moviedetails.objects.all()
	my_dict={'movie_data':movie_data}
	return render(request=request,template_name='movieapp/movielist.html',context=my_dict)