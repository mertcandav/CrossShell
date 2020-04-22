# Parameters

Parameters are used in modules to use multiple functions of the command. They have a structure that you can be familiar with from many Shell.

Each parameter is reported with a dash. As:
```
sysinfo -all
```
#
If more than one parameter is desired to be declared, a space must be inserted. Short lines used without any spaces are included in the current parameter. As:<br>

| Paramter count: 2
```
sysinfo -cpu -cores
```
| Paramter count: 1
```
sysinfo -cpu-cores
```
#
A parameter cannot be specified more than once. Declaring a parameter multiple times will result in an error and / or command not working. As:
```
sysinfo -cpu -cpu
```
#
The space character cannot come after a parameter declaration. Causes the error and / or command not to work. As:
```
sysinfo - all
```
#
Declaring a parameter and not defining the parameter will result in errors and / or the command not running. As:
```
sysinfo -
```
