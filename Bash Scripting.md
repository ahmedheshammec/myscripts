# Bash Scripting
Here's how we can start:

Introduction to Bash Scripting

1. **Basics of Bash:**
   - Bash is a command language interpreter for Unix-like systems.
   - It allows you to write scripts to automate complex, repetitive tasks.

2. **Creating Your First Script:**
   - Open your terminal.
   - Use a text editor to create a new file. For instance, type `nano myscript.sh`.
   - Add the following line to the file: `echo "Hello, World!"`. This script just prints "Hello, World!" to the console.
   - After editing the file in nano, you save it by pressing Ctrl + O, then Enter, and exit nano with Ctrl + X.

3. **Making the Script Executable:**
   - Save the file and exit the editor.
   - In the terminal, type `chmod +x myscript.sh` to make your script executable.
   - Run it by typing `./myscript.sh`.
### what is the difference between 
chmod +x myscript.sh
chmod a+x myscript.sh ? 
	1.	chmod +x myscript.sh:
	- This command makes myscript.sh executable by the user who owns the file.
	- If you are the owner of the file, this command allows you to execute it.
	- It doesn’t change the executable permissions for the group and others.
	2.	chmod a+x myscript.sh:
	- a stands for “all”, meaning all users.
	- This command adds executable permissions to the file for everyone (user, group, and others).
	- It’s a more inclusive permission setting, ensuring that any user on the system can execute the script.


4. **Basic Structure of a Bash Script:**
   - The first line of a bash script is usually `#!/bin/bash` which tells the system to execute the script in a bash shell.
   - Comments are added using `#`.

First Concepts to Learn

1. **Variables:**
   - Assigning values to variables: `varname=value`.
   - Accessing variable values: `$varname`.

2. **Control Structures:**
   - `if` statements, `for` loops, `while` loops, `case` statements.

3. **Positional Parameters:**
   - `$0, $1, $2, ...` represent the script name and the arguments passed to it.

4. **Reading User Input:**
   - `read` command.

5. **Basic Commands:**
   - `echo`, `printf` for output.
   - `grep`, `awk`, `sed` for text processing.

Next Steps

- **Practice:** Try modifying the script to do something else, like listing files in a directory.
- **Experiment:** The best way to learn scripting is by doing. Try to automate a simple task you do daily.
- **Study Examples:** Look at existing scripts to see how they work.
- **Resources:** There are many free resources online to learn bash scripting.

<!-- /////////////////////////////////// -->

### 1. Creating Variables
To create a variable, you just assign a value to a name. In Bash, you don't need to declare a variable's type. Here's an example:

```bash
my_name="Ahmed"
my_age=25
```

In this example, `my_name` is a string variable containing `"Ahmed"`, and `my_age` is an integer variable containing `25`.

### 2. Using Variables
To use a variable, prefix it with a `$`. Here's how to echo them:

```bash
echo "My name is $my_name and I am $my_age years old."
```

This will output: `My name is Ahmed and I am 25 years old.`

### 3. Read-Only Variables
You can make a variable read-only by using the `readonly` command. This means you can't change its value later in the script.

```bash
readonly my_constant="This value cannot change"
```

### 4. Command Substitution
You can store the output of a command in a variable using command substitution.

```bash
current_date=$(date)
echo "Today is $current_date"
```

This will display the current date and time.

### 5. Arithmetic Operations
For arithmetic operations, you can use the `$((expression))` syntax.

```bash
a=5
b=3
sum=$((a + b))
echo "The sum is $sum"
```

This will output: `The sum is 8.`

### 6. Environment Variables
Environment variables are available system-wide, not just in your script. For instance, `$HOME` contains your home directory path.

```bash
echo "Your home directory is $HOME"
```

### 7. Updating Variables
You can update the value of a variable by simply reassigning it.

```bash
my_city="Cairo"
echo "City: $my_city"

# Changing the value
my_city="Alexandria"
echo "Updated City: $my_city"
```

This will first output "City: Cairo" and then "Updated City: Alexandria."

These examples cover the basics of variable usage in Bash scripting. You can use variables for various purposes like storing user input, temporary data, file paths, and configuration settings.
<!-- so echo is like print in python ?  -->
Yes, exactly! In Bash scripting, `echo` is similar to `print` in Python. It's used to display text or the value of variables to the standard output, which is usually the terminal screen. 

Here are some examples to illustrate this:

1. **Printing Text:**
   ```bash
   echo "Hello, world!"
   ```
   This will simply print "Hello, world!" to the terminal.

2. **Printing Variables:**
   ```bash
   my_var="Welcome to Bash scripting"
   echo $my_var
   ```
   This will print the contents of `my_var`, which is "Welcome to Bash scripting".

3. **Combining Text and Variables:**
   ```bash
   user="Ahmed"
   echo "Hello, $user!"
   ```
   This will print "Hello, Ahmed!" to the terminal.

4. **Using Options:**
   - `echo -n`: Prints text without the trailing newline.
   - `echo -e`: Enables interpretation of backslash escapes (like `\n` for a new line).

5. **Echo with Special Characters:**
   ```bash
   echo -e "Line1\nLine2"
   ```
   This uses `-e` to interpret `\n` as a newline, printing "Line1" and "Line2" on separate lines.

In summary, `echo` is a fundamental command in Bash scripting for displaying output, similar to how `print` is used in Python.

<!-- /////////////////////////////////// -->

### If statements 
in Bash are used for making decisions in scripts based on conditions. Here are some examples to help you understand how they work:

### Basic Syntax

```bash
if [ condition ]; then
  # commands if the condition is true
fi
```

### Example 1: Checking Numbers

```bash
num=10
if [ $num -gt 5 ]; then
  echo "The number is greater than 5"
fi
```
This script checks if `num` is greater than 5. If it is, it prints a message.

### Example 2: Using Else

```bash
num=4
if [ $num -gt 5 ]; then
  echo "The number is greater than 5"
else
  echo "The number is less than or equal to 5"
fi
```
This adds an `else` clause to handle the case where the condition is not met.

### Example 3: Else If (elif)

```bash
num=5
if [ $num -gt 5 ]; then
  echo "The number is greater than 5"
elif [ $num -eq 5 ]; then
  echo "The number is equal to 5"
else
  echo "The number is less than 5"
fi
```
`elif` lets you add more conditions.

### Example 4: String Comparison

```bash
name="Ahmed"
if [ "$name" == "Ahmed" ]; then
  echo "Hello, Ahmed!"
fi
```
This checks if the variable `name` is equal to the string "Ahmed".

### Example 5: File Checks

```bash
filename="example.txt"
if [ -e $filename ]; then
  echo "$filename exists."
fi
```
This checks if a file named `example.txt` exists.

### Notes on Syntax

- Spaces around `[` and `]` are required.
- For string comparisons, make sure to quote variables to handle spaces correctly.
- `-gt`, `-lt`, `-eq` are used for numerical comparisons (greater than, less than, equal to).
- `-e`, `-d`, `-f`, etc., are used for file checks (exists, is directory, is file).

If statements are essential in Bash for controlling the flow of the script based on different conditions.

<!-- /////////////////////////////////// -->

### For loops 
in Bash scripting are used to execute a series of commands repeatedly for each item in a list or range. Here are some examples to demonstrate their usage:

### Basic Syntax

```bash
for variable in list
do
  # commands to execute for each item in the list
done
```

### Example 1: Looping Over a List of Values

```bash
for name in Alice Bob Charlie
do
  echo "Hello, $name!"
done
```
This script prints a greeting for each name in the list.

### Example 2: Looping Over a Range of Numbers

Using brace expansion:

```bash
for number in {1..5}
do
  echo "Number is $number"
done
```
This prints numbers from 1 to 5.

### Example 3: Looping Over Output of a Command

```bash
for file in $(ls)
do
  echo "File: $file"
done
```
This lists all files in the current directory.

### Example 4: Looping Over a Sequence with Step

```bash
for i in {0..10..2}
do
  echo "Count: $i"
done
```
This prints even numbers from 0 to 10.

### Example 5: C-Style For Loop

```bash
for ((i=0; i<=5; i++))
do
  echo "Number: $i"
done
```
This is similar to the for loop in languages like C or Java.

### Example 6: Looping Through Files with a Specific Extension

```bash
for img in *.jpg
do
  echo "Processing $img"
  # some commands to process the image
done
```
This script will process each `.jpg` file in the current directory.

### Notes:

- It's essential to understand how word splitting and globbing work in Bash to effectively use for loops.
- Always quote your variables when possible to avoid issues with filenames or strings with spaces.

For loops are very powerful in shell scripting, allowing you to automate repetitive tasks efficiently.

<!-- /////////////////////////////////// -->

### While loops 
in Bash scripting are used to repeatedly execute a block of commands as long as a certain condition is true. They're useful for tasks that need to continue until a particular state is reached or changed. Here's a basic syntax and some examples to illustrate their usage:

### Basic Syntax

```bash
while [ condition ]
do
  # commands to execute while the condition is true
done
```

### Example 1: Basic While Loop

```bash
counter=1
while [ $counter -le 5 ]
do
  echo "Counter: $counter"
  ((counter++))
done
```
This script prints numbers from 1 to 5, incrementing `counter` in each iteration.

### Example 2: Reading Lines from a File

```bash
while read line
do
  echo "Line: $line"
done < input.txt
```
This reads and prints each line from `input.txt`.

### Example 3: Waiting for a File to Appear

```bash
while [ ! -f /tmp/myfile ]
do
  echo "Waiting for file..."
  sleep 1
done
```
This waits for a file named `myfile` to appear in the `/tmp` directory, checking every second.

### Example 4: Infinite Loop

```bash
while true
do
  echo "Press [CTRL+C] to stop.."
  sleep 1
done
```
This creates an infinite loop that can be stopped with Ctrl+C.

### Example 5: Loop Until a Command Succeeds

```bash
until ping -c 1 google.com
do
  echo "Waiting for network..."
  sleep 1
done
```
This keeps trying to ping `google.com` until it succeeds.

### Notes:

- The condition in the while loop is evaluated before each iteration. If the condition is false at the start, the commands inside the loop won't be executed.
- Make sure the condition in a while loop eventually becomes false; otherwise, you'll create an infinite loop.
- `((counter++))` is an arithmetic operation that increments the value of `counter`.
- In shell scripting, `0` is often treated as `true` (especially in return statuses), and non-zero values as `false`. This might be counterintuitive if you're used to other programming languages.

While loops are particularly useful when you need to wait for a certain condition or perform a task a variable number of times until a specific state is achieved.

<!-- /////////////////////////////////// -->

### Case statements 
in Bash are used for making decisions based on specific values of a variable. They are similar to the switch-case statements in other programming languages. Here's an example to illustrate how to use them:

```bash
#!/bin/bash

echo "Enter a number between 1 and 3:"
read number

case $number in
    1)
        echo "You entered number 1"
        ;;
    2)
        echo "You entered number 2"
        ;;
    3)
        echo "You entered number 3"
        ;;
    *)
        echo "You did not enter a number between 1 and 3"
        ;;
esac
```

In this script:

- The `case` statement starts with the variable (`$number`) we're checking.
- Each pattern to match (`1`, `2`, `3`) is followed by a right parenthesis.
- The `;;` syntax ends the action for each particular pattern.
- The `*` pattern serves as a default case for when no other patterns match.
- The `esac` keyword (which is `case` spelled backwards) ends the case statement.

This script will prompt the user to enter a number, and then use a case statement to provide a response based on the number entered. If the number isn't 1, 2, or 3, it falls to the default case.

<!-- /////////////////////////////////// -->

### Positional parameters 
in Bash are variables that hold the arguments passed to a script or a function. They are named numerically: `$1`, `$2`, `$3`, and so on. `$0` represents the script's name itself. This is useful for writing scripts that can accept different input values when executed.

Here's a simple example of a script using positional parameters:

```bash
#!/bin/bash

echo "Script Name: $0"
echo "First Argument: $1"
echo "Second Argument: $2"
echo "Third Argument: $3"
```

Let's say you save this script as `myscript.sh`. You can run it with arguments like this:

```bash
bash myscript.sh apple orange banana
```

The output would be:

```
Script Name: myscript.sh
First Argument: apple
Second Argument: orange
Third Argument: banana
```

In this case:
- `$0` is the script's name (`myscript.sh`).
- `$1`, `$2`, and `$3` are the first, second, and third arguments provided (`apple`, `orange`, `banana`).

Additionally, you can use `$#` to get the number of positional parameters (not counting `$0`), and `$@` or `$*` to get all the positional parameters as a list.

:: **Practical Exaple** ::
if we have a folder that is already added to the path variables in your system and this folder contains a bunch of bash scripts; then we can make a little trick to run this script from anywhere without the need to copy the script file to location you want
we will add this simple code in the start of the script: 
```bash
location=$1
cd "$location"
```
so now all we have to do is to make the script executable just for one time in the script folder and when we run the script from anywhere in the drive we just give it the location which we want to execute the script from and the script will automatically jump into the directory you entered and execute the rest of the script
```
convert.sh 'user/document/folder/'
```
this is basically saying execute the convert.sh script in the directory `user/document/folder/`

what is even more powerful is you can make variable from the output of a command 
```bash 
user=$(whoami)
```
and we can use this user variblae later in the script
```bash
echo "You are currently logged in as $user"
```
<!-- /////////////////////////////////// -->

### how to run bash script from anywhere on the system ? 
To run a Bash script from anywhere on your system, you'll need to do two things:

1. **Make the script executable**:
   Ensure your script is executable by using the `chmod` command. For example:
   ```bash
   chmod +x myscript.sh
   ```

2. **Place the script in a directory that's in your PATH**:
   The PATH environment variable contains a list of directories that the system searches for executable files. By placing your script in one of these directories, you can run it from anywhere.

   Common directories in the PATH include `/usr/local/bin` or `~/bin` (if this directory is added to your PATH). To move your script to one of these directories, you can use:
   ```bash
   mv myscript.sh /usr/local/bin
   ```
   Or, if you prefer to keep it in a custom directory, you can add that directory to your PATH.

   To add a custom directory (e.g., `~/my_scripts`) to your PATH, you can add this line to your `.bash_profile`, `.bashrc`, or `.zshrc` (depending on your shell and setup):
   ```bash
   export PATH=$PATH:~/my_scripts
   ```
   After adding the directory to your PATH, you'll need to either restart your terminal or source the profile file with `source ~/.bash_profile` (or the respective file you've edited).

Once you've done this, you should be able to run your script from anywhere by simply typing its name (without the `.sh` extension if you prefer). Make sure the script's first line is the shebang `#!/bin/bash` to indicate that it should be run with Bash.

### if i made the script executable and moved or edited the script file, it will remain executable or not ? 
If you make a script executable and then move it, the executable permission will typically be retained. However, if you edit the script, especially with some text editors or IDEs, it might change the permissions. It largely depends on how the editor handles file saving. Some editors create a new file and replace the old one, which can sometimes reset the permissions.

To be on the safe side, after editing a script, you can quickly check its permissions with:

```bash
ls -l myscript.sh
```

If the executable permission is lost, you'll see something like `-rw-r--r--` at the start of the line. If the executable permission is still there, it will show as `-rwxr-xr-x` or similar (with `x` indicating executable permissions). If you need to make it executable again, you can use:

```bash
chmod +x myscript.sh
```

This command will reinstate the executable permission.

### what does the -l stand for in ls -l myscript.sh
The `-l` option in the `ls` command stands for "long format." When you use `ls -l`, it displays a detailed listing of the file(s) attributes. Here's what each part of the output represents when you run `ls -l myscript.sh`:

1. **File Type and Permissions**: This is a string of characters at the start, like `-rw-r--r--`. The first character indicates the file type (e.g., `-` for regular files, `d` for directories). The next nine characters show the permissions in three sets of three: the first set for the owner, the second for the group, and the third for others. Each set can have `r` (read), `w` (write), and `x` (execute) permissions.

2. **Number of Links**: This number shows how many hard links there are to the file.

3. **Owner**: The username of the file's owner.

4. **Group**: The group that the file belongs to.

5. **Size**: The size of the file in bytes.

6. **Modification Time**: The last time the file was modified.

7. **File Name**: The name of the file.

For example, if you see `-rw-r--r-- 1 user group 4096 Apr 1 12:00 myscript.sh`, it means:

- It's a regular file (`-`).
- It has read and write permissions for the owner (`rw-`), read-only permissions for the group (`r--`), and read-only for others (`r--`).
- There is 1 hard link to this file.
- The owner is `user`, and the group is `group`.
- The file size is 4096 bytes.
- The file was last modified on April 1 at 12:00.
- The file's name is `myscript.sh`.








