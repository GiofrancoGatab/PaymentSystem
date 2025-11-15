from django.shortcuts import render, redirect, get_object_or_404
from .models import Payment
from django.utils import timezone
from decimal import Decimal

# LIST + ADD FORM TOGETHER
def add_payment(request):
    if request.method == 'POST':
        card_number = request.POST.get('card_number')
        cardholder_name = request.POST.get('cardholder_name')
        amount = request.POST.get('amount')
        action = request.POST.get('action')  # deposit or withdraw

        # Use current date and time if empty
        now = timezone.now()
        date = now.date()
        time_str = now.strftime('%H:%M:%S')  # HH:MM:SS format

        Payment.objects.create(
            card_number=card_number,
            cardholder_name=cardholder_name,
            amount=Decimal(amount),
            action=action,
            date=date,
            time=time_str
        )
        return redirect('payment_list')

    return render(request, 'add_payment.html')


# EDIT PAYMENT
from django.utils import timezone
from decimal import Decimal

def edit_payment(request, id):
    payment = Payment.objects.get(id=id)

    if request.method == "POST":
        # Keep ID and cardholder name unchanged
        payment_id = payment.id
        cardholder_name = payment.cardholder_name

        # Get new transaction info
        new_action = request.POST.get("new_action")  # 'deposit' or 'withdraw'
        new_amount = Decimal(request.POST.get("new_amount"))

        # Adjust amount based on new action
        if new_action == "deposit":
            payment.amount += new_amount
        elif new_action == "withdraw":
            payment.amount -= new_amount

        # Update action to new transaction
        payment.action = new_action

        # Update date and time to current
        payment.date = timezone.now().date()
        payment.time = timezone.now().time()

        payment.save()

        return redirect('payment_list')

    return render(request, "edit_payment.html", {"payment": payment})


# DELETE
def delete_payment(request, id):
    payment = get_object_or_404(Payment, id=id)
    payment.delete()
    return redirect('payment_list')


# REPORT / PRINT
def payment_report(request):
    payments = Payment.objects.all()
    return render(request, 'payment_report.html', {'payments': payments})

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payment_list.html', {'payments': payments})

