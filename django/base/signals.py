from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.db.models.signals import pre_init, post_init, pre_save, post_save, pre_delete, post_delete, pre_migrate, post_migrate
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created

from django.contrib.auth.models import User
from django.dispatch import Signal, receiver



# step 1 : to establish connection between sender and receiver add this file in ready method of apps
        # def ready(self):
        # import base.signals 

# step 2 : create receiver function which tells us what to do when signal passes from sender

# step 3 : make connection of signal between sender and receiver using following method
# `````````1 . Add manually using signal   OR
# `````````2 . using receiver @decorator

##################################################################################################

# built in auth signals ---->

'''Signal 1 : user_logged_in (this will trigger once user logged in)'''

# method 2 : using decorator
@receiver(sender=User, signal=user_logged_in)
def login_receiver(sender, request, user, **kwargs):
    print("login receiver activated............")

# mthod 1 : manually adding using signal
# user_logged_in.connect(sender=User, receiver=login_receiver)


'''Signal 2 : user_logged_out (this will trigger once user logged out)'''


@receiver(sender=User, signal=user_logged_out)
def logout_receiver(sender, request, user, **kwargs):
    print("logout receiver activated............")

# user_logged_out.connect(sender=User, receiver=logout_receiver)


'''Signal 3 : user_login_failed  (this will trigger with login fail)''' # (sender not required in this while connecting)


@receiver(signal=user_login_failed) 
def login_failed_receiver(sender, credentials, request, **kwargs):
    print("login failed receiver activated............")

# user_login_failed.connect(receiver=login_failed_receiver)

##################################################################################################

# built in model signals ---->

'''Signal 1 : pre_save (this will trigger before we save any model(User model in this example))'''

@receiver(sender=User, signal=pre_save)
def pre_save_receiver(sender, instance, **kwargs):
    print("prev save receiver activated............")

# pre_save.connect(sender=User, receiver=pre_save_receiver)


'''Signal 2 : post_save (this will trigger after we save any model(User model in this example))'''

@receiver(sender=User, signal=post_save)
def post_save_receiver(sender, instance, created, **kwargs):
    # created true -> new record created, created false -> old record updated
    if created:
        print("post save receiver activated with created............")
    else:
        print("post save receiver activated with updated............")

# post_save.connect(sender=User, receiver=post_save_receiver)


'''Signal 3 : pre_delete (this will trigger before we delete any model(User model in this example))'''

@receiver(sender=User, signal=pre_delete)
def pre_delete_receiver(sender, instance, **kwargs):
    print("pre delete receiver activated............")

# pre_delete.connect(sender=User, receiver=pre_delete_receiver)


'''Signal 4 : post_delete (this will trigger after we delete any model(User model in this example))'''

@receiver(sender=User, signal=post_delete)
def post_delete_receiver(sender, instance, **kwargs):
    print("post delete receiver activated............")

# post_delete.connect(sender=User, receiver=post_delete_receiver)


'''Signal 5 : pre_init (this will trigger before perform any activity -> like ctrl + s)'''

@receiver(sender=User, signal=pre_init)
def pre_init_receiver(sender, *args, **kwargs):
    print("pre init receiver activated............")

# pre_init.connect(sender=User, receiver=pre_init_receiver)


'''Signal 6 : post_init (this will trigger after perform any activity -> like ctrl + s)'''

@receiver(sender=User, signal=post_init)
def post_init_receiver(sender, *args, **kwargs):
    print("post init receiver activated............")

# post_init.connect(sender=User, receiver=post_init_receiver)


'''Signal  7 : pre_migrate (this will trigger before we run migrate on all models in django)'''

@receiver(signal=pre_migrate)
def pre_migrate_receiver(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print("pre migrate receiver activated............")

# pre_migrate.connect(receiver=pre_migrate_receiver)


'''Signal  8 : post_migrate (this will trigger after we run migrate on all models in django)'''

@receiver(signal=post_migrate)
def post_migrate_receiver(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print("post migrate receiver activated............")

# pre_migrate.connect(receiver=post_migrate_receiver)

##################################################################################################

# built in request-response signals ---->

'''Signal 1 : request_started (this will trigger when we ask django to return httpresponse or template)'''

@receiver(signal=request_started)
def request_started_receiver(sender, environ, **kwargs):
    print("request started receiver activated............")

# request_started.connect(receiver=request_started_receiver)


'''Signal 2 : request_finished (this will trigger after django returning httpresponse or template)'''

@receiver(signal=request_finished)
def request_finished_receiver(sender, **kwargs):
    print("request finished receiver activated............")

# request_finished.connect(receiver=request_finished_receiver)


'''Signal 3 : got_request_exception (this will trigger when we ask django to return invalid httpresponse or template)'''
# this will get used when we see django error page while accessing template

@receiver(signal=got_request_exception)
def got_request_exception_receiver(sender, request, **kwargs):
    print("got request exception receiver activated............")

# got_request_exception.connect(receiver=got_request_exception_receiver)


##################################################################################################

# built in database wrappers signals ---->

'''Signal 1 : connection_created (this will trigger when databse connection initiated)'''
# for example while running -> python manage.py runsever

@receiver(connection_created)
def connection_created_receiver(sender, connection, **kwargs):
    print("connection created receiver activated............")

# connection_created.connect(connection_created_receiver)


##################################################################################################

# Custom signal -->

# step 1 : create signal using Signal class
# step 2 : attach that signal in code where you want to generate for example in views.py
        #   def home(request):
        #     custom_signal.send(sender=None)
        #     context = {}
        #     return render(request, 'base/home.html', context)

# step 3 : create receiver function and attach signal using any one method as above for built in signal


custom_signal = Signal()

@receiver(signal=custom_signal, sender=None)
def custom_signal_receiver(sender, **kwargs):
    print("custom signal activated...........")

# custom_signal.connect(sender=None, receiver=custom_signal_receiver)