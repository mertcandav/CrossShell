# Variables

You can keep and use variables and values. The keyword "var" is used to define variables. To change the value of an existing variable, it is enough to write its name.

A sample variable definition and changing its value:
```
var name = "Mertcan Davulcu";
print(name);
name = input("Type your name: ");
print(name);

#>
OUTPUT

Mertcan Davulcu
Type your name: <user input>
<user input>
<#
```

Value must be given when defining a variable.


Example codes:
```
var name = input("Type your name: ");
var surname = input("Yype your surname: ");
print("Hello " + name + " " + surname);

#>
OUTPUT

Type your name: <user input> # "Mertcan"
Type your surname: <user input> # "Davulcu"
Hello Mertcan Davulcu

<#

```
```
var name = "Hello " + input("Type your name: ");
print(name);

#>
OUTPUT

Type your name: <user input> # "Mertcan"
Hello Mertcan

<#

```

<br>

## See also
<a href="https://github.com/mertcandav/CrossShell/blob/master/docs/learn/scripts/definitions.md">Definitions</a>

