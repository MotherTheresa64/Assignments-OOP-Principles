# Assignments-OOP-Principles
# Below are the instructions and specs I was given before making the necessary changes

Some helpful hints: 
1. Modular Design: Break down your application into logical modules.
2. Reusability: By using modules, you can easily reuse code. 
3. Maintainability: With modular code, making changes or updates becomes simpler and less risky.
4. Testing: Testing modules independently becomes more straightforward. You can write and run tests for each module to ensure its functionality before integrating it into the   
   main system.
5. Importing Modules: Use the import statement to include modules in your main application script. 
6. Directory Structure: Organize your modules in a clear directory structure.
7. Naming Conventions: Follow Python naming conventions for your modules. Typically, module names should be lowercase with underscores to improve readability (e.g., smart_device.py).
8. Documenting Modules: Provide documentation for each module. A brief comment at the beginning of each module explaining its purpose and functionality can be very helpful.

By adhering to a modular approach, your solutions for the assignments will not only be more effective and efficient but also align with industry standards. This practice will prepare you for larger-scale projects in your programming career.



1. Encapsulation in Personal Budget Management
Objective: The aim of this assignment is to reinforce the understanding of encapsulation in Python, focusing on the use of private attributes and getters and setters.

Problem Statement: You are required to build a Personal Budget Management application. The application will manage budget categories like food, entertainment, utilities, etc., ensuring that budget details remain private and are accessed or modified through public methods.

Task 1: Define Budget Category Class Create a class `BudgetCategory` with private attributes for category name and allocated budget. - Initialize these attributes in the constructor.

- Expected Outcome: A `BudgetCategory` class capable of storing category details securely.

Task 2: Implement Getters and Setters - Write getter and setter methods for both the category name and the allocated budget. - Ensure that the setter methods include validation (e.g., budget should be a positive number).

- Expected Outcome: Methods that allow controlled access and modification of the private attributes, with validation checks in place.

Task 3: Add Budget Functionality Implement a method to add expenses to a category and adjust the budget accordingly. - Validate the expense amount before making deductions from the budget.

Expected Outcome: Ability to track expenses per category and update the remaining budget safely.

Task 4: Display Budget Details Create a method to display the details of a budget category, including the name, allocated budget, and remaining budget after expenses.

Expected Outcome: Users can view a summary of each budget category, showcasing encapsulation in action.

Code Examples:

class BudgetCategory:
    # Constructor and private attributes
    # ...

    # Getters and setters for category name and budget
    # ...

    def add_expense(self, amount):
        # Method to add an expense to the category
        # ...

    def display_category_summary(self):
        # Method to display the budget category details
        # ...

food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()


NOTE: Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks the run button at the top, all code executes as intended. For example, if there are if statements, print statements, or for loops, they should function correctly and display output in the console as expected. If you have a function, make sure the function is called and runs. If there are classes/objects, make sure they are instantiated and the methods are called.

The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.