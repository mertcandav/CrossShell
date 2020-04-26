# pause

This module stops inputting commands until you press the ``enter`` key.

If used alone, as:
```
pause
```
It will wait for ``enter`` input with the following output: ``Press enter for continue...``
#
If a special message is desired to be given, it must be specified with "string", as follows:
```
pause "Enter for continue:"
```
Now the output will look like this: ``Enter for continue:``