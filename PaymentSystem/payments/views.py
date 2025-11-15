from django.shortcuts import render, redirect, get_object_or_404
from .models import Payment
from django.utils import timezone

# LIST ALL PAYMENTS
def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payment_list.html', {'payments': payments})

# ADD PAYMENT
def add_payment(request):
    if request.method == 'POST':
        card_number = request.POST.get('card_number')
        cardholder_name = request.POST.get('cardholder_name')
        amount = request.POST.get('amount')
        action = request.POST.get('action')  # deposit or withdraw
        date = request.POST.get('date') or timezone.now().date()  # Use today if empty

        Payment.objects.create(
            card_number=card_number,
            cardholder_name=cardholder_name,
            amount=amount,
            action=action,
            date=date
        )
        return redirect('payment_list')

    return render(request, 'add_payment.html')

# EDIT PAYMENT
def edit_payment(request, id):
    payment = get_object_or_404(Payment, id=id)

    if request.method == "POST":
        payment.card_number = request.POST.get("card_number")
        payment.cardholder_name = request.POST.get("cardholder_name")
        payment.amount = request.POST.get("amount")
        payment.date = request.POST.get("date")
        payment.action = request.POST.get("action")
        payment.save()

        return redirect('payment_list')

    return render(request, "edit_payment.html", {"payment": payment})

# DELETE PAYMENT
def delete_payment(request, id):
    payment = get_object_or_404(Payment, id=id)
    payment.delete()
    return redirect('payment_list')

# PAYMENT REPORT
def payment_report(request):
    payments = Payment.objects.all()
    return render(request, 'payment_report.html', {'payments': payments})
