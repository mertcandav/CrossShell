# Operators

## @
Commands written alone appear as inputs on command lines. You can add ``@'' to the codes to be processed directly without seeing which code is entered. E.g:
```
echo "Hello World"

# Runtime:
    CS C:\Users\docs\Desktop> echo "Hello World"
    Hello World
```
```
@echo "Hello World"

# Runtime:
    Hello World
```

<br>

## >
This command indicates that there are commands specific to CrossShell Scripts. It is put at the beginning of special commands. E.g:
```
echo "Hello World"; >BREAK
```

<br>

## =
It is used in definitions and assignments. E.g:
```
var name = input("Type your name: ");
name = "Hello " + name;
```

<br>

## <-
Force the terminal command to cry value with the value handler. This way variables etc. You can use. E.g:
```
var name = input("Type your name: ");
@echo <- "\"Hello " + name + "\"";

#>
OUTPUT

Type your name: <user input> # Mertcan
Hello Mertcan
<#
```
