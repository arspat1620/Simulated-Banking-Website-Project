from django.shortcuts import render,redirect
from .models import Transaction_History
from user.models import CustomUser

# Create your views here.

def transfer(request):
    if request.user.is_authenticated:
        name = request.user.username
        AcNo = f"{request.user.id:011}"
        balance = request.user.balance
    else:
        return redirect('login')
    
    if request.method=='POST':
        target_account = request.POST.get('AcNo')
        amount = request.POST.get('Amt')

        try:
            target_user = CustomUser.objects.get(id = int(target_account))
            if int(amount) > int(balance):
                raise ValueError
        except CustomUser.DoesNotExist:
            return render(request,'transfer.html',{'error' : "Account Number does not exist"})
        except ValueError:
            return render(request,'transfer.html',{'error' : "Insufficient Funds"})
        else:
            target_user.balance+=int(amount)
            target_user.save()
            request.user.balance-=int(amount)
            request.user.save()
            Transaction_History.objects.create(sender=AcNo, receiver=target_account, amount = int(amount))
            return render(request, 'transfer.html', {'success' : 'Transaction Successful'})


    
    return render(request,'transfer.html',{'name' : name})