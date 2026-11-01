## Day 1 — Classes and Objects

### Problem 1

[solution.py](./01_Classes_and_Objects/problem_1_solution.py)
## 🎓 Real-life scenario: Student Management System

You're building a student management system for a school.

The school needs a system to store student information and calculate their academic performance.

Each student has:

- Name
- Student ID
- List of marks

For example:

python

```python
student1 = Student("Ali", "S001", [80, 75, 90])
student2 = Student("John", "S002", [45, 60, 55])
```

Your system should allow the school to:

- Add new marks to a student's record.
- Calculate the student's average mark.
- Display student information.
- Determine whether the student passed or failed.

A student passes if their average mark is at least 50.

## Your programming version

Implement:

python

```python
class Student:
    ...
```

Create these methods:

python

```python
def add_mark(self, mark):
    ...

def calculate_average(self):
    ...

def display_info(self):
    ...

def check_result(self):
    ...
```

Example:

python

```python
student1 = Student("Ali", "S001", [80, 75, 90])

student1.add_mark(85)

student1.calculate_average()
```

Expected:

text

```text
Average: 82.5
Result: Pass
```

Create at least 3 student objects and test them.

## Think before coding

Don't write Python yet.

Answer:

1. What is a class?
2. What is an object?
3. What information should each student object store?
4. Why should we use `__init__()`?
5. What is the purpose of `self`?
6. If you create 3 students, will they share the same marks?
7. Which attributes belong to each individual student?
8. Why should calculating the average be a method?
9. What should happen if a student has no marks?
10. Can you explain the difference between a class and an object in your own words?

# Day 2 — Encapsulation

### Problem 2

[solution.py](./02_Encapsulation/problem_2_solution.py)
## 🏦 Real-life scenario: Banking System

You're developing a banking application.

Customers can deposit and withdraw money from their accounts.

For example:

python

```python
account1 = BankAccount("Ali", "ACC001", 1000)
```

The account contains:

text

```text
Account holder: Ali
Account number: ACC001
Balance: RM1000
```

However, there's one important security requirement.

Customers should not be able to directly modify their account balance.

For example, this should not be allowed:

python

```python
account1.balance = 1000000
```

Instead, they must use the proper banking operations.

Your system should support:

- Depositing money.
- Withdrawing money.
- Checking the current balance.

### Rules

1. Deposits must be greater than zero.
2. Withdrawals must be greater than zero.
3. Customers cannot withdraw more money than their available balance.
4. The balance should be protected using encapsulation.

## Your programming version

Implement:

python

```python
class BankAccount:
    ...
```

Create these methods:

python

```python
def deposit(self, amount):
    ...

def withdraw(self, amount):
    ...

def check_balance(self):
    ...
```

Example:

python

```python
account1 = BankAccount("Ali", "ACC001", 1000)

account1.deposit(500)
account1.withdraw(200)

account1.check_balance()
```

Expected:

text

```text
Deposit successful: RM500
Withdrawal successful: RM200
Current balance: RM1300
```

Another example:

python

```python
account1.withdraw(2000)
```

Expected:

text

```text
Insufficient balance!
```

## Think before coding

Don't write Python yet.

Answer:

1. What problem does encapsulation solve?
2. Why shouldn't customers directly modify their balance?
3. What is the difference between public and private attributes?
4. What does `__balance` mean in Python?
5. How can methods safely modify private attributes?
6. Why should we validate the deposit amount?
7. What happens if someone tries to withdraw more than the balance?
8. What is the purpose of a getter?
9. What is the purpose of a setter?
10. How does encapsulation protect an object's data?

# Day 3 — Inheritance

### Problem 3

[solution.py](./03_Inheritance/problem_3_solution.py)

## 🛒 Real-life scenario: Online Shopping System

You're building an online shopping application.

Your store sells different types of products:

- Electronics
- Clothing
- Food

Every product shares some common information:

- Product name
- Product ID
- Price

However, each product type has additional information.

For example:

Electronics

text

```text
Product: Laptop
Price: RM3000
Warranty: 2 years
```

Clothing

text

```text
Product: T-Shirt
Price: RM50
Size: M
```

Food

text

```text
Product: Chocolate
Price: RM10
Expiry date: 2026-12-30
```

Instead of writing the same attributes and methods repeatedly, you decide to use inheritance.

## Your programming version

Implement:

python

```python
class Product:
    ...
```

Create three child classes:

python

```python
class Electronics(Product):
    ...

class Clothing(Product):
    ...

class Food(Product):
    ...
```

The parent class should contain:

python

```python
name
product_id
price
```

Each child class should contain its own additional attribute.

Implement:

python

```python
def display_info(self):
    ...
```

Example:

python

```python
laptop = Electronics("Laptop", "P001", 3000, 2)

shirt = Clothing("T-Shirt", "P002", 50, "M")

chocolate = Food("Chocolate", "P003", 10, "2026-12-30")
```

Expected:

text

```text
Product: Laptop
ID: P001
Price: RM3000
Warranty: 2 years
```

Display the information for all three products.

## Think before coding

Don't write Python yet.

Answer:

1. What is inheritance?
2. Why do we need a parent class?
3. What attributes should be placed inside the parent class?
4. What attributes should be placed inside child classes?
5. What does `class Electronics(Product)` mean?
6. What is the purpose of `super()`?
7. Can a child class access its parent's methods?
8. Can a child class have its own methods?
9. Why is inheritance better than repeating the same code?
10. What is the relationship between a parent class and a child class?

# Day 4 — Polymorphism

### Problem 4

[solution.py](./04_Polymorphism/problem_4_solution.py)

## 💳 Real-life scenario: Payment Processing System

You're developing an online shopping application.

Customers can pay using different payment methods:

- Credit card
- PayPal
- Bank transfer

Each payment method works differently.

For example:

Credit Card

text

```text
Processing credit card payment...
Payment of RM100 successful!
```

PayPal

text

```text
Processing PayPal payment...
Payment of RM100 successful!
```

Bank Transfer

text

```text
Processing bank transfer...
Payment of RM100 successful!
```

Although the payment methods work differently, they all perform the same general operation:

python

```python
process_payment(amount)
```

You want to write one function that can work with all payment types.

## Your programming version

Implement:

python

```python
class Payment:
    ...

class CreditCardPayment(Payment):
    ...

class PayPalPayment(Payment):
    ...

class BankTransferPayment(Payment):
    ...
```

Each child class should implement:

python

```python
def process_payment(self, amount):
    ...
```

Now create a function:

python

```python
def checkout(payment_method, amount):
    ...
```

Example:

python

```python
credit_card = CreditCardPayment()
paypal = PayPalPayment()
bank = BankTransferPayment()

checkout(credit_card, 100)
checkout(paypal, 200)
checkout(bank, 300)
```

Expected:

text

```text
Processing credit card payment...
Payment of RM100 successful!

Processing PayPal payment...
Payment of RM200 successful!

Processing bank transfer...
Payment of RM300 successful!
```

## Think before coding

Don't write Python yet.

Answer:

1. What is polymorphism?
2. What does the word polymorphism mean?
3. Why do different payment classes have the same method name?
4. What happens when you call `process_payment()` on different objects?
5. Why can the same function work with different payment objects?
6. What is method overriding?
7. How is method overriding related to inheritance?
8. Do you need to check the object's class name inside `checkout()`?
9. What would happen if you added a new payment method?
10. How does polymorphism make your code more flexible?

# Day 5 — Encapsulation + Inheritance

### Problem 5

[solution.py](./05_Inheritance_and_Encapsulation/problem_5_solution.py)

## 🏥 Real-life scenario: Hospital Management System

You're developing a hospital management system.

The hospital needs to manage doctors and patients.

Both doctors and patients share common information:

- Name
- Age
- Contact information

However, they also have different information.

Doctor

text

```text
Name: Dr. Ahmad
Age: 40
Specialization: Cardiologist
Consultation fee: RM150
```

Patient

text

```text
Name: Ali
Age: 25
Patient ID: P001
Medical history: Private
```

You decide to use inheritance to organize the system.

However, patient medical information must also be protected.

### Rules

1. Create a parent class called `Person`.
2. Create child classes called `Doctor` and `Patient`.
3. Doctors should have a specialization and consultation fee.
4. Patients should have a patient ID and medical history.
5. Medical history should not be directly accessible for modification.
6. Provide methods to safely view and update medical history.

## Your programming version

Implement:

python

```python
class Person:
    ...

class Doctor(Person):
    ...

class Patient(Person):
    ...
```

The `Patient` class should contain:

python

```python
def update_medical_history(self, new_history):
    ...

def view_medical_history(self):
    ...
```

Example:

python

```python
doctor1 = Doctor("Dr. Ahmad", 40, "0123456789",
                 "Cardiologist", 150)

patient1 = Patient("Ali", 25, "0198765432",
                   "P001", "No previous medical history")
```

Expected:

text

```text
Doctor: Dr. Ahmad
Specialization: Cardiologist
Consultation fee: RM150

Patient: Ali
Patient ID: P001
Medical history: No previous medical history
```

## Think before coding

Don't write Python yet.

Answer:

1. What information is shared between doctors and patients?
2. Why should both classes inherit from `Person`?
3. Which attributes belong only to `Doctor`?
4. Which attributes belong only to `Patient`?
5. Why should medical history be private?
6. How can you update private information safely?
7. Can a child class access methods from its parent?
8. What is the purpose of `super()`?
9. Can inheritance and encapsulation be used together?
10. How would you prevent unauthorized changes to medical history?

# Day 6 — Abstraction + Polymorphism

### Problem 6

[solution.py](./06_Abstraction_and_Polymorphism/problem_6_solution.py)

## 🍔 Real-life scenario: Food Delivery Application

You're building a food delivery application.

Customers can choose different delivery methods:

- Bike delivery
- Car delivery
- Van delivery

Each delivery method has different delivery fees and estimated delivery times.

For example:

Bike Delivery

text

```text
Delivery fee: RM5
Estimated time: 20 minutes
```

Car Delivery

text

```text
Delivery fee: RM10
Estimated time: 15 minutes
```

Van Delivery

text

```text
Delivery fee: RM15
Estimated time: 30 minutes
```

However, every delivery method must provide two operations:

- Calculate delivery fee.
- Estimate delivery time.

You want to enforce this requirement using abstraction.

## Your programming version

Implement an abstract class:

python

```python
from abc import ABC, abstractmethod

class Delivery(ABC):
    ...
```

Define two abstract methods:

python

```python
@abstractmethod
def calculate_delivery_fee(self):
    ...

@abstractmethod
def estimate_delivery_time(self):
    ...
```

Create three child classes:

python

```python
class BikeDelivery(Delivery):
    ...

class CarDelivery(Delivery):
    ...

class VanDelivery(Delivery):
    ...
```

Each child class must implement both abstract methods.

Now create a function:

python

```python
def display_delivery_info(delivery):
    ...
```

Example:

python

```python
bike = BikeDelivery()
car = CarDelivery()
van = VanDelivery()

display_delivery_info(bike)
display_delivery_info(car)
display_delivery_info(van)
```

Expected:

text

```text
Delivery method: Bike
Delivery fee: RM5
Estimated time: 20 minutes
```

Repeat for the other delivery methods.

## Think before coding

Don't write Python yet.

Answer:

1. What is abstraction?
2. Why do we need an abstract class?
3. What is the purpose of `ABC`?
4. What does `@abstractmethod` do?
5. Can you create an object directly from an abstract class?
6. What happens if a child class doesn't implement an abstract method?
7. Why must every delivery class implement the same methods?
8. How is abstraction different from encapsulation?
9. How does polymorphism work with abstract classes?
10. Why is abstraction useful when building large applications?

# Day 7 — Mixed Problem (Full OOP Project)

### Problem 7

[solution.py](./07_Full_OOP_Project/problem_7_solution.py)

## 🛍️ Real-life scenario: E-Commerce Application

You're building a complete e-commerce application similar to a small online shopping platform.

Your application needs to support:

- Customer registration and login.
- Product management.
- Shopping carts.
- Checkout.
- Multiple payment methods.

You must use all the OOP concepts you've learned.

## Your programming requirements

### 1. User Management — Classes and Objects

Create a parent class:

python

```python
class User:
    ...
```

Each user should have:

text

```text
Name
Email
Password
```

Implement:

python

```python
def login(self, email, password):
    ...

def display_info(self):
    ...
```

### 2. Customer and Admin — Inheritance

Create two child classes:

python

```python
class Customer(User):
    ...

class Admin(User):
    ...
```

Customer should be able to:

- Browse products.
- Add products to cart.
- Remove products from cart.
- Checkout.

Admin should be able to:

- Add products.
- Update products.
- Remove products.
- View available inventory.

### 3. Product Management — Encapsulation

Create:

python

```python
class Product:
    ...
```

Each product should have:

text

```text
Product ID
Name
Price
Quantity
```

Protect the quantity using encapsulation.

Implement:

python

```python
def update_quantity(self, amount):
    ...

def check_stock(self):
    ...
```

Make sure the system does not allow invalid stock quantities.

### 4. Payment Processing — Abstraction

Create an abstract class:

python

```python
class Payment(ABC):
    ...
```

Define an abstract method:

python

```python
@abstractmethod
def pay(self, amount):
    ...
```

Create two child classes:

python

```python
class CreditCardPayment(Payment):
    ...

class CashPayment(Payment):
    ...
```

Each payment method should implement `pay()` differently.

### 5. Polymorphism

Create a checkout function:

python

```python
def checkout(payment_method, amount):
    ...
```

It should work with both:

python

```python
credit_card = CreditCardPayment()
cash = CashPayment()
```

You should not need to write separate checkout functions for each payment method.

### 6. Modules

Organize your application into separate Python files.

Suggested folder structure:

text

```text
ecommerce/
│
├── main.py
│
├── users.py
│
├── products.py
│
├── payments.py
│
├── cart.py
│
└── admin.py
```

Each file should have a clear responsibility.

Use imports to connect the different classes.

## Expected application behaviour

Your application should support a flow similar to this:

text

```text
Welcome to E-Commerce!

1. Login as Customer
2. Login as Admin

Select: 1

Welcome, Ali!

Available Products:

P001 - Laptop - RM3000 - Stock: 5
P002 - Mouse - RM50 - Stock: 10
P003 - Keyboard - RM100 - Stock: 8

Select a product: P002

Mouse added to cart!

Your Cart:

Mouse - RM50

Total: RM50

Choose Payment Method:

1. Credit Card
2. Cash

Select: 1

Processing credit card payment...

Payment successful!

Order completed!
```

## Think before coding

Don't write Python yet.

Answer:

1. Which classes do you need in this application?
2. Which classes should inherit from other classes?
3. Which attributes should be private?
4. Which class should be abstract?
5. Where will you implement polymorphism?
6. Why should `Customer` and `Admin` inherit from `User`?
7. Which class should be responsible for managing products?
8. How should the cart communicate with the product class?
9. Why should the application be separated into modules?
10. How would you prevent customers from purchasing more products than available stock?
11. What happens if a customer tries to checkout with an empty cart?
12. Can you explain how all six OOP concepts work together in this application?

