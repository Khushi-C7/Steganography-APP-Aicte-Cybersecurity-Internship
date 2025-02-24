# Image Stegnography

# overview

🚀 Features
Encrypt Secret Messages into images without noticeable changes.
Decrypt Messages Securely with a password. 
Wrong Password Protection: If the password is incorrect, the image remains unchanged, preventing detection.
Download Encrypted Images for secure storage and sharing.

🏗️ Technologies Used
Python (Backend Logic)
Streamlit (User Interface)
Pillow (Image Processing)
NumPy (Efficient Data Handling)

# 🛠️ Usage Guide
## 🔐 Encrypting a Message
Open the app.
Select Encrypt Message from the sidebar.
Upload an image (.jpg or .png).
Enter the secret message.
Set an encryption password.
Click Encrypt to embed the message.
Download the encrypted image.
## 🔓 Decrypting a Message
Open the app.
Select Decrypt Message from the sidebar.
Upload the encrypted image.
Enter the correct decryption password.
Click Decrypt to reveal the hidden message.
## 📥 Installation Guide
### 🔹 1️⃣ Install Dependencies
```bash
pip install pyngrok streamlit
```
### 🔹 2️⃣ Run the Application
```bash
streamlit run app.py &>/dev/null &
```
🔍 How It Works

Encoding Process:
The secret message is converted into binary.
A hashed password is added for authentication.
The binary data is hidden in the least significant bit (LSB) of the image pixels.
Decoding Process:
Extracts binary data from the image.
Verifies the password before revealing the message.
If the password is incorrect, no secret message is displayed.

🔐 Security Measures
Password Protection: Messages can only be decrypted with the correct password.
Stealth Mode: Without the correct password, the image appears unchanged.
End Marker: Prevents over-reading of hidden data, ensuring data integrity.
