from django.shortcuts import render, redirect
from .models import Candidate

DELETE_PASSWORD = "admin123"


def home(request):

    # ADD CANDIDATE
    if request.method == 'POST' and request.POST.get('action') == 'add':

        Candidate.objects.create(
            name=request.POST.get('name'),
            phone=request.POST.get('phone'),
            company=request.POST.get('company'),
            total_fee=request.POST.get('total_fee'),
            paid_amount=request.POST.get('paid_amount'),
            pending_amount=request.POST.get('pending_amount'),
            status=request.POST.get('status')
        )

        return redirect('/')

    # DELETE CANDIDATE
    if request.method == 'POST' and request.POST.get('action') == 'delete':

        entered_password = request.POST.get('delete_password')
        candidate_id = request.POST.get('candidate_id')

        if entered_password == DELETE_PASSWORD:

            Candidate.objects.filter(id=candidate_id).delete()

        return redirect('/')

    data = Candidate.objects.all().order_by('-id')

    total_paid = 0
    total_pending = 0

    for i in data:
        total_paid += i.paid_amount
        total_pending += i.pending_amount

    context = {
        'data': data,
        'total_paid': total_paid,
        'total_pending': total_pending
    }

    return render(request, 'home.html', context)