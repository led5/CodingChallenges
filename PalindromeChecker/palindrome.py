import tkinter as tk 

# Create view 
root = tk.Tk()
root.title("Palindrome Checker")
tk.Label(root, text="Enter Palindrome ").grid(row=0)

# User input 
input = tk.Entry(root)
input.grid(row=0, column=1)

# Result from check_palindrome to console 
result = tk.Label(root, text='')
result.grid(row=2, column=0, columnspan=2)

def check_palindrome(p):
    ret = ''
    if ((p == p[::-1]) == True):
        ret = p + ' is a palindrome.'
    else:
        ret = p + ' is not a palindrome.'
    return ret

def clear_input():
    input.delete(first=0, last=100)
     
def is_palindrome():
    # Create buttons 
    check = tk.Button(root, text="Check") 
    clear = tk.Button(root, text="Clear", command=clear_input) 
    check.config(command=lambda: result.config(text=check_palindrome(input.get())))

    # Arrange buttons 
    check.grid(row=1, column=0)
    clear.grid(row=1, column=1)

    root.mainloop()

if __name__ == "__main__":
    is_palindrome()