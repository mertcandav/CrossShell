# Function: trimRight

Deletes spaces on right sides of a string value.

Overloadings:
+ ``trimRight(value)``

Example use:
```
var name = trimRight(input("Type your name: "));
if name != "" ->> {
    print("Lime", "Hello \"" + name + '"');
};
delete name;

>CDBASEPATH

#>
OUTPUT

Type your name: <input> # "      Mertcan   "
Hello "      Mertcan"
------------------------
Type your name: <input> # "   "
<#
```
