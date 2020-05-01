# del

This module allows you to delete files.

To delete a file by typing its name, as:
```
del MyNotes.txt
```
This command will delete the file named "MyNotes.txt".
#
You want to delete multiple files but this is not supported, there is a way to do it, don't worry. With the ``-rgx`` parameter, you can delete using regular expression. For example, this command is enough to delete all files that start with ``MyNotes``:
```
del MyNotes* -rgx
```
When you enable regular expression queries, you can delete with regular expression patterns like the above command.

### Parameters

+ ``-help``<br>
    Show help of module. This parameter can only be used alone.

+ ``-rgx``<br>
    Use regular expressions.
    