# exec

This module allows you to run a file.

Example usage:
```
exec MyNotes.txt
```
This code will open the MyNotes.txt file with the default application.
#
It is combined with the current location by default. If you want to write full path, you should use ``-merge`` parameter.
```
exec C:\Windows\cmd.exe -merge
```

### Parameters

+ ``-help``<br>
    Show help of module. This parameter can only be used alone.

+ ``-merge``<br>
    Disable merging with current location.
