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

<b>If you use</b> ``$`` <b>at the beginning of the code, it is sent directly to the system terminal.

If you have permanently turned on the integration, the command is first processed in CrossShell, if the command is available in CrossShell, it is executed in CrossShell.

If it does not exist in CrossShell, it is sent to the system terminal. If the command is incorrect, the error you receive will belong to the system terminal, not CrossShell.

If you are using a common command on CrossShell and the system terminal and want the command to run on the system terminal, not CrossShell, you have to put ``$`` per command even if the integration is turned on.
</b>

#
If you want to use one-time activation, you can put '$' at the beginning of the command. For example, to use cmd's "dir" command in Windows, the following command can be written:
```
M:\Desktop> $dir
```
