from django.shortcuts import render, redirect, get_object_or_404
from .models import Payment

# LIST + ADD FORM TOGETHER
def payment_list(request):
    payments = Payment.objects.all()

    if request.method == "POST":  # this part acts as add_payment
        Payment.objects.create(
            cardholder_name=request.POST['cardholder_name'],
            card_number=request.POST['card_number'],
            amount=request.POST['amount'],
            reference_number=request.POST['reference_number'],
            status="Processed"
        )
        return redirect('payment_list')

    return render(request, 'payment_list.html', {'payments': payments})


# ADD PAYMENT (separate function if needed by your URLs)
def add_payment(request):
    if request.method == "POST":
        Payment.objects.create(
            cardholder_name=request.POST['cardholder_name'],
            card_number=request.POST['card_number'],
            amount=request.POST['amount'],
            reference_number=request.POST['reference_number'],
            status="Processed"
        )
        return redirect('payment_list')

    return render(request, 'add_payment.html')
    

# EDIT
def edit_payment(request, id):
    payment = get_object_or_404(Payment, id=id)

    if request.method == "POST":
        payment.cardholder_name = request.POST['cardholder_name']
        payment.card_number = request.POST['card_number']
        payment.amount = request.POST['amount']
        payment.reference_number = request.POST['reference_number']
        payment.status = request.POST['status']
        payment.save()
        return redirect('payment_list')

    return render(request, 'edit_payment.html', {'payment': payment})


# DELETE
def delete_payment(request, id):
    payment = get_object_or_404(Payment, id=id)
    payment.delete()
    return redirect('payment_list')


# REPORT / PRINT
def payment_report(request):
    payments = Payment.objects.all()
    return render(request, 'payment_report.html', {'payments': payments})
