# views.py

from django.shortcuts import render, redirect
from .models import Candidate


def home(request):

    if request.method == 'POST':

        action = request.POST.get('action')

        # ADD CANDIDATE

        if action == 'add':

            Candidate.objects.create(
                name=request.POST.get('name'),
                phone=request.POST.get('phone'),
                company=request.POST.get('company'),
                total_fee=request.POST.get('total_fee'),
                paid_amount=request.POST.get('paid_amount'),
                pending_amount=request.POST.get('pending_amount'),
                status=request.POST.get('status'),
            )

        # EDIT CANDIDATE

        elif action == 'edit':

            candidate = Candidate.objects.get(
                id=request.POST.get('candidate_id')
            )
            
            total_fee = int(request.POST.get('total_fee'))
            paid_amount = int(request.POST.get('paid_amount'))

            pending_amount = total_fee - paid_amount

            if pending_amount < 0:
                pending_amount = 0
            candidate.name = request.POST.get('name')
            candidate.phone = request.POST.get('phone')
            candidate.company = request.POST.get('company')
            candidate.total_fee = total_fee
            candidate.paid_amount = paid_amount
            candidate.pending_amount = pending_amount
            candidate.status = request.POST.get('status')

            candidate.save()

        # DELETE CANDIDATE

        elif action == 'delete':

            password = request.POST.get('delete_password')

            if password == "admin123":

                Candidate.objects.get(
                    id=request.POST.get('candidate_id')
                ).delete()

        return redirect('/')

    data = Candidate.objects.all().order_by('-id')

    total_paid = sum(i.paid_amount for i in data)
    total_pending = sum(i.pending_amount for i in data)

    context = {
        'data': data,
        'total_paid': total_paid,
        'total_pending': total_pending,
    }

    return render(request, 'home.html', context)