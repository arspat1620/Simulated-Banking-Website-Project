from django.shortcuts import render,redirect
from transaction.models import Transaction_History
from django.db.models import Q

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        name = request.user.username
    try:
        if name:
            return render(request,'home.html',{'name' : name})
    except UnboundLocalError:
        return render(request,'home.html')

def about(request):
    if request.user.is_authenticated:
        name = request.user.username
    try:
        if name:
            return render(request,'about.html',{'name' : name})
    except UnboundLocalError:
        return render(request,'about.html')

def account(request):
    if request.user.is_authenticated:
        name = request.user.username
        AcNo = f"{request.user.id:011}"
        balance = request.user.balance
    else:
        return redirect('login')
    
    results = Transaction_History.objects.filter(Q(sender=f"{AcNo:011}") | Q(receiver=AcNo)).order_by("-id")[:10]
    myList=list()
    for transaction in results:
        if transaction.sender==AcNo:
            myList.append(f"<tr class='text-info'><td>{transaction.id}</td><td>{transaction.receiver}</td><td>{transaction.amount}</td><td>Transfer</td>")
        else:
            myList.append(f"<tr class='text-info'><td>{transaction.id}</td><td>{transaction.sender}</td><td>{transaction.amount}</td><td>Received</td></tr>")
    
    if myList:
        return render(request,'account.html',{'name' : name, 'AcNo' : AcNo, 'balance' : balance, 'list' : myList})
    else:
        return render(request,'account.html',{'name' : name, 'AcNo' : AcNo, 'balance' : balance})
    