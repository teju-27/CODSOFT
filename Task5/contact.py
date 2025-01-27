import tkinter as tk
from tkinter import messagebox, simpledialog
class ContactBookApp:
    def __init__(self, window):
        self.window = window
        self.window.title("📖 Contact Book")
        self.window.geometry("400x500")
        self.contacts = {}
        tk.Label(window, text="📖 My Contact Book", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Button(window, text="➕ Add Contact", command=self.add_contact, width=25).pack(pady=5)
        tk.Button(window, text="📂 View Contacts", command=self.view_contacts, width=25).pack(pady=5)
        tk.Button(window, text="🔍 Search Contact", command=self.search_contact, width=25).pack(pady=5)
        tk.Button(window, text="✏️ Update Contact", command=self.update_contact, width=25).pack(pady=5)
        tk.Button(window, text="🗑 Delete Contact", command=self.delete_contact, width=25).pack(pady=5)
        tk.Button(window, text="🚪 Exit", command=window.quit, width=25, bg="red", fg="white").pack(pady=10)
    def add_contact(self):
        name = simpledialog.askstring("New Contact", "Enter Contact Name:")
        if not name:
            return  # Stop if no name is entered
        phone = simpledialog.askstring("New Contact", "Enter Phone Number:")
        email = simpledialog.askstring("New Contact", "Enter Email Address:")
        address = simpledialog.askstring("New Contact", "Enter Home Address:")
        self.contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        messagebox.showinfo("Success", f"✅ Contact '{name}' added successfully!")
    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Contacts", "ℹ️ No contacts available. Add some first!")
            return
        contact_list = "\n".join([f"📌 {name}: {info['Phone']}" for name, info in self.contacts.items()])
        messagebox.showinfo("Contacts List", contact_list)
    def search_contact(self):
        query = simpledialog.askstring("Search Contact", "Enter Name or Phone Number:")
        if not query:
            return
        for name, details in self.contacts.items():
            if name.lower() == query.lower() or details["Phone"] == query:
                contact_info = f"👤 Name: {name}\n📞 Phone: {details['Phone']}\n📧 Email: {details['Email']}\n🏠 Address: {details['Address']}"
                messagebox.showinfo("Contact Found", contact_info)
                return
        messagebox.showwarning("Not Found", "❌ No matching contact found!")
    def update_contact(self):
        name = simpledialog.askstring("Update Contact", "Enter Contact Name:")
        if not name or name not in self.contacts:
            messagebox.showwarning("Not Found", "❌ Contact not found!")
            return
        messagebox.showinfo("Update", "ℹ️ Leave fields blank to keep existing details.")
        new_phone = simpledialog.askstring("Update Contact", f"📞 New Phone ({self.contacts[name]['Phone']}):")
        new_email = simpledialog.askstring("Update Contact", f"📧 New Email ({self.contacts[name]['Email']}):")
        new_address = simpledialog.askstring("Update Contact", f"🏠 New Address ({self.contacts[name]['Address']}):")
        if new_phone:
            self.contacts[name]["Phone"] = new_phone
        if new_email:
            self.contacts[name]["Email"] = new_email
        if new_address:
            self.contacts[name]["Address"] = new_address
        messagebox.showinfo("Success", f"✅ Contact '{name}' updated!")
    def delete_contact(self):
        name = simpledialog.askstring("Delete Contact", "Enter Contact Name:")
        if not name or name not in self.contacts:
            messagebox.showwarning("Not Found", "❌ Contact not found!")
            return
        confirm = messagebox.askyesno("Confirm Deletion", f"⚠️ Are you sure you want to delete '{name}'?")
        if confirm:
            del self.contacts[name]
            messagebox.showinfo("Deleted", f"🗑️ Contact '{name}' deleted!")
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()