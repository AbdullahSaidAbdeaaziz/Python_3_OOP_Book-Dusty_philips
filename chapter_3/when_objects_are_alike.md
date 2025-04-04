# 🚀 Chapter Three: When object-oriented are alike

## 📖 overview
This chapter dives into how inheritance helps you avoid duplicating code by creating “is a” relationships between classes. It covers both basic and multiple inheritance, explains how to override methods and use the `super()` function to call parent methods correctly, and discusses advanced topics like polymorphism, duck typing, and abstract base classes (ABCs).

---

## 1️⃣ Basic Inheritance
- **Definition:** Inheritance allows a subclass to extend a parent (or superclass), reusing common code while adding or overriding functionality.
- **Syntax:**
  ``` python
  class MySubClass(object):
    pass
  ```
- 📓 Even if you don't specify a parent class in python 3, every class automatically inherits from object.
- **Example - Contact and Supplier:**
  - The `Contact` class maintains a shared list of contacts using a class variable. The `Supplier` subclass inherits from `Contact` and adds an `order` method without duplicating the initialization code.
  - [01.base_class](https://github.com/MansAlien/Python_3_OOP_Book-Dusty_philips/blob/main/chapter_3/examples/01.base_class.py)
  - [02.Contact_supplier.py](https://github.com/MansAlien/Python_3_OOP_Book-Dusty_philips/blob/main/chapter_3/examples/02.contact_and_supplier.py)

 
---
  
## 2️⃣ Extending built-ins
- **Concept:** You can create subclasses from built-in types (like `list` and `dict`) to add new functionality.
- **Example - ContactList Subclass:**
  - Instead of using a regular list to store contacts, a subclass called `ContactList` is defined to include a custom `search` method.
  - [03. contactlist_subclass](https://github.com/MansAlien/Python_3_OOP_Book-Dusty_philips/blob/main/chapter_3/examples/03.contactlist_subclass.py)

---

## 3️⃣ Overriding Methods and Using `super()`
- **Overriding:** A subclass can redefine a method from its parent to extend or modify bahavior.
- **Using `super()`:** Instead of calling a parent's method directly (which might lead to duplicated calls), use `super()` to ensure the parent's method is called only once and in the proper order.
- [04.overriding](https://github.com/MansAlien/Python_3_OOP_Book-Dusty_philips/blob/main/chapter_3/examples/04.overriding.py)
- A `super()` call can be made inside any method, not just `__init__`. This means all methods can be modified via overriding and calling `super()`.

---

## 4️⃣ Multiple Inheritance
- **Concept:** A class can inherit from multiple superclass, combining the functionality.
- **Explanation:**
    - THis is useful for mixins (small classes adding specific features) but can complicate method resolution order (MRO), especially in the "diamond problem" where a method might be called multiple times.
    - [05.multiple_inheritance](https://github.com/MansAlien/Python_3_OOP_Book-Dusty_philips/blob/main/chapter_3/examples/05.multiple_inheritance.py)
    - [06.diamond_problem_no_super](https://github.com/MansAlien/Python_3_OOP_Book-Dusty_philips/blob/main/chapter_3/examples/06.diamond_problem_no_super.py)
    - [07.diamond_problem_with_super](https://github.com/MansAlien/Python_3_OOP_Book-Dusty_philips/blob/main/chapter_3/examples/07.diamond_problem_with_super.py)
- `super()` follows the MRO (determined by C3 linearization, ensuring each method is called once.
- **Best Practice:** Use multiple inheritance sparingly, prefer composition for unrelated behaviors, and rely on super to manage MRO correctly.

---

## 5️⃣ Polymorphism
- **Concept:** Different subclasses can implement the same method differently, allowing uniform treatment by a common interface.
- **Explanation:** Polymorphism lets you call a method on a superclass type without knowing the exact subclass, enhancing flexibility.
- **Best Practice:** Design interfaces that allow polymorphic behavior to keep code extensible.
- [08.polymorphism](https://github.com/MansAlien/Python_3_OOP_Book-Dusty_philips/blob/main/chapter_3/examples/08.polymorphism.py)

---

## 6️⃣ Duck Typing
- **Concept:** If an object has the required methods, it can be used regardless of its class or inheritance.
- **Explanation:** Python focuses on behavior ("if it walks like a duck and talks like a duck, it's a duck") rather than strict type hierachies.
- **Best Practice:** Use duck typing to reduce unnecessary inheritance, focusing on what an object does rather than what it is.
- [09.duck_typing_1](https://github.com/MansAlien/Python_3_OOP_Book-Dusty_philips/blob/main/chapter_3/examples/09.duck_typing_1.py)
- [10.duck_typing_2](https://github.com/MansAlien/Python_3_OOP_Book-Dusty_philips/blob/main/chapter_3/examples/10.duck_typing_2.py)

---

## 7️⃣ Abstract Base Classes (ABCs)
- **Concept:** ABCs define a contract that subclasses must follow, ensuring specific methods are implemented.
- **Explanation:** ABCs enforce structure while allowing duck typing flexibility.
- **Best Practice:** Use ABCs to document and enforce inheritance, especially in extensible systems.
- [11.ABCs_1](https://github.com/MansAlien/Python_3_OOP_Book-Dusty_philips/blob/main/chapter_3/examples/11.ABCs_1.py)
- [12.ABCs_2](https://github.com/MansAlien/Python_3_OOP_Book-Dusty_philips/blob/main/chapter_3/examples/12.ABCs_2.py)
