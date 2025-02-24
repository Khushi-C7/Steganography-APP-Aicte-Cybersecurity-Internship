import cv2
import numpy as np
import streamlit as st
from io import BytesIO
from PIL import Image

# Function to encrypt the image
def encrypt_image(image, password):
    img = np.array(image)  # Convert to NumPy array
    h, w, _ = img.shape

    np.random.seed(sum(ord(c) for c in password))  # Generate key from password
    key = np.random.randint(0, 256, size=(h, w, 3), dtype=np.uint8)  # Generate key of same shape

    encrypted_img = cv2.bitwise_xor(img, key)  # XOR operation to encrypt

    return Image.fromarray(encrypted_img), key  # Convert back to PIL image

# Function to decrypt the image
def decrypt_image(encrypted_image, key):
    enc_img = np.array(encrypted_image)  # Convert to NumPy array
    decrypted_img = cv2.bitwise_xor(enc_img, key)  # Reverse XOR operation

    return Image.fromarray(decrypted_img)  # Convert back to PIL image

# Streamlit UI
st.title("🔒 Image Encryption & Decryption")

option = st.radio("Choose an option:", ["Encrypt", "Decrypt"])

if option == "Encrypt":
    uploaded_file = st.file_uploader("Upload an image (JPG, PNG)", type=["jpg", "png"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Original Image", use_column_width=True)

        password = st.text_input("Enter a passcode:", type="password")

        if st.button("Encrypt"):
            encrypted_image, key = encrypt_image(image, password)
            st.image(encrypted_image, caption="Encrypted Image", use_column_width=True)

            # Save encrypted image
            img_io = BytesIO()
            encrypted_image.save(img_io, format="PNG")
            img_io.seek(0)

            st.download_button(
                label="Download Encrypted Image",
                data=img_io,
                file_name="encrypted_image.png",
                mime="image/png"
            )

            # Save key as bytes
            key_io = BytesIO()
            np.save(key_io, key)
            key_io.seek(0)

            st.download_button(
                label="Download Encryption Key",
                data=key_io,
                file_name="encryption_key.npy",
                mime="application/octet-stream"
            )

elif option == "Decrypt":
    encrypted_file = st.file_uploader("Upload the encrypted image", type=["png", "jpg"])
    key_file = st.file_uploader("Upload the encryption key (.npy)", type=["npy"])

    if encrypted_file and key_file:
        encrypted_img = Image.open(encrypted_file)

        key_io = BytesIO(key_file.read())
        key = np.load(key_io)

        if st.button("Decrypt"):
            decrypted_image = decrypt_image(encrypted_img, key)
            st.image(decrypted_image, caption="Decrypted Image", use_column_width=True)

            # Save decrypted image
            img_io = BytesIO()
            decrypted_image.save(img_io, format="PNG")
            img_io.seek(0)

            st.download_button(
                label="Download Decrypted Image",
                data=img_io,
                file_name="decrypted_image.png",
                mime="image/png"
            )
