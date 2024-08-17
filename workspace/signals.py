from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from marketplace.models import UserModel,Nft
from django.contrib.auth.models import User


@receiver(post_save,sender=User)
def post_save_user(sender, instance, created, *args, **kwargs):

    if created:
        UserModel.objects.create(user=instance)



# @receiver(post_save,sender=Nft)
# def post_save_user(sender, instance, created, *args, **kwargs):

#     if created:
#         _ = UserModel.objects.get(user=instance.created_by.user)

#         _.created += 1
#         _.balans += instance.prise
#         _.save()

#         _ = UserModel.objects.all()