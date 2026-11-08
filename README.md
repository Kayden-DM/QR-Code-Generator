## QR Code Generator
A desktop QR code generator built with CustomTkinter and the qrcode library. It takes text or a URL, renders a QR code preview in the window, and lets you save the result as a PNG file.

## Features
Input Field — A CTkEntry with placeholder text where the user types the text or URL to encode.

Generate Button — Builds a QR code from the input and displays it in a 250×250 preview.

High Error Correction — Uses ERROR_CORRECT_H so the code stays scannable even if partially damaged or covered.

Live Preview — The generated QR image is shown inline via CTkImage, with matching light and dark variants.

Save to File — Opens a save dialog and writes the QR code as a .png, defaulting to qr_code.png.

Empty Input Guard — Shows "Put something in first" and skips generation if the input is blank.

Disabled Save Until Ready — The Save button stays disabled until a QR code has been generated.

Custom Theme — Dark appearance mode with the blue default color theme applied to all CustomTkinter widgets.

## Technologies Used
| Technology | Purpose |
|---|---|
| Python | Application logic |
| `customtkinter` | Window, entry, buttons, labels, image preview |
| `qrcode` | Generates the QR code matrix and image |
| `qrcode.constants` | Sets the error correction level |
| `PIL` (Pillow) | Converts the QR image to RGB for display and saving |
| `filedialog` | Native save dialog for exporting the PNG |
| `CTkImage` | Renders the QR preview in the window |
## How to Use It
Install Python 3.8 or newer from python.org and make sure it's added to your PATH.

Install the dependencies by running pip install qrcode customtkinter pillow.

Save the code as qr_generator.py.

Open a terminal in the folder containing the file.

Run python qr_generator.py.

Type text or a URL into the entry, press Generate to see the preview, then press Save to file to export it as a PNG.

## Improvements
Add a custom filename field — the save dialog defaults to qr_code.png; an entry for the filename would let the user set it before saving.

Add an error correction selector — the level is hardcoded to ERROR_CORRECT_H; a dropdown for L/M/Q/H would let users trade redundancy for smaller, denser codes.

Show the encoded content on save — the status label only shows the filename; displaying the encoded text alongside it would make it easier to confirm what was saved.

Allow colour customisation — fill_color and back_color are fixed to black and white; exposing them would let users generate branded QR codes.
