# Conditions

You can direct algorithms with conditions. They have the same function as other scripting and programming languages.

Defining conditions:
```go
var name = input("Type your name: ");

if name != "" ->> {
    print("Hello " + name);
};

#>
OUTPUT

Type your name: <User Input> # Mertcan
Hello Mertcan
-----
Type your name: <User Input> #
<#
```

After the condition is declared with the ``if`` keyword, the function of the condition is defined with the local function.

> The functions of the conditions are indicated by ``->>`` and not by ``->``.

<br>

#

+ ``==``<br>
Equal.

+ ``!=``<br>
Not equal.

+ ``>``<br>
Bigger.

+ ``<``<br>
Lower.

+ ``>=``<br>
Bigger or equal.

+ ``<=``<br>
Lower or equal.

#

## See also
<a href="https://github.com/mertcandav/CrossShell/blob/master/docs/learn/scripts/definitions.md">Definitions</a><br>
<a href="https://github.com/mertcandav/CrossShell/blob/master/docs/learn/scripts/functions.md">Functions</a>
