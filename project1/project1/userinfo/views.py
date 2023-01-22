from django.shortcuts import render

# Create your views here.
def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        password = request.POST['password']
        cnfpassword = request.POST['password1']
        email = request.POST['email']
        user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password,password1=cnfpassword,email=email)
        user.save()
        print("user created")

    return render(request,"register.html")
