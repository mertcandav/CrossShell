# Functions

Functions should be used to make your job easier.

Defining and calling functions:
```go
func getName -> {
    var input = input("Type your name: ");
    return input;
};

print("Hello" + getName());

#>
OUTPUT

Type your name: <User Input> # Mertcan
Hello Mertcan
<#
```
#
Local function calling:
```go
var message = -> {
    var input = input("Type your name: ");
    input = "Hello" + input;
    return input;
};

print(message);

#>
OUTPUT

Type your name: <User Input> # Mertcan
Hello Mertcan
<#
```
#
Function overriding:
```go
var name = "Undefined";

func printName -> {
    print(name);
}

printName();

name = input("Type your name: ");

printName();

printName -> {
    print("Hello " + name);
};

printName();

#>
OUTPUT

Undefined
Type your name: <User Input> # Mertcan
Mertcan
Hello Mertcan
<#
```

<br>

## See also
<a href="https://github.com/mertcandav/CrossShell/blob/master/docs/learn/scripts/definitions.md">Definitions</a>
