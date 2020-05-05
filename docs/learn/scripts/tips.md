# Tips

When the script is run, the location of CrossShell is set to the directory where the script file is located. If you want to run the commands in your own directory, not the directory where the script file is, add ``>CDBASEPATH`` command at the beginning of the script.
#
If you have run the script with the script command from CrossShell and want to move it from your old location after the script is finished, add ``>CDBASEPATH`` command at the end.
#
If you use ``return`` in the normal position (outside the function) without using the ``>BREAK`` command, you will get the same function as ``>BREAK``.