import tkinter as tk
from tkinter import ttk, messagebox


class SignUpForm(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Sign Up Form")
        self.geometry("500x700")
        self.resizable(False, False)
        self.configure(bg="#2C2F3D")

        self._create_widgets()

    def _create_widgets(self):

        header_frame = tk.Frame(self, bg="#E67E22", height=40)
        header_frame.pack(fill=tk.X)

        label_header = tk.Label(
            header_frame,
            text="Sign Up",
            font=("Arial", 16, "bold"),
            bg="#E67E22",
            fg="white",
            anchor="w",
            padx=15
        )
        label_header.pack(side=tk.LEFT, fill=tk.Y)

        form_frame = tk.Frame(self, bg="#2C2F3D")
        form_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        form_frame.columnconfigure(1, weight=1)

        self._create_labeled_entry(form_frame, "First Name", "first_name", row=0)

        self._create_labeled_entry(form_frame, "Last Name", "last_name", row=1)

        self._create_labeled_entry(form_frame, "Screen Name", "screen_name", row=2)

        self._create_date_of_birth_fields(form_frame, row=3)

        self._create_gender_field(form_frame, row=4)

        self._create_country_field(form_frame, row=5)

        self._create_labeled_entry(form_frame, "E-mail", "email", row=6)

        self._create_labeled_entry(form_frame, "Phone", "phone", row=7)

        self._create_labeled_entry(form_frame, "Password", "password", show="*", row=8)

        self._create_labeled_entry(form_frame, "Confirm Password", "confirm_password", show="*", row=9)

        self._create_checkbox(form_frame, row=10)

        footer_frame = tk.Frame(self, bg="#E67E22", height=50)
        footer_frame.pack(fill=tk.X)

        btn_submit = tk.Button(
            footer_frame,
            text="submit",
            font=("Arial", 11, "bold"),
            bg="#2ECC71",
            fg="white",
            activebackground="#27AE60",
            relief=tk.FLAT,
            padx=15,
            pady=5,
            command=self._on_submit
        )
        btn_submit.pack(side=tk.RIGHT, padx=(10, 5))

        btn_cancel = tk.Button(
            footer_frame,
            text="Cancel",
            font=("Arial", 11, "bold"),
            bg="#E74C3C",
            fg="white",
            activebackground="#C0392B",
            relief=tk.FLAT,
            padx=15,
            pady=5,
            command=self._on_cancel
        )
        btn_cancel.pack(side=tk.RIGHT, padx=5)

    def _create_labeled_entry(self, parent, label_text, var_name, show=None, row=0):
        label = tk.Label(
            parent,
            text=label_text,
            font=("Arial", 10, "bold"),
            bg="#2C2F3D",
            fg="#FFD700",
            anchor="e",
            width=15
        )
        label.grid(row=row, column=0, padx=(0, 10), pady=8, sticky="e")

        entry = tk.Entry(
            parent,
            font=("Arial", 10),
            bg="white",
            relief=tk.SOLID,
            bd=1,
            show=show
        )
        entry.grid(row=row, column=1, sticky="ew", pady=8, ipady=5)
        setattr(self, f"entry_{var_name}", entry)

    def _create_date_of_birth_fields(self, parent, row):
        label = tk.Label(
            parent,
            text="Date of Birth",
            font=("Arial", 10, "bold"),
            bg="#2C2F3D",
            fg="#FFD700",
            anchor="e",
            width=15
        )
        label.grid(row=row, column=0, padx=(0, 10), pady=8, sticky="e")

        combo_month = ttk.Combobox(parent, state="readonly", width=8)
        combo_month['values'] = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        combo_month.current(4)
        combo_month.grid(row=row, column=1, sticky="w", padx=(0, 5), pady=8)
        self.entry_dob_month = combo_month

        combo_day = ttk.Combobox(parent, state="readonly", width=5)
        combo_day['values'] = [str(i) for i in range(1, 32)]
        combo_day.current(4)
        combo_day.grid(row=row, column=1, sticky="w", padx=(50, 5), pady=8)
        self.entry_dob_day = combo_day

        combo_year = ttk.Combobox(parent, state="readonly", width=6)
        years = [str(y) for y in range(1950, 2026)]
        combo_year['values'] = years
        combo_year.current(35)
        combo_year.grid(row=row, column=1, sticky="w", padx=(100, 0), pady=8)
        self.entry_dob_year = combo_year

    def _create_gender_field(self, parent, row):
        label = tk.Label(
            parent,
            text="Gender",
            font=("Arial", 10, "bold"),
            bg="#2C2F3D",
            fg="#FFD700",
            anchor="e",
            width=15
        )
        label.grid(row=row, column=0, padx=(0, 10), pady=8, sticky="e")

        self.gender_var = tk.StringVar(value="Male")

        rb_male = tk.Radiobutton(
            parent,
            text="Male",
            variable=self.gender_var,
            value="Male",
            bg="#2C2F3D",
            fg="#FFD700",
            selectcolor="#2C2F3D",
            activebackground="#2C2F3D"
        )
        rb_male.grid(row=row, column=1, sticky="w", padx=(0, 15), pady=8)

        rb_female = tk.Radiobutton(
            parent,
            text="Female",
            variable=self.gender_var,
            value="Female",
            bg="#2C2F3D",
            fg="#FFD700",
            selectcolor="#2C2F3D",
            activebackground="#2C2F3D"
        )
        rb_female.grid(row=row, column=1, sticky="w", padx=(60, 0), pady=8)

    def _create_country_field(self, parent, row):
        label = tk.Label(
            parent,
            text="Country",
            font=("Arial", 10, "bold"),
            bg="#2C2F3D",
            fg="#FFD700",
            anchor="e",
            width=15
        )
        label.grid(row=row, column=0, padx=(0, 10), pady=8, sticky="e")

        combo_country = ttk.Combobox(parent, state="readonly")
        countries = ["USA", "Canada", "UK", "Germany", "France", "Russia", "China", "Japan"]
        combo_country['values'] = countries
        combo_country.current(0)
        combo_country.grid(row=row, column=1, sticky="ew", pady=8, ipady=5)
        self.entry_country = combo_country

    def _create_checkbox(self, parent, row):
        self.agree_var = tk.BooleanVar(value=False)

        checkbox = tk.Checkbutton(
            parent,
            text="I agree to the Terms of Use",
            variable=self.agree_var,
            bg="#2C2F3D",
            fg="#FFD700",
            selectcolor="#2C2F3D",
            activebackground="#2C2F3D",
            font=("Arial", 9)
        )
        checkbox.grid(row=row, column=1, sticky="w", pady=10, padx=(0, 0))

    def _on_submit(self):
        first_name = self.entry_first_name.get().strip()
        last_name = self.entry_last_name.get().strip()
        screen_name = self.entry_screen_name.get().strip()
        dob_month = self.entry_dob_month.get()
        dob_day = self.entry_dob_day.get()
        dob_year = self.entry_dob_year.get()
        gender = self.gender_var.get()
        country = self.entry_country.get()
        email = self.entry_email.get().strip()
        phone = self.entry_phone.get().strip()
        password = self.entry_password.get()
        confirm_password = self.entry_confirm_password.get()
        agreed = self.agree_var.get()

        errors = []
        if not first_name:
            errors.append("Введите имя.")
        if not last_name:
            errors.append("Введите фамилию.")
        if not screen_name:
            errors.append("Введите экранное имя.")
        if not email or "@" not in email:
            errors.append("Введите корректный email.")
        if len(password) < 6:
            errors.append("Пароль должен быть не менее 6 символов.")
        if password != confirm_password:
            errors.append("Пароли не совпадают.")
        if not agreed:
            errors.append("Вы должны согласиться с условиями использования.")

        if errors:
            messagebox.showerror("Ошибка", "\n".join(errors))
            return

        print("=" * 50)
        print("ДАННЫЕ РЕГИСТРАЦИИ:")
        print(f"Имя: {first_name} {last_name}")
        print(f"Экранное имя: {screen_name}")
        print(f"Дата рождения: {dob_month} {dob_day}, {dob_year}")
        print(f"Пол: {gender}")
        print(f"Страна: {country}")
        print(f"Email: {email}")
        print(f"Телефон: {phone}")
        print(f"Пароль: {'*' * len(password)}")
        print(f"Согласие с условиями: {'Да' if agreed else 'Нет'}")
        print("=" * 50)

        messagebox.showinfo("Успех", "Регистрация прошла успешно!\nПроверьте консоль.")

        self.entry_first_name.delete(0, tk.END)
        self.entry_last_name.delete(0, tk.END)
        self.entry_screen_name.delete(0, tk.END)
        self.entry_dob_month.current(0)
        self.entry_dob_day.current(0)
        self.entry_dob_year.current(0)
        self.gender_var.set("Male")
        self.entry_country.current(0)
        self.entry_email.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)
        self.entry_confirm_password.delete(0, tk.END)
        self.agree_var.set(False)

    def _on_cancel(self):
        self.entry_first_name.delete(0, tk.END)
        self.entry_last_name.delete(0, tk.END)
        self.entry_screen_name.delete(0, tk.END)
        self.entry_dob_month.current(0)
        self.entry_dob_day.current(0)
        self.entry_dob_year.current(0)
        self.gender_var.set("Male")
        self.entry_country.current(0)
        self.entry_email.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)
        self.entry_confirm_password.delete(0, tk.END)
        self.agree_var.set(False)

if __name__ == "__main__":
    app = SignUpForm()
    app.mainloop()