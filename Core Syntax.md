# 🔍 Python Core Syntax and Magic Methods

Now it’s time to get familiar with Python core syntax expressions and their corresponding magic methods. The following tables will help you in situations where you'd like to implement a custom method for a Python core operation, as the tables enumerate the most popular operators and functions that have magic method counterparts.

Treat it as a universal reference list, unrelated to any specific data type.

---

## 🧮 Comparison Methods

| Function or Operator | Magic Method             | Purpose                                |
|----------------------|--------------------------|----------------------------------------|
| `==`                 | `__eq__(self, other)`    | Equality operator                      |
| `!=`                 | `__ne__(self, other)`    | Inequality operator                    |
| `<`                  | `__lt__(self, other)`    | Less-than operator                     |
| `>`                  | `__gt__(self, other)`    | Greater-than operator                  |
| `<=`                 | `__le__(self, other)`    | Less-than-or-equal-to operator         |
| `>=`                 | `__ge__(self, other)`    | Greater-than-or-equal-to operator      |

---

## ➕ Numeric Methods

### 🔹 Unary Operators and Functions

| Function or Operator | Magic Method             | Purpose                                |
|----------------------|--------------------------|----------------------------------------|
| `+`                  | `__pos__(self)`          | Unary positive (`a = +b`)              |
| `-`                  | `__neg__(self)`          | Unary negative (`a = -b`)              |
| `abs()`              | `__abs__(self)`          | Behavior for `abs()`                   |
| `round(a, b)`        | `__round__(self, b)`     | Behavior for `round()`                 |

### 🔹 Common Binary Operators and Functions

| Function or Operator | Magic Method                | Purpose                             |
|----------------------|-----------------------------|-------------------------------------|
| `+`                  | `__add__(self, other)`      | Addition operator                   |
| `-`                  | `__sub__(self, other)`      | Subtraction operator                |
| `*`                  | `__mul__(self, other)`      | Multiplication operator             |
| `//`                 | `__floordiv__(self, other)` | Integer division operator           |
| `/`                  | `__div__(self, other)`      | Division operator                   |
| `%`                  | `__mod__(self, other)`      | Modulo operator                     |
| `**`                 | `__pow__(self, other)`      | Exponential (power) operator        |

---

## 🧩 Augmented Operators and Functions

> By augmented assignment we understand operations like `a += 20`, which combine an operation and assignment.

| Function or Operator | Magic Method                 | Purpose                                     |
|----------------------|------------------------------|---------------------------------------------|
| `+=`                 | `__iadd__(self, other)`      | Addition and assignment                     |
| `-=`                 | `__isub__(self, other)`      | Subtraction and assignment                  |
| `*=`                 | `__imul__(self, other)`      | Multiplication and assignment               |
| `//=`                | `__ifloordiv__(self, other)` | Integer division and assignment             |
| `/=`                 | `__idiv__(self, other)`      | Division and assignment                     |
| `%=`                 | `__imod__(self, other)`      | Modulo and assignment                       |
| `**=`                | `__ipow__(self, other)`      | Exponential (power) and assignment          |

---

## 🔄 Type Conversion Methods

Python offers a set of methods responsible for the conversion of built-in data types.

| Function     | Magic Method              | Purpose                                                         |
|--------------|---------------------------|-----------------------------------------------------------------|
| `int()`      | `__int__(self)`           | Conversion to integer type                                      |
| `float()`    | `__float__(self)`         | Conversion to float type                                        |
| `oct()`      | `__oct__(self)`           | Conversion to string containing an octal representation         |
| `hex()`      | `__hex__(self)`           | Conversion to string containing a hexadecimal representation    |

---

## 🔍 Object Introspection

Python offers a set of methods responsible for representing object details using ordinary strings.

| Function     | Magic Method                   | Purpose                                                           |
|--------------|--------------------------------|-------------------------------------------------------------------|
| `str()`      | `__str__(self)`                | Handles `str()` function calls                                    |
| `repr()`     | `__repr__(self)`               | Handles `repr()` function calls                                   |
| `format()`   | `__format__(self, formatstr)`  | Called when new-style string formatting is applied to an object   |
| `hash()`     | `__hash__(self)`               | Handles `hash()` function calls                                   |
| `dir()`      | `__dir__(self)`                | Handles `dir()` function calls                                    |
| `bool()`     | `__nonzero__(self)`            | Handles `bool()` function calls                                   |

---

## 🔁 Object Retrospection

Continuing the topic of object introspection, Python also provides methods responsible for object reflection.

| Function                      | Magic Method                           | Purpose                               |
|-------------------------------|----------------------------------------|---------------------------------------|
| `isinstance(object, class)`   | `__instancecheck__(self, object)`      | Handles `isinstance()` function calls |
| `issubclass(subclass, class)` | `__subclasscheck__(self, subclass)`    | Handles `issubclass()` function calls |

---

## 🧠 Object Attribute Access

Access to object attributes can be controlled via the following magic methods:

| Expression Example           | Magic Method                          | Purpose                                        |
|------------------------------|---------------------------------------|------------------------------------------------|
| `object.attribute`           | `__getattr__(self, attribute)`        | Handles access to a **non-existing** attribute |
| `object.attribute`           | `__getattribute__(self, attribute)`   | Handles access to an **existing** attribute    |
| `object.attribute = value`   | `__setattr__(self, attribute, value)` | Handles setting an attribute's value           |
| `del object.attribute`       | `__delattr__(self, attribute)`        | Handles deleting an attribute                  |

---

## 📦 Container Access Methods

Containers are objects that hold an arbitrary number of other objects (e.g., `list`, `dict`, `tuple`, `set`). These magic methods provide ways to interact with their contents.

| Expression Example           | Magic Method                    | Purpose                                             |
|------------------------------|---------------------------------|-----------------------------------------------------|
| `len(container)`             | `__len__(self)`                 | Returns the number of elements in the container     |
| `container[key]`             | `__getitem__(self, key)`        | Fetches the element identified by the key           |
| `container[key] = value`     | `__setitem__(self, key, value)` | Sets the element identified by the key              |
| `del container[key]`         | `__delitem__(self, key)`        | Deletes the element identified by the key           |
| `for element in container`   | `__iter__(self)`                | Returns an iterator for the container               |
| `item in container`          | `__contains__(self, item)`      | Checks if the container contains the selected item  |

---

For a full reference of Python's special methods, see the official documentation:  
🔗 [Python Data Model – Special Method Names](https://docs.python.org/3/reference/datamodel.html#special-method-names)
