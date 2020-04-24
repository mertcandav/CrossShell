<b>System Shell Integration</b>
---

Manage the use of the system's default shell/terminal.
#
``$`` Can be used to change the internal state of the System Shell.

Let your current location be this: ``M:\Desktop``<br>
It looks like this in CrossShell:
```
M:\Desktop>
```
'$' does not appear. This means that it is not internally active. The following command can be entered to activate:
```
$
```
It looks like this in CrossShell:
```
M:\Desktop>$
```
This means that it is now active. The same command can be used again to disable it.
#
If you want to use one-time activation, you can put '$' at the beginning of the command. For example, to use cmd's "dir" command in Windows, the following command can be written:
```
M:\Desktop> $dir
```
