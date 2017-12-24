from django.contrib import admin

from .models import singup, guess, search_history, logs, config

admin.site.register(singup)
admin.site.register(guess)
admin.site.register(search_history)
admin.site.register(logs)
admin.site.register(config)