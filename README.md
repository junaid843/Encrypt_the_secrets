# 🔐 Secret Code Encrypter & Decrypter

This is a simple **Streamlit web application** that allows users to **encrypt and decrypt secret messages** using a password.  
The application uses **Fernet encryption** from the `cryptography` library to ensure secure message handling.  
No data is stored anywhere; everything runs locally on your system.

---

## ✨ Features

- Encrypt plain text messages using a secret password  
- Decrypt encrypted messages using the same password  
- Password-based key generation  
- Clean and beginner-friendly Streamlit UI  
- Fully local and secure (no database, no logging)

---

## 🛠️ Technologies Used

Python, Streamlit, Cryptography (Fernet), Base64 Encoding

---

## 🚀 Setup & Usage

First, install the required libraries:

## 🔐 Security Notes

---

The encryption key is derived from the password provided by the user.
If the password is lost, the encrypted message cannot be recovered.
No messages or passwords are saved or transmitted anywhere.

---
## 📌 Use Cases

Secure text sharing

Learning basic encryption concepts

Streamlit practice project

Cybersecurity demo application
