import tkinter as tk


def main():
    window = tk.Tk()
    window.title("Sprint 0 GUI Demo")
    window.geometry("400x350")

    # --- TEXT ---
    title = tk.Label(window, text="Sprint 0 GUI Demo",
                     font=("Arial", 16, "bold"))
    title.pack(pady=10)

    subtitle = tk.Label(window, text="By Muhammad - CS 449",
                        font=("Arial", 10))
    subtitle.pack()

    # --- LINES ---
    # A horizontal line drawn on a Canvas.
    canvas = tk.Canvas(window, width=350, height=40, highlightthickness=0)
    canvas.pack(pady=10)
    canvas.create_line(10, 20, 340, 20, fill="black", width=2)
    canvas.create_line(10, 30, 340, 30, fill="gray", width=1)

    # --- RADIO BUTTONS ---
    tk.Label(window, text="Pick a color:",
             font=("Arial", 11, "bold")).pack()

    color_choice = tk.StringVar(value="Red")
    for color in ["Red", "Green", "Blue"]:
        tk.Radiobutton(window, text=color, variable=color_choice,
                       value=color).pack(anchor="w", padx=100)

    # --- CHECK BOX ---
    agree = tk.BooleanVar()
    tk.Checkbutton(window, text="I agree to the terms",
                   variable=agree).pack(pady=10)

    # --- BUTTON that shows what was selected ---
    result = tk.Label(window, text="", font=("Arial", 10), fg="blue")
    result.pack()

    def show_selection():
        result.config(
            text=f"Color: {color_choice.get()} | Agreed: {agree.get()}"
        )

    tk.Button(window, text="Show Selection",
              command=show_selection).pack(pady=5)

    window.mainloop()


if __name__ == "__main__":
    main()