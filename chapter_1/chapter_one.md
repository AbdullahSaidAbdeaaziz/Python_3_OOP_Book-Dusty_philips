
# 📘 Chapter One: Object-Oriented Design

## 🔍 What is Object-Oriented Programming?

- **🧱 Object**: A collection of data and the behaviors (methods) associated with that data.
- **🎯 Oriented**: Directed toward.
- **🧩 Object-Oriented**: A programming paradigm directed toward modeling software using objects.

---

## 🧭 Key Phases of Object-Oriented Development

### 1️⃣ Object-Oriented Analysis
- The process of examining a problem, system, or task to identify the objects involved and their interactions.
- Focuses on **what** needs to be done.

```
Task or Website → Analysis Stage → Requirements
```

---

### 2️⃣ Object-Oriented Design
- Translates requirements into implementation specifications, such as class structures and interfaces.
- Focuses on **how** the solution should be implemented.

```
Requirements → Design Stage → Classes, Interfaces, Architecture
```

---

### 3️⃣ Object-Oriented Programming
- The final step: writing code based on the design to create a functioning application that meets the original requirements.

```
Classes & Design → Programming Stage → Functional Python Program
```

---

## 🧱 Core Concepts

### 🧰 Classes and Objects
- **📦 Class**: A blueprint for creating objects.
- **🔸 Object**: A concrete instance of a class.

---

### 🎭 Attributes and Behaviors
- **📌 Attributes**: Data stored in an object (also called properties or fields).
- **⚙️ Behaviors (Methods)**: Functions associated with an object that define its actions.

---

## 🔐 Encapsulation and Public Interfaces

- **🔒 Encapsulation**: Hiding internal implementation details and exposing only what's necessary through a public interface.

### 🎯 Why Encapsulation Matters
1. ✅ **Protects Data Integrity** – Prevents unintended modifications.
2. ✅ **Reduces Complexity** – Users interact only with what they need to.
3. ✅ **Improves Maintainability** – Internals can change without affecting external code.
4. ✅ **Enhances Security** – Sensitive data stays protected.

### 🧩 Public Interface vs. Private Data
- **🌐 Public Interface**: Methods and attributes available for external use.
- **🔐 Private Data**: Internal implementation details hidden from outside access.

### 🔐 Encapsulation Example

```python
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

# Usage
acc = Account("Alice", 1000)
acc.deposit(500)
print(acc.get_balance())  # Output: 1500
```

---

## 🎭 Abstraction

- Abstraction means showing only the necessary details while hiding the complexity.
- Encapsulation supports abstraction by exposing a clean interface.

**Examples:**
- *🔧 Encapsulation*: The engine is hidden inside the car; users interact with the pedals and steering.
- *🚗 Abstraction*: Users don’t need to know how the engine works, just how to drive.

---

## 🧬 Composition

- **🧱 Composition** is a design technique that models a “has-a” relationship.
- One object is composed of other objects, each responsible for part of the behavior.

### 🔑 Key Points:
- Models modular, maintainable systems.
- Encourages code reuse and separation of concerns.
- Components can often be reused independently.

### 🧱 Composition Example

```python
class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition

    def drive(self):
        self.engine.start()
        print("Car is driving.")

# Usage
my_car = Car()
my_car.drive()
```

---

## 🧬 Inheritance

- **📤 Inheritance** allows a new class (child/subclass) to inherit attributes and methods from an existing class (parent/superclass).
- Models an “is-a” relationship.

### 📚 Benefits:
- Promotes code reuse.
- Enables specialization through method overriding.

### 🧬 Inheritance Example

```python
class Animal:
    def speak(self):
        print("Animal speaks.")

class Dog(Animal):  # Inherits from Animal
    def speak(self):
        print("Woof!")

# Usage
dog = Dog()
dog.speak()  # Output: Woof!
```

---

## 🌀 Polymorphism

- **🌀 Polymorphism** allows objects of different subclasses to be treated as objects of the parent class.
- Python supports **dynamic polymorphism** due to its **duck typing** nature:

> “If it walks like a duck and quacks like a duck, it’s a duck.”

### 🌀 Polymorphism Example

```python
class Bird:
    def fly(self):
        print("Bird is flying.")

class Airplane:
    def fly(self):
        print("Airplane is flying.")

def make_it_fly(flyer):
    flyer.fly()

# Usage
make_it_fly(Bird())      # Output: Bird is flying.
make_it_fly(Airplane())  # Output: Airplane is flying.
```

---

## 🌐 Multiple Inheritance

- A class can inherit from more than one parent class.
- Python resolves method conflicts using the **Method Resolution Order (MRO)** – typically left to right.

### ⚠️ Caution:
- Multiple inheritance increases flexibility and reuse, **but also complexity**, especially with:
  - 🔁 Diamond inheritance
  - 🧱 Deep class hierarchies

### ✅ Recommendation:
- Prefer **composition** over inheritance when design becomes tangled.
- Python's `super()` function and MRO help manage complex inheritance trees safely—but only when used with care.

### 🌀 Composition over Inheritance Example

```python
class Father:
    def speak(self):
        return "Father says: Work hard!"

class Mother:
    def speak(self):
        return "Mother says: Be kind!"

class Child:
    def __init__(self, father, mother):
        self.father = father
        self.mother = mother

    def speak(self, parent="father"):  # Explicitly choose which method to call
        if parent == "father":
            return self.father.speak()
        elif parent == "mother":
            return self.mother.speak()
        else:
            return "Child says: I have my own voice!"

# Creating instances
dad = Father()
mom = Mother()
child = Child(dad, mom)

# Explicitly choosing which parent's method to call
print(child.speak("father"))  # Outputs: "Father says: Work hard!"
print(child.speak("mother"))  # Outputs: "Mother says: Be kind!"
print(child.speak("self"))    # Outputs: "Child says: I have my own voice!"
```
