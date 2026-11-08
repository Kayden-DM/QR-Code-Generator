import qrcode
import customtkinter as ctk
from tkinter import filedialog

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

img_qr = None

def make():
    global img_qr
    data = entry.get().strip()
    if not data:
        status.configure(text="Put something in first")
        return
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,
                       box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img_qr = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    pic = ctk.CTkImage(light_image=img_qr, dark_image=img_qr, size=(250, 250))
    preview.configure(image=pic, text="")
    preview._image = pic
    save_btn.configure(state="normal")
    status.configure(text="")

def save():
    if not img_qr:
        return
    path = filedialog.asksaveasfilename(defaultextension=".png",
                                        filetypes=[("PNG", "*.png")],
                                        initialfile="qr_code.png")
    if path:
        img_qr.save(path)
        status.configure(text=f"Saved: {path.split('/')[-1]}")

root = ctk.CTk()
root.title("QR Code Generator")
root.geometry("400x500")

ctk.CTkLabel(root, text="QR Code Generator", font=("Arial", 24, "bold")).pack(pady=(20, 10))

entry = ctk.CTkEntry(root, placeholder_text="Text or URL...")
entry.pack(pady=5, padx=20, fill="x")
ctk.CTkButton(root, text="Generate", width=120, command=make).pack(pady=10)

preview = ctk.CTkLabel(root, text="", width=250, height=250)
preview.pack(pady=10)

save_btn = ctk.CTkButton(root, text="Save to file", width=120,
                         command=save, state="disabled")
save_btn.pack(pady=10)

status = ctk.CTkLabel(root, text="")
status.pack(pady=(5, 0))

root.mainloop()