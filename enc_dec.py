import streamlit as st
from cryptography.fernet import Fernet
import base64

# --- Functions ---

def generate_key_from_password(password: str):
    """Generates a 32-byte key from a string password to use with Fernet."""
    # Fernet keys must be 32 url-safe base64-encoded bytes.
    # We pad/slice the password to make it fit the format.
    key = password.ljust(32)[:32].encode()
    return base64.urlsafe_b64encode(key)

def encrypt_text(text, password):
    key = generate_key_from_password(password)
    f = Fernet(key)
    token = f.encrypt(text.encode())
    return token.decode()

def decrypt_text(token, password):
    try:
        key = generate_key_from_password(password)
        f = Fernet(key)
        decoded_text = f.decrypt(token.encode())
        return decoded_text.decode()
    except Exception:
        return "❌ Invalid Key or Corrupted Code!"

# --- Streamlit UI ---

st.set_page_config(page_title="Secret Code Encrypter", page_icon="🔐")

st.title("🔐 Secret Code Encrypter & Decrypter")
st.write("Secure your messages with a password before sending them.")

# Sidebar for instructions
st.sidebar.header("How to use:")
st.sidebar.info(
    "1. Choose a Mode (Encrypt/Decrypt).\n"
    "2. Enter your message.\n"
    "3. Set a Secret Password (don't forget it!).\n"
    "4. Share the result with your friend!"
)

# App Tabs
tab1, tab2 = st.tabs(["Encrypt 🔒", "Decrypt 🔓"])

with tab1:
    st.header("Encrypt a Message")
    message_to_encrypt = st.text_area("Enter the plain text message:", placeholder="Hello friend...")
    pass_encrypt = st.text_input("Set a Secret Password:", type="password", key="p1")
    
    if st.button("Generate Secret Code"):
        if message_to_encrypt and pass_encrypt:
            result = encrypt_text(message_to_encrypt, pass_encrypt)
            st.success("Message Encrypted Successfully!")
            st.code(result, language="text")
            st.info("Copy the code above and send it to your friend.")
        else:
            st.warning("Please enter both a message and a password.")

with tab2:
    st.header("Decrypt a Message")
    code_to_decrypt = st.text_area("Paste the Secret Code here:", placeholder="gAAAAABl...")
    pass_decrypt = st.text_input("Enter the Secret Password:", type="password", key="p2")
    
    if st.button("Unlock Message"):
        if code_to_decrypt and pass_decrypt:
            decrypted = decrypt_text(code_to_decrypt, pass_decrypt)
            if "❌" in decrypted:
                st.error(decrypted)
            else:
                st.success("Message Decrypted!")
                st.subheader("Original Message:")
                st.write(decrypted)
        else:
            st.warning("Please enter both the code and the password.")

st.divider()
st.caption("Built with Streamlit & Cryptography Library. No data is stored on our servers.")