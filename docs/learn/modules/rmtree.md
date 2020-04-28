# rmdir

This module is a module that allows you to delete directories and childs.

To delete a directory by typing its name, you must type its name in ``string`` type. As:
```
rmdir "MyDir"
```
This command will delete the directory named "MyDir".
#
You want to delete multiple files but this is not supported, there is a way to do it, don't worry. With the ``-rgx`` parameter, you can delete using regular expression. For example, this command is enough to delete all directories that start with ``MyDir``:
```
rmdir "MyDir*" -rgx
```
When you enable regular expression queries, you can delete with regular expression patterns like the above command.

### Parameters

+ ``-help``<br>
    Show help of module. This parameter can only be used alone.

+ ``-rgx``<br>
    Use regular expressions.
    