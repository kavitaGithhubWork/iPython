# Step 1: Create an empty to-do list
todo_list = []

# Step 2: Add some tasks using append()
todo_list.append("call mom")
todo_list.append("call dad")
todo_list.append("call Suhani")
print("Initial To-Do List:", todo_list)

# Step 3: Insert a high-priority task at the beginning

todo_list.insert("didi")

# Step 4: Update a task (change "Call Mom" to "Call Dad")
i = todo_list("call mom")
todo_list[i] = "call papa"
# Step 5: Remove a completed task
todo_list.remove("Buy groceries")

# Step 6: Add multiple tasks using extend()
todo_list.extend(["Walk the dog", "Read a book"])

# Step 7: Display a slice (first 3 tasks)
print("Top 3 Tasks:", todo_list[:3])

# Step 8: Show tasks in reverse order
print("Tasks in Reverse:", todo_list[::-1])

# Step 9: Sort tasks alphabetically
todo_list.sort()

# Step 10: Display final list
print("Final To-Do List:", todo_list)
