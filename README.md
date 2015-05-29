# pythuhn - huh? interpreter in Python

huh? is an esoteric programming language created by David Catt where the interpreter doesn't understand what you want it to do. Every file is a valid huh? program. The interpreter will do its best to understand the input, but will fail 99.99999999999% of the time. If it doesn't understand something, it will do nothing and simply express its confusion. It is implied that every command does something, we're just not sure what. [[source](https://esolangs.org/wiki/Huh%3F)]

I just ported the .NET interpreter to Python using .NET Reflector to figure out what it does. Since the language seems to be developed for Windows in mind, this application will likely only run properly, if at all, on Windows.

# Usage
```
python pythuhn [file]
```
