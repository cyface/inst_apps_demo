Demo of Dynamic INSTALLED_APPS
------------------------------

This app demonstrates dynamically setting the INSTALLED APPS in settings.

Often this will be because there are environment-specific settings files that need to add or remove certain apps (e.g. prod logging, or redis)

PyCharm can't detect the modification of the INSTALLED_APPS setting, and only looks at the last time it was set.

PyCharm works fine with the newer list syntax for INSTALLED_APPS (e.g. [ ] rather than the older tuple ( ) style).

But if it's defined as the older tuple style, it causes PyCharm to be unable to detect the contents of INSTALLED_APPS.

This screenshot shows the taglibs showing as unrecognized when the settings are specified as a tuple and then changed later:

![Unrecognized Taglib](https://github.com/cyface/inst_apps_demo/raw/master/unrecognized_taglibs.png "Unrecognized Taglib")

