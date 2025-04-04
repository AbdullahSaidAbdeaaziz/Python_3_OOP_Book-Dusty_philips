# 🚀 Chapter Three: When object-oriented are alike

## 📖 overview
This chapter dives into how inheritance helps you avoid duplicating code by creating “is a” relationships between classes. It covers both basic and multiple inheritance, explains how to override methods and use the super() function to call parent methods correctly, and discusses advanced topics like polymorphism, duck typing, and abstract base classes (ABCs).

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
  - The contact class maintains a shared list of contacts using a class variable. The supplier subclass inherits from contact and adds an order method without duplicating the initialization code.
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
