# Comment Lines

Comment lines are ignored. You can use it if you need to write a description, article or anything. You can also write anything you don't want reflected in the code.

Single line comment lines are for that line only. The comment line is ignored from where it is marked until the end of the line. One-line comments are indicated by ``#``. E.g:
```
# Mertcan Davulcu
# Copyright 2020

echo "Hello World"; # echo "Test"

# Output: Hello World
```
#
If you need to comment in multiple lines, using single line comments can be tortured. Anything you write between ``#>`` and ``<#`` to comment on multiple lines is ignored. E.g:
```
#>
MIT License

Copyright (c) 2020 Mertcan Davulcu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
<#

echo "Hello World"

# Output: Hello World
```
