## 🧬 Multiple Inheritance in Python

There are no obstacles to using **multiple inheritance** in Python. You can derive any new class from more than one previously defined class.

However, multiple inheritance should be used with **more prudence** than single inheritance because:

- ✅ A **single inheritance** class is always simpler, safer, and easier to understand and maintain.
- ⚠️ **Multiple inheritance** may make method overriding somewhat tricky; moreover, using the `super()` function can lead to ambiguity.
- 📛 It is highly probable that by implementing multiple inheritance you are **violating the Single Responsibility Principle (SRP)**.
- 💡 If your solution tends to require multiple inheritance, it might be a good idea to consider implementing **composition** instead.


---

## 🧭 Multiple Inheritance and MRO Example

```python
class A:
    def info(self):
        print('Class A')

class B(A):
    def info(self):
        print('Class B')

class C(A):
    def info(self):
        print('Class C')

class D(B, C):
    pass

D().info()  # Output: Class B
```

In the **multiple inheritance** scenario, any specified attribute is searched for:

1. First in the current class;
2. Then in direct parent classes, following a **depth-first, left-to-right** order according to the class definition.

This is defined by the **MRO (Method Resolution Order)** algorithm.

### In this case:

* `class D` does **not** define the method `info()`, so Python looks into its ancestors.
* `class D` inherits from `B` and `C`, in that order.
* Python looks into `B` first → finds `info()` → **stops searching**.
* The method from `class B` is executed: `Class B`.

To view the MRO explicitly, you can run:

```python
print(D.__mro__)
```
