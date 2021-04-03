from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'billing/home.html')

@login_required(login_url='account_login')
def make_payment(request):
    return render(request, 'billing/makepayment.html')

@login_required(login_url='account_login')
def bill_overview(request):
    return render(request, 'billing/bill_overview.html')

@login_required(login_url='account_login')
def payment_report(request):
    return render(request, 'billing/payment_report.html')


@login_required
def add_customer(request):
    # Show most common tags
    try:
        if request.method == 'POST':
            form = AddCustomerForm(request.POST, request.FILES)
            if form.is_valid():
                newcustomer = form.save(commit=False)
                newcustomer.slug = slugify(newbook.title)
                newcustomer.seller = curr_seller
                newcustomer.save()
                form.save_m2m()
                messages.info(request, "The customer was added!")
                return redirect("home")
            else:
                print(form.errors)
                messages.warning(request, "The customer was not added")
                return redirect("/add-customer")

        else:
            form = AddCustomerForm()
            context = {
                'form': form,
            }
            return render(request, 'billing/add_customer.html', context)
    except:
        messages.warning(request, "Either the data was invalid or you don't have a sellers account!")
        return redirect('/add-book')
