# Simple application to send Email using Python tkinter

import tkinter as tk
from tkinter import messagebox
import smtplib

def send_email():
    sender_email = sender_entry.get()
    sender_password = password_entry.get()
    recipient_email = recipient_entry.get()
    subject = subject_entry.get()
    message_body = message_text.get("1.0", tk.END)

    if not sender_email or not sender_password or not recipient_email or not subject or not message_body.strip():
        messagebox.showwarning("Input Error", "All fields are required.")
        return
    
    message = f"Subject: {subject}\n\n{message_body}"
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()

        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message)
        server.quit()
        
        messagebox.showinfo("Success", "Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        messagebox.showerror("Authentication Error", "Failed to login. Please check your email or password.")
    except smtplib.SMTPException as e:
        messagebox.showerror("SMTP Error", f"Failed to send email: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

window = tk.Tk()
window.title("Email Sender")
window.geometry("400x500")
window.configure(bg = "#2C3E50")

entry_bg_color = "#ECF0F1"
button_bg_color = "#2980B9"
button_fg_color = "#FFFFFF"
label_fg_color = "#ECF0F1"
text_bg_color = "#ECF0F1"

tk.Label(window, text = "Sender Email:", bg = "#2C3E50", fg = label_fg_color).pack(pady = 5)
sender_entry = tk.Entry(window, width = 40, bg = entry_bg_color, fg = "black", highlightthickness = 1, bd = 0)
sender_entry.pack(pady = 5)

tk.Label(window, text = "Password:", bg = "#2C3E50", fg = label_fg_color).pack(pady = 5)
password_entry = tk.Entry(window, show = '*', width = 40, bg = entry_bg_color, fg = "black", highlightthickness = 1, bd = 0)
password_entry.pack(pady = 5)

tk.Label(window, text = "Recipient Email:", bg = "#2C3E50", fg = label_fg_color).pack(pady = 5)
recipient_entry = tk.Entry(window, width = 40, bg = entry_bg_color, fg = "black", highlightthickness = 1, bd = 0)
recipient_entry.pack(pady = 5)

tk.Label(window, text = "Subject:", bg = "#2C3E50", fg = label_fg_color).pack(pady = 5)
subject_entry = tk.Entry(window, width = 40, bg = entry_bg_color, fg = "black", highlightthickness = 1, bd = 0)
subject_entry.pack(pady = 5)

tk.Label(window, text = "Message:", bg = "#2C3E50", fg = label_fg_color).pack(pady = 5)
message_text = tk.Text(window, width = 40, height = 10, bg = text_bg_color, fg = "black", highlightthickness = 1, bd = 0)
message_text.pack(pady = 5)

send_button = tk.Button(window, text = "Send Email", command = send_email, width = 20, bg = button_bg_color, fg = button_fg_color, bd = 0, highlightthickness = 0, activebackground = "#3498DB", activeforeground = button_fg_color)
send_button.pack(pady = 20)

window.mainloop()
