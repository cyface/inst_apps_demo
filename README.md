Demo of Dynamic INSTALLED_APPS
------------------------------

This app demonstrates dynamically setting the INSTALLED APPS in settings.

Often this will be because there are environment-specific settings files that need to add or remove certain apps (e.g. prod logging, or redis)

PyCharm can't detect the modification of the INSTALLED_APPS setting, and only looks at the last time it was set.
