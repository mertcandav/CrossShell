# Keywords

## var
Used to define variables, it is written before the variable definition. E.g:
```
var name = "Mertcan Davulcu";
```

<br>

## return
Used to return a value. It does not return any value if used alone. When used, it breaks the function. E.g:
```
func getWelcomeMsg -> {
    return "Hello, welcome to the CrossShell documentations!";
};
```
```
func example -> {
    return;
    print("Hi"); # This code is not processed!
};
```

<br>

## func
Used to define functions, it is written before the function definition. E.g:
```
func getNameInput -> {
    var input = input("Type your name: ");
    return input;
};
```

<br>

## delete
Deletes a displayed variable or function from memory. E.g:
```
var name = input("Type your name: ");
print("Hello " + name);
delete name;
```
```
func getNameInput -> {
    var input = input("Type your name: ");
    return input;
};

print(getNameInput());
delete getNameInput();
```

<br>

## if
Declare a new condition. E.g:
```
var name = input("Type your name: ");
if name != "" -> {
    print("Yellow", "Hello " + name)
};
```
