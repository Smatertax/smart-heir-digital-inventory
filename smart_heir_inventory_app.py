import streamlit as st
import pandas as pd

st.set_page_config(page_title="Smart Heir™ - Digital Asset Inventory", layout="wide")

st.title("🔐 Smart Heir™ - Digital Asset Inventory Kit")
st.subheader("Securely document all your digital assets for your family or executor.")

st.markdown("---")

st.header("👤 Owner Information")
full_name = st.text_input("Full Name")
email = st.text_input("Primary Email")
phone = st.text_input("Phone Number")

st.header("🌐 Digital Accounts")
account_types = ["Email", "Banking App", "Crypto Wallet", "Social Media", "Subscription", "Other"]
accounts_data = []

st.markdown("Add each digital account you'd like to include:")

with st.form("add_account"):
    account_type = st.selectbox("Account Type", account_types)
    account_name = st.text_input("Account Name (e.g. Gmail, Coinbase, Netflix)")
    username = st.text_input("Username or Email")
    notes = st.text_area("Access Notes (password location, MFA details, etc.)")
    submit = st.form_submit_button("Add Account")

    if submit:
        accounts_data.append({
            "Type": account_type,
            "Name": account_name,
            "Username": username,
            "Notes": notes
        })

if "accounts" not in st.session_state:
    st.session_state.accounts = []

if submit:
    st.session_state.accounts.append(accounts_data[-1])

if st.session_state.accounts:
    st.subheader("📄 Your Saved Digital Assets")
    df = pd.DataFrame(st.session_state.accounts)
    st.dataframe(df)

    if st.download_button("📥 Download as CSV", data=df.to_csv(index=False).encode(), file_name="digital_assets.csv"):
        st.success("✅ Inventory file downloaded successfully!")

st.markdown("---")
st.header("📲 Emergency Contact Setup")
contact_name = st.text_input("Contact's Full Name")
relationship = st.text_input("Relationship")
contact_email = st.text_input("Contact Email")
contact_notes = st.text_area("Instructions (e.g. access upon death or incapacity)")

if st.button("💾 Save Emergency Contact"):
    st.success("Emergency contact saved. Include in your legal estate documents.")

st.markdown("---")
st.markdown("🔒 **Tip**: Always store your CSV and access instructions in a secure place or upload to a password manager.")
