"""Program 3.12: to-do list with ordered tasks and unique tags."""
tasks = []
def add_task(task, tags): tasks.append({"task": task, "tags": set(tags)})
def display_all():
    for index, item in enumerate(tasks, 1): print(str(index) + ".", item["task"], "-", ", ".join(sorted(item["tags"])))
def find_by_tag(tag): return [item["task"] for item in tasks if tag in item["tags"]]

add_task("Complete Python practical", ["study", "python"])
add_task("Buy notebook", ["personal", "shopping"])
add_task("Revise functions", ["study", "python"])
display_all()
print("Tasks tagged 'study':", find_by_tag("study"))
