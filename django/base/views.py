from django.shortcuts import render, redirect
from . models import Student,Test, StudentData, Post
from . forms import StudentForm, CustomUserCreationForm, CustomUserChangeForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from django import forms
from .signals import custom_signal
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from datetime import datetime, time, date
from django.db.models import Avg, Sum, Min, Max, Count
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator




def home(request):
    custom_signal.send(sender=None) # to initiate signal
    context = {}
    return render(request, 'base/home.html', context)


##################################################################################################

''' Query Set '''

def querySet(request):
    # it will retrun all objects 
    obj1 = StudentData.objects.all() 
    # it will return objets with having marks==100
    obj2 = StudentData.objects.filter(marks=100) 
    # it will exclude objects with having marks==100
    obj3 = StudentData.objects.exclude(marks=100) 
    # it will order objects by first name
    obj4 = StudentData.objects.order_by('first_name')
    # it will order reversely objects by first name
    obj5 = StudentData.objects.order_by('first_name').reverse() 
    # it will return first object 
    obj6 = StudentData.objects.first() 
    # it will return last object
    obj7 = StudentData.objects.last() 
    # if will return True if object there in DB based on filtr else False
    obj8 = StudentData.objects.filter(city='Mumbai').exists() 
    # it will return only one object based on look up field which has to be unique 
    obj9 = StudentData.objects.get(id=6)

    # it will create object and store in DB
    """obj10 = StudentData.objects.create(first_name='Omkar2', last_name='Pedamkar', std=11, city='mumbai1', marks=90)"""
    
    # it will return two values -> (object, bool) 
    # if object with same data already there then it will return (get_object, False) 
    # else it will create and return (create_object, True)
    """obj11, created = StudentData.objects.get_or_create(first_name='Omkar2', last_name='Pedamkar', std=11, city='mumbai1', marks=90)"""
    # print(obj11, created) # resulr -> (Omkar2 Pedamkar, False)

    # Take single or multiple objects using filter and apply update method and it will update the data
    # before -> 10	Raj	Mukhne	11	Mysore	60
    """obj12 = StudentData.objects.filter(id=10).update(marks=90)"""
    # after -> 10 Raj	Mukhne	11	Mysore	90

    # it will return two values -> (object, bool) 
    # if we pass the data and that all data is already available in DB then it will just update and return -> (update_object, False)
    # if not present all data then it will create and return -> (created_object, True)
    """obj13, created = StudentData.objects.update_or_create(first_name='Omkar2', last_name='Pedamkar', std=11, city='mumbai1', marks=90)"""
    # print(obj13, created) # result -> (Omkar2 Pedamkar, False)

    # it will delete the object with help of filter method with lookup field
    '''obj14 = StudentData.objects.filter(id=10).delete()'''

    # it will return count of object
    '''obj15 = StudentData.objects.all().count()'''

    ### for lookup fields -> fieldName__method

    # it will return no of objects containg name exact 'omkar' (case sensitive)
    obj16 = StudentData.objects.filter(first_name__exact='omkar')

    # it will return no of objects containg first_name exact 'omkar' (case insensitive)(add i to make it insensitive)
    obj17 = StudentData.objects.filter(first_name__iexact='omkar')

    # it will return no of objects those contains "omkar" string in first_name field (case sensitive)
    obj18 = StudentData.objects.filter(first_name__contains='omkar')

    # it will return no of objects those contains "omkar" string in first_name field (case insensitive)
    obj19 = StudentData.objects.filter(first_name__icontains='omkar')

    # it will return no of objects those having id = 1,5,7,8 
    obj20 = StudentData.objects.filter(id__in=[1, 5, 7, 8])

    # it will return no of object those having marks greater than 70
    obj21 = StudentData.objects.filter(marks__gt=70)

    # it will return no of object those having marks greater than  or equal to 70
    obj22 = StudentData.objects.filter(marks__gte=70)

    # it will return no of object those having marks less than 70
    obj23 = StudentData.objects.filter(marks__lt=70)

    # it will return no of object those having marks less than  or equal to 70
    obj24 = StudentData.objects.filter(marks__lte=70)

    # it will return no of objects whose first_name starts with 'O' (case sensitive)
    obj25 = StudentData.objects.filter(first_name__startswith='O')

    # it will return no of objects whose first_name starts with 'O' (case insensitive)
    obj26 = StudentData.objects.filter(first_name__istartswith='O')

    # it will return no of objects whose first_name ends with 'r' (case sensitive)
    obj27 = StudentData.objects.filter(first_name__endswith='r')

    # it will return no of objects whose first_name ends with 'r' (case insensitive)
    obj28 = StudentData.objects.filter(first_name__iendswith='r')

    # it will return no of objects whose marks in range of 60 to 80 (inclusive)
    obj29 = StudentData.objects.filter(marks__range=('60', '80'))

    # it will return no of objects whose date exactly matches with (2022, 8, 10)
    obj30 = StudentData.objects.filter(passout__date=date(2022, 8, 10))

    # it will return no of objects whose date greater than (2022, 8, 10). same way gte, lt, lte
    obj31 = StudentData.objects.filter(passout__date__gt=date(2022, 8, 10))

    # it will return no of objects whose year exactly matches with 2021
    obj32 = StudentData.objects.filter(passout__year=2021)

    # it will return no of objects whose year greater than 2021. same way gte, lt, lte
    obj33 = StudentData.objects.filter(passout__year__gt=2021)

    # it will return no of objects whose month exactly matches with 10
    obj34 = StudentData.objects.filter(passout__month=10)

    # it will return no of objects whose month greater than 10. same way gte, lt, lte
    obj35 = StudentData.objects.filter(passout__month__gt=10)

    # it will return no of objects whose day date exactly matches with 5. (sun(0) - sat(6))
    obj36 = StudentData.objects.filter(passout__day=5)

    # it will return no of objects whose day date greater than 5. same way gte, lt, lte (sun(0) - sat(6))
    obj37 = StudentData.objects.filter(passout__day__gt=5)

    # it will return no of objects whose week exactly matches with 10 (week range 0-52)
    obj38 = StudentData.objects.filter(passout__week=10)

    # it will return no of objects whose week greater than 10. same way gte, lt, lte
    obj39 = StudentData.objects.filter(passout__week__gt=10)

    # it will return no of objects whose week day exactly matches with 10 (sun(0) - sat(6))
    obj40 = StudentData.objects.filter(passout__week_day=5)

    # it will return no of objects whose week day greater than 10. same way gte, lt, lte (sun(0) - sat(6))
    obj41 = StudentData.objects.filter(passout__week_day__gt=5)

    # it will return no of objects whose quarter is 2 (Q1: jan to mar, Q2: apr-jun, Q3: july-sep, Q4: oct-dec)
    obj42 = StudentData.objects.filter(passout__quarter=2)

    # it will return no of objects whose time exactly 21:05 
    obj43 = StudentData.objects.filter(passout__time=time(21, 5))

    # it will return no of objects whose hour exactly 13 
    obj44 = StudentData.objects.filter(passout__hour=13)

    # it will return no of objects whose minute exactly 43
    obj45 = StudentData.objects.filter(passout__minute=43)

    # it will return no of objects whose seconds exactly 45
    obj46 = StudentData.objects.filter(passout__second=45)

    # it will return no of objects whose city field is null(if its false then it will records whose city field not null)
    obj47 = StudentData.objects.filter(city__isnull=True)


    ### for Aggregate fields ->

    # it will calculate average of marks field
    obj48 = StudentData.objects.aggregate(Avg('marks'))

    # it will calculate total of marks field
    obj49 = StudentData.objects.aggregate(Sum('marks'))

    # it will calculate minimum of marks field
    obj50 = StudentData.objects.aggregate(Min('marks'))

    # it will calculate maximum of marks field
    obj51 = StudentData.objects.aggregate(Max('marks'))

    # it will calculate count of rows of marks field
    obj52 = StudentData.objects.aggregate(Count('marks'))


    ### for Q lookup fields -> (To add multiple lookup field in single filter using AND, OR, NOT)

    # AND -> it will return all objects who has id = 9 as well as having marks=90
    obj53 = StudentData.objects.filter(Q(id=9) & Q(marks=90))

    # OR -> it will return all objects who has id = 9 or marks=90
    obj54 = StudentData.objects.filter(Q(id=9) | Q(marks=100))

    # NOT -> it will return all objects except object who has id=9
    obj55 = StudentData.objects.filter(~Q(id=9))


    context = {'obj1': obj1, 'obj2': obj2, 'obj3':obj3, 'obj4':obj4,'obj5':obj5,
               'obj6':obj6, 'obj7':obj7,'obj9':obj9,'obj48':obj48, 'obj49':obj49, 'obj50':obj50,
               'obj51':obj51, 'obj52':obj52,'obj53':obj53, 'obj54':obj54, 'obj55':obj55
                }
    return render(request, 'base/queryset.html', context)


''' function based view V/S Class based view'''

# List view ->

# using function 
@login_required(login_url='userlogin') # to restrict page from Anonymous user in function based view
def studentList(request):
    students = Student.objects.all()
    context = {'students' : students}
    return render(request, 'base/student_list_f.html', context)

# using class 
# LoginRequiredMixin -> to restrict page from Anonymous user in class based view
# Add line in settings.py to redirect anonymous user -> LOGIN_URL = 'userlogin'
class StudentList(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'base/student_list_c.html'
    context_object_name = 'students'

    # to pass any different model data in class based using context method
    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)
        context['tests'] = Test.objects.all()
        return context


# Detail view ->

# using function 
def studentDetail(request, pk):
    student = Student.objects.get(id=pk)
    context = {'student' : student }
    return render(request, 'base/student_detail_f.html', context)

# using class 
class StudentDetail(DetailView):
    model = Student
    template_name = 'base/student_detail_c.html'
    context_object_name = 'student'


# Create view ->

# using function 
def studentCreate(request):
    form = StudentForm

    # without using form 
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        std = request.POST.get('std')

        Student.objects.create(name=name, email=email, std=std)
        return redirect('studentcreate-f')

    # with using form 

    '''if request.method == "POST":
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('studentcreate-f')'''
    
    context = {'form' : form}
    return render(request, 'base/student_create_f.html', context)

# using class 
class StudentCreate(CreateView):
    # without using any django form it will take care of get and post method
    model = Student
    fields = '__all__'
    template_name = 'base/student_create_c.html'
    context_object_name = 'form'
    success_url = '/studentcreatec/'

    # but is this case we wont get any styling or css as we are not using own modelform
    # to get that we need to override get form method

    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class':'my-name', 'placeholder':'Enter your name'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'my-email', 'placeholder':'Enter your email'})
        form.fields['std'].widget = forms.TextInput(attrs={'class':'my-std', 'placeholder':'Enter your std'})

        return form


    # to use djnago created form use this and this will take all styles or css which are mentioned in modelform
    # just remove model and fields from above code
    '''form_class = StudentCreateForm'''


# Update view ->

# using function 
def studentUpdate(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)
    context = {'form' : form}

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
        return redirect('home')

    return render(request, 'base/student_update_f.html', context)

# using class 
class StudentUpdate(UpdateView):
    # without using any django form it will take care of get and post method
    model = Student
    fields = '__all__'
    success_url = '/'
    template_name = 'base/student_update_c.html'
    context_object_name = 'form'

    # but is this case we wont get any styling or css as we are not using own modelform
    # to get that we need to override get form method

    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class':'my-name', 'placeholder':'Enter your name'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'my-email', 'placeholder':'Enter your email'})
        form.fields['std'].widget = forms.TextInput(attrs={'class':'my-std', 'placeholder':'Enter your std'})

        return form

    # to use djnago created form use this and this will take all styles or css which are mentioned in modelform
    # just remove fields from above code and make sure to add model 
        '''model = Student
        form_class = StudentForm'''


# delete view ->

# using function 
def studentDelete(request, pk):
    student = Student.objects.get(id=pk)
    context = {'student' : student}

    if request.method == 'POST':
        student.delete()
        return redirect('studentlist-f')

    return render(request, 'base/student_delete_f.html', context)

# using class 
class StudentDelete(DeleteView):
    model = Student
    success_url = '/studentlistc/'
    template_name = 'base/student_delete_c.html'
    
##################################################################################################

'''Pagination'''

# using function
def pagination(request):
    posts = Post.objects.all().order_by('id')
    # object_list:object of model, per_page:no of model object on single page
    # orphans: no of objects on last page should move to second last page in this case last 1 object should move to second last
    paginator = Paginator(object_list=posts, per_page=3, orphans=1)
    # get the page number value from page variable 
    page_number = request.GET.get('page')
    # based on page number pass those correspoding specific objects
    page_obj = paginator.get_page(page_number)
    context = {'page_obj' : page_obj}

    # here even if user passes random value to page then it will automatically will redirect user to last page

    return render(request, 'base/paginationf.html', context)

# using class
class PaginatorView(ListView):
    model = Post
    template_name = 'base/paginationc.html'
    paginate_by = 3
    paginate_orphans = 1

    # if user manually passes page value in url which is out of bound 
    # i.e. if we have 5 paginator pages but user gives page = 1000 then it will throw error.
    # hence we need to update page value to start that is 1 and then pass context data
    # use try if everything perfect retrun as it is else update page value to 1 and return it
    def get_context_data(self, *args, **kwargs):
        try:
            return super().get_context_data(*args, **kwargs)
        except Exception as e:
            self.kwargs['page'] = 1
            return super().get_context_data(*args, **kwargs)



##################################################################################################

'''User related functionality'''

# to create user signup form using built in UserCreationForm
def user_signup_form(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userlogin')
    else:
        form = UserCreationForm()

    return render(request, 'base/user_signup_form.html', {'form' : form})
    
# to create user signup form using custom CustomUserCreationForm which is inherited from UserCreationForm
def user_signup_form2(request):

    if request.method == "POST":
        # here we created CustomUserCreationForm using UserCreationForm. code present in models.py
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userlogin')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'base/user_signup_form2.html', {'form' : form})

# to create user login form using built in AuthenticationForm and allow user to login
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
    
    else:
        form = AuthenticationForm()
    
    return render(request, 'base/user_login.html', {'form' : form})

# to logout user
@login_required(login_url='userlogin')
def user_logout(request):
    logout(request)
    return redirect('home')

# to update user data using built in UserChangeForm
@login_required(login_url='userlogin')
def user_update_form(request):
    # This function will show all fields of user which is not preferred. 
    # Hence need to create custom form for this
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserChangeForm(instance=request.user)
    
    return render(request, 'base/user_update_form.html', {'form':form})

# to create user update form using custom CustomUserChangeForm which is inherited from UserChangeForm
@login_required(login_url='userlogin')
def user_update_form2(request):
    if request.method == "POST":
        # here we created CustomUserChangeForm using UserChangeForm. code present in models.py
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserChangeForm(instance=request.user)
    
    return render(request, 'base/user_update_form2.html', {'form':form})

# to update user password with old using PasswordChangeForm
@login_required(login_url='userlogin')
def user_password_update_with_old(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user) # to keep user signed in without killing session
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please enter correct password')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'base/user_password_change_with_old.html', {'form': form})

# to update user password without old using SetPasswordForm
@login_required(login_url='userlogin')
def user_password_update_without_old(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user) # to keep user signed in without killing session
            return redirect('home')
        else:
            messages.error(request, 'Please enter correct password')
    else:
        form = SetPasswordForm(request.user)
    return render(request, 'base/user_password_change_with_old.html', {'form': form})

##################################################################################################