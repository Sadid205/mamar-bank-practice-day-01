from django.contrib import admin
from .models import Transaction
# Register your models here.
@admin.register(Transaction)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['account','amount','balance_after_transaction','transaction_type','loan_approve','is_bankrupt']

    def save_model(self,request,obj,form,change):
        if obj.loan_approve:
            obj.account.balance += obj.amount
            obj.balance_after_transaction = obj.account.balance
            obj.account.save()
        
        if 'is_bankrupt' in form.changed_data:
            Transaction.objects.all().update(is_bankrupt=obj.is_bankrupt)

        super().save_model(request,obj,form,change)
