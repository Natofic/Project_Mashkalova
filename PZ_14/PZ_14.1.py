import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Certificate Self Service Portal")
root.geometry("700x700")
root.configure(bg='#f0f0f0')
root.resizable(False, False)

label_title = tk.Label(
    root,
    text="Certificate Self Service Portal",
    font=("Arial", 24, "bold"),
    bg='#f0f0f0',
    fg='#333333',
    anchor='w'
)
label_title.pack(pady=(30, 10), padx=40, fill='x')

label_subtitle = tk.Label(
    root,
    text="Fill out the form to get a certificate.",
    font=("Arial", 11),
    bg='#f0f0f0',
    fg='#666666',
    anchor='w'
)
label_subtitle.pack(pady=(0, 20), padx=40, fill='x')

form_frame = tk.Frame(root, bg='#f0f0f0')
form_frame.pack(fill='both', expand=True, padx=40, pady=10)

frame_requester = tk.Frame(form_frame, bg='#f0f0f0')
frame_requester.pack(fill='x', pady=8)

label_requester = tk.Label(
    frame_requester,
    text="Requester",
    font=("Arial", 9, "bold"),
    bg='#f0f0f0',
    fg='#333333',
    width=15,
    anchor='e'
)
label_requester.pack(side='left', padx=(0, 10))

entry_requester = tk.Entry(
    frame_requester,
    font=("Arial", 10),
    bg='white',
    relief='solid',
    bd=1
)
entry_requester.pack(side='left', fill='x', expand=True, ipady=5)
entry_requester.insert(0, "firstname lastname")

frame_short_name = tk.Frame(form_frame, bg='#f0f0f0')
frame_short_name.pack(fill='x', pady=8)

label_short_name = tk.Label(
    frame_short_name,
    text="Short Name",
    font=("Arial", 9, "bold"),
    bg='#f0f0f0',
    fg='#333333',
    width=15,
    anchor='e'
)
label_short_name.pack(side='left', padx=(0, 10))

entry_short_name = tk.Entry(
    frame_short_name,
    font=("Arial", 10),
    bg='white',
    relief='solid',
    bd=1
)
entry_short_name.pack(side='left', fill='x', expand=True, ipady=5)
entry_short_name.insert(0, "asdf")

frame_email = tk.Frame(form_frame, bg='#f0f0f0')
frame_email.pack(fill='x', pady=8)

label_email = tk.Label(
    frame_email,
    text="Email",
    font=("Arial", 9, "bold"),
    bg='#f0f0f0',
    fg='#333333',
    width=15,
    anchor='e'
)
label_email.pack(side='left', padx=(0, 10))

entry_email = tk.Entry(
    frame_email,
    font=("Arial", 10),
    bg='white',
    relief='solid',
    bd=1
)
entry_email.pack(side='left', fill='x', expand=True, ipady=5)
entry_email.insert(0, "mail@mail.com")

frame_organization = tk.Frame(form_frame, bg='#f0f0f0')
frame_organization.pack(fill='x', pady=8)

label_organization = tk.Label(
    frame_organization,
    text="Organization",
    font=("Arial", 9, "bold"),
    bg='#f0f0f0',
    fg='#333333',
    width=15,
    anchor='e'
)
label_organization.pack(side='left', padx=(0, 10))

entry_organization = tk.Entry(
    frame_organization,
    font=("Arial", 10),
    bg='white',
    relief='solid',
    bd=1
)
entry_organization.pack(side='left', fill='x', expand=True, ipady=5)
entry_organization.insert(0, "Organization")

frame_country = tk.Frame(form_frame, bg='#f0f0f0')
frame_country.pack(fill='x', pady=8)

label_country = tk.Label(
    frame_country,
    text="Country",
    font=("Arial", 9, "bold"),
    bg='#f0f0f0',
    fg='#333333',
    width=15,
    anchor='e'
)
label_country.pack(side='left', padx=(0, 10))

combo_country = ttk.Combobox(
    frame_country,
    font=("Arial", 10),
    state='readonly'
)
countries = ["Austria", "Germany", "France", "USA", "Russia", "China", "Japan", "UK"]
combo_country['values'] = countries
combo_country.current(0)
combo_country.pack(side='left', fill='x', expand=True, ipady=5)

frame_ipv4 = tk.Frame(form_frame, bg='#f0f0f0')
frame_ipv4.pack(fill='x', pady=8)

label_ipv4 = tk.Label(
    frame_ipv4,
    text="IPv4 Address",
    font=("Arial", 9, "bold"),
    bg='#f0f0f0',
    fg='#333333',
    width=15,
    anchor='e'
)
label_ipv4.pack(side='left', padx=(0, 10))

entry_ipv4 = tk.Entry(
    frame_ipv4,
    font=("Arial", 10),
    bg='white',
    relief='solid',
    bd=1
)
entry_ipv4.pack(side='left', fill='x', expand=True, ipady=5)
entry_ipv4.insert(0, "127.0.0.1")

frame_hostname = tk.Frame(form_frame, bg='#f0f0f0')
frame_hostname.pack(fill='x', pady=8)

label_hostname = tk.Label(
    frame_hostname,
    text="Hostname",
    font=("Arial", 9, "bold"),
    bg='#f0f0f0',
    fg='#333333',
    width=15,
    anchor='e'
)
label_hostname.pack(side='left', padx=(0, 10))

entry_hostname = tk.Entry(
    frame_hostname,
    font=("Arial", 10),
    bg='white',
    relief='solid',
    bd=1
)
entry_hostname.pack(side='left', fill='x', expand=True, ipady=5)
entry_hostname.insert(0, "host")

frame_fqdn = tk.Frame(form_frame, bg='#f0f0f0')
frame_fqdn.pack(fill='x', pady=8)

label_fqdn = tk.Label(
    frame_fqdn,
    text="FQDN",
    font=("Arial", 9, "bold"),
    bg='#f0f0f0',
    fg='#333333',
    width=15,
    anchor='e'
)
label_fqdn.pack(side='left', padx=(0, 10))

entry_fqdn = tk.Entry(
    frame_fqdn,
    font=("Arial", 10),
    bg='white',
    relief='solid',
    bd=1
)
entry_fqdn.pack(side='left', fill='x', expand=True, ipady=5)
entry_fqdn.insert(0, "host.domain.tld")

frame_description = tk.Frame(form_frame, bg='#f0f0f0')
frame_description.pack(fill='x', pady=8)

label_description = tk.Label(
    frame_description,
    text="Description",
    font=("Arial", 9, "bold"),
    bg='#f0f0f0',
    fg='#333333',
    width=15,
    anchor='ne'
)
label_description.pack(side='left', padx=(0, 10))

text_frame = tk.Frame(frame_description, bg='#f0f0f0')
text_frame.pack(side='left', fill='both', expand=True)

text_description = tk.Text(
    text_frame,
    font=("Arial", 10),
    height=5,
    bg='white',
    relief='solid',
    bd=1,
    wrap='word'
)
text_description.pack(fill='both', expand=True)
text_description.insert('1.0', "desc")

button_frame = tk.Frame(form_frame, bg='#f0f0f0')
button_frame.pack(fill='x', pady=(20, 10))

empty_label = tk.Label(button_frame, text="", width=15, bg='#f0f0f0')
empty_label.pack(side='left', padx=(0, 10))

submit_button = tk.Button(
    button_frame,
    text="Submit Form",
    font=("Arial", 11, "bold"),
    bg='#3182ce',
    fg='white',
    activebackground='#2c5282',
    activeforeground='white',
    relief='flat',
    padx=20,
    pady=10,
    cursor='hand2'
)
submit_button.pack(side='left')

root.mainloop()