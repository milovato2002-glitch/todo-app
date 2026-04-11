"""
To-Do List CLI Application
A simple command-line to-do list manager that allows users
to add, view, and delete tasks.
"""


# Task storage list
tasks = []


def display_welcome():
    """Display a welcome message when the application starts."""
    print("\n" + "=" * 40)
    print("   Welcome to the To-Do List App!")
    print("=" * 40)


def display_menu():
    """Display the main menu options to the user."""
    print("\nPlease choose an option:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Quit")


def add_task():
    """Prompt the user for a task description and add it to the list."""
    try:
        task = input("\nEnter the task description: ").strip()
        # Validate that the input is not empty
        if not task:
            print("Invalid input: Task description cannot be empty.")
        else:
            tasks.append(task)
    except EOFError:
        print("\nError: Unexpected end of input.")
    else:
        if task:
            print(f'Task "{task}" has been added.')
    finally:
        print(f"You now have {len(tasks)} task(s) in your list.")


def view_tasks():
    """Display all current tasks in the list."""
    try:
        # Check if the list is empty
        if not tasks:
            print("\nYour to-do list is empty. Add some tasks first!")
        else:
            print("\nYour To-Do List:")
            print("-" * 30)
            for index, task in enumerate(tasks, start=1):
                print(f"  {index}. {task}")
            print("-" * 30)
    except Exception as e:
        print(f"\nError displaying tasks: {e}")
    finally:
        print(f"Total tasks: {len(tasks)}")


def delete_task():
    """Prompt the user for a task number and remove it from the list."""
    # Check if there are any tasks to delete
    if not tasks:
        print("\nYour to-do list is empty. Nothing to delete!")
        return

    # Show current tasks so the user knows what to delete
    view_tasks()

    try:
        choice = input("\nEnter the task number to delete: ").strip()
        task_number = int(choice)

        # Validate the task number is within range
        if task_number < 1 or task_number > len(tasks):
            print(f"Task not found: Please enter a number between 1 and {len(tasks)}.")
        else:
            removed_task = tasks.pop(task_number - 1)
            print(f'Task "{removed_task}" has been deleted.')
    except ValueError:
        print("Invalid input: Please enter a valid number.")
    except EOFError:
        print("\nError: Unexpected end of input.")
    finally:
        print(f"Remaining tasks: {len(tasks)}")


def get_menu_choice():
    """Get and validate the user's menu selection.

    Returns:
        str: The user's menu choice as a string, or None on input error.
    """
    try:
        choice = input("\nEnter your choice (1-4): ").strip()
    except EOFError:
        print("\nError: Unexpected end of input.")
        return None
    else:
        return choice
    finally:
        pass  # Input prompt complete


def main():
    """Run the main application loop."""
    display_welcome()

    # Main loop — keeps running until the user chooses to quit
    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("\nGoodbye! Have a productive day!")
            break
        else:
            # Alert the user about an invalid menu option
            print("Invalid option: Please choose 1, 2, 3, or 4.")


# Entry point
if __name__ == "__main__":
    main()
