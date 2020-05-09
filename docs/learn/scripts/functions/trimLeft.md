# Function: trimLeft

Deletes spaces on left sides of a string value.

Overloadings:
+ ``trimLeft(value)``

Example use:
```
var name = trimLeft(input("Type your name: "));
if name != "" ->> {
    print("Lime", "Hello " + name);
};
delete name;

>CDBASEPATH

#>
OUTPUT

Type your name: <input> # "      Mertcan"
Hello Mertcan
------------------------
Type your name: <input> # "   "
<#
```
