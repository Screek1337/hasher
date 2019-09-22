from tkinter import Frame, Entry, Button, LEFT, Tk, filedialog
import hashlib


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.filename = None
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.edit_field = Entry(root, width=100)
        self.choose_file_button = Button(
            root, text="Choose file", command=self.get_file_dir)
        self.get_digest_button = Button(
            root, text="Get hash", command=self.get_digest)
        self.edit_field.pack()
        self.choose_file_button.pack(side=LEFT)
        self.get_digest_button.pack(side=LEFT)

    def get_file_dir(self):
        self.filename = filedialog.askopenfilename(
            initialdir="/", title="Select file", filetypes=(
                ("text files", "*.txt"), ("all files", "*.*")))

    def get_digest(self):
        with open(self.filename, "rb") as f:
            bytes = f.read()
            readable_hash = hashlib.sha256(bytes).hexdigest()
            self.edit_field.delete(0, "end")
            self.edit_field.insert(0, readable_hash)


if __name__ == "__main__":
    root = Tk()
    root.title("SHA-256 hash")
    app = Application(master=root)
    app.mainloop()
