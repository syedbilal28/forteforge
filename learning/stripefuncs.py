import stripe
from stripe.api_resources import subscription
from .models import Profile

def CreateCustomer(user):
    customer=stripe.Customer.create(
            email=user.email,
            name=user.get_full_name(),
            metadata={
                'user_id':user.pk,
                'username':user.username
            },
            description="UnoStartup Customer",
            )
    profile=Profile.objects.get(user=user)
    profile.stripe_customer_id=customer.id
    profile.save()
    return customer
    
def PurchaseProduct(profile,product_stripe_id):
    currency="eur"
    email=profile.user.email
    items=[
        {
            "parent":product_stripe_id
        }
    ]
    
def CreatePaymentMethod(card,cvc,exp_month,exp_year):
    Payment_Method=stripe.PaymentMethod.create(
                type="card",
                card={
                    "number":card,
                    "cvc":cvc,
                    'exp_month':exp_month,
                    'exp_year':exp_year
                }
            )
    return Payment_Method   

def CreateSubscription(cus_id,package):
    subscription=stripe.Subscription.create(
    customer=cus_id,
    items=[
        {"plan": package},
    ],
    )

def AttachPaymentMethod(customer_id,payment_method_id):
    stripe.PaymentMethod.attach(
        payment_method_id,
        customer=customer_id,
    )
    
def CreateInvoice(customer_id):
    stripe.InvoiceItem.create(
        customer = customer_id,
        price = "price_1IzjWCIvRYhh9p0mLe7dlN84",
    )

    invoice = stripe.Invoice.create(
        customer = customer_id,
        auto_advance = False # auto-finalize this draft after ~1 hour
    )

    stripe.Invoice.finalize_invoice(invoice.id)

def CancelSubscription(subscription_id):
    stripe.Subscription.delete(subscription_id)
    return True