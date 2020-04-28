# cd

Allows you to manage the current location. It has the same function as what you know from most shell.

It is sufficient to use it alone to find out the current directory. as follows:
```
cd
```
#
To enter a directory, that directory must be in the directory you are in.

The following command must be processed to enter the directory:
```
cd Documents
```
This command enters the "Documents" directory. The name of the directory you want to enter must be in the "Documents" section.
#
If you want to go back to the previous directory, that is, if you want to go to the upper directory, you can use ``..``. As:
```
cd ..
```
#
To change to a different partition, the partition name can be written. As:<br>
Current location: ``M:\Development``
```
cd C:
```
or
```
cd C:\
```
New location: ``C:\``
#
Let's use it a little more mixed. Let's have a file structure like this:
+ M:\
    + Development
        + CrossShell
            + src
                + core
            + docs
            + anyDir1
        + apollo
        + MochaDB

The current position is: ``M:\Development\CrossShell``

Since ".." takes the top position, it functions the same in multiple uses. So if the following command is written:
```
cd ..\CrossShell
```
We come back to the same directory. The leading ``..`` takes us to the parent directory ``Development``. With the ``CrossShell`` that comes later, we enter the directory we are in again.

If we wrote the following command:
```
cd ../..
```
Now we are in this position: ``M:\``

Because with the ".." position shown in a row, we go up two directories.

Since we have regressed to the main directory of the disk, the ``..`` positions to be written after that will be dysfunctional.

We can use this command to access the "MochaDB" directory located in the "Development" directory:
```
cd Development/MochaDB
```
So this is our new position: ``M:\Development\MochaDB``

If we want to get out and go to the "src" directory in the "CrossShell" directory, we can use this command:
```
cd ../CrossShell/src
```
So this is our new position: ``M:\Development\CrossShell\src``
