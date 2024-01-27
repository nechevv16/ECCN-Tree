from customtkinter import CTk, CTkLabel, CTkButton
from tkinter import messagebox

class TreeNode:
    def __init__(self, question, description, children=None):
        self.question = question
        self.description = description
        self.children = children or []

# Custom Tkinter App
class CustomTkinterApp:
    def __init__(self, root, tree_file):
        self.root = root
        self.tree_root = self.create_tree_from_file(tree_file)
        self.current_node = None
        self.current_screen = 0
        self.screens = []  # List to store screens
        self.widgets = []  # List to store widgets for current screen

        self.create_screens(self.tree_root)
        self.show_current_screen()

    def create_tree_from_file(self, tree_file):
        with open(tree_file, 'r') as file:
            lines = file.readlines()

        root = TreeNode("", "", [])
        stack = [(0, root)]

        for line in lines[1:]:
            depth = line.index(line.lstrip()) // 4  # Assuming 4 spaces for each level of indentation
            question, description = map(str.strip, line.split("|", 1))
            node = TreeNode(question, description, [])

            while stack and stack[-1][0] >= depth:
                stack.pop()

            parent = stack[-1][1] if stack else root
            parent.children.append(node)
            stack.append((depth, node))

        return root

    def create_screens(self, node):
        self.screens.append((node.question, node.description, node.children))
        for child in node.children:
            self.create_screens(child)

    def show_current_screen(self):
        if self.current_screen < len(self.screens):
            self.current_node = self.screens[self.current_screen]
            self.create_gui()
        else:
            messagebox.showinfo("Leaf Node", "You've reached the leaf node.")

    def create_gui(self):
        # Remove previous widgets
        for widget in self.widgets:
            widget.destroy()

        # Create new widgets for the current screen
        CTkLabel(self.root, text=self.current_node[0]).pack(pady=5)
        CTkLabel(self.root, text=self.current_node[1]).pack(pady=5)

        if self.current_screen == 0:  # Display only initial options
            for i, child in enumerate(self.current_node[2]):
                button = CTkButton(self.root, text=f"Option {i + 1}", command=lambda c=child: self.next_screen(c))
                button.pack(pady=5)
                self.widgets.append(button)

        if self.current_screen > 0:
            back_button = CTkButton(self.root, text="Back", command=self.go_back)
            back_button.pack(pady=10)
            self.widgets.append(back_button)

    def next_screen(self, next_node):
        self.current_screen += 1
        self.show_current_screen()

    def go_back(self):
        if self.current_screen > 0:
            self.current_screen -= 1
            self.show_current_screen()

# Main Application
if __name__ == "__main__":
    root = CTk()
    app = CustomTkinterApp(root, "tree_with_description.txt")
    root.mainloop()
