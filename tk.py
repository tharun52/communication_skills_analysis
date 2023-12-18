import tkinter as tk
from tkinter import scrolledtext

def show_triple_section_dialog(paragraph1, paragraph2, score):
    # Create the main window
    root = tk.Tk()
    root.title("Triple Section Dialog Box")

    # Create the first section with title and paragraph
    section1_label = tk.Label(root, text="Transcribed text", font=("Helvetica", 14, "bold"))
    section1_label.pack(pady=5)

    text_widget1 = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=6)
    text_widget1.insert(tk.END, paragraph1)
    text_widget1.configure(state='disabled')  # Make the text widget read-only
    text_widget1.pack(padx=10, pady=5)

    # Create a separator between sections
    separator1 = tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN)
    separator1.pack(fill=tk.X, padx=5, pady=5)

    # Create the second section with title and paragraph
    section2_label = tk.Label(root, text="Corrected text", font=("Helvetica", 14, "bold"))
    section2_label.pack(pady=5)

    text_widget2 = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=6)
    text_widget2.insert(tk.END, paragraph2)
    text_widget2.configure(state='disabled')  # Make the text widget read-only
    text_widget2.pack(padx=10, pady=5)

    # Create a separator between sections
    separator2 = tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN)
    separator2.pack(fill=tk.X, padx=5, pady=5)

    # Display the score in a label
    score_label = tk.Label(root, text=f"Formality score: {score}", font=("Helvetica", 12))
    score_label.pack(padx=10, pady=5)

    # Run the main loop
    root.mainloop()

