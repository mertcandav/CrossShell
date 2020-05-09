# Function: trim

Deletes spaces on both sides of a string value.

Overloadings:
+ ``trim(value)``

Example use:
```
var name = trim(input("Type your name: "));
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
