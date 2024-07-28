# Personal Budget Management Application

# Task 1: Define Budget Category Class
class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        # Private attributes
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget  # Initialize remaining budget

    # Task 2: Implement Getters and Setters

    # Getter for category name
    def get_category_name(self):
        return self.__category_name

    # Setter for category name
    def set_category_name(self, new_name):
        self.__category_name = new_name

    # Getter for allocated budget
    def get_allocated_budget(self):
        return self.__allocated_budget

    # Setter for allocated budget with validation
    def set_allocated_budget(self, new_budget):
        if new_budget < 0:
            raise ValueError("Budget must be a positive number.")
        self.__allocated_budget = new_budget
        self.__remaining_budget = new_budget  # Reset remaining budget

    # Task 3: Add Budget Functionality

    # Add expense method
    def add_expense(self, amount):
        if amount < 0:
            raise ValueError("Expense amount must be a positive number.")
        if amount > self.__remaining_budget:
            raise ValueError("Expense exceeds the remaining budget.")
        self.__remaining_budget -= amount

    # Task 4: Display Budget Details

    # Display category summary
    def display_category_summary(self):
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: ${self.__allocated_budget:.2f}")
        print(f"Remaining Budget: ${self.__remaining_budget:.2f}")

# Example usage
if __name__ == "__main__":
    # Create a budget category
    food_category = BudgetCategory("Food", 500)
    
    # Display initial details
    print("Initial category details:")
    food_category.display_category_summary()
    
    # Add expenses
    food_category.add_expense(100)
    
    # Display updated details
    print("\nAfter adding an expense of $100:")
    food_category.display_category_summary()
    
    # Update category and budget details
    food_category.set_category_name("Groceries")
    food_category.set_allocated_budget(600)
    food_category.add_expense(50)
    
    # Display final updated details
    print("\nAfter updating the category and adding another expense of $50:")
    food_category.display_category_summary()
