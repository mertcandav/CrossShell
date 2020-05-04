# Function: print

Prints the given value on the screen.

Overloadings:
+ ``input(msg)``
+ ``input(colorName, msg)``

Example use:
```
print("My name is \"Mertcan Davulcu\"");

# Output: My name is "Mertcan Davulcu"
```

If only one input will be written in color, you do not need to do code pollution with ``setForeColor`` function. Type the color name in the first parameter and write your message in the second parameter, it will be printed in the color you gave the message and then return to the default color.

Example use:
```
print("Yellow", "My name is \"Mertcan Davulcu\"");
```
