import streamlit as st
import requests

API_URL = "http://flask-app:5000/users"

st.title("CRUD operation")

st.sidebar.title("Navigation")
options = st.sidebar.radio("Select an action:", ["Create User", "View Users", "Update User", "Delete User"])

if options == "Create User":
    st.subheader("Create User")
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Create User"):
        if name and email and password:
            response = requests.post(API_URL, json={"name": name, "email": email, "password": password})
            if response.status_code == 201:
                st.success(f"User created successfully! User ID: {response.json()['id']}")
            else:
                st.error("Error creating user: " + response.json().get('error', 'Unknown error'))

elif options == "View Users":
    st.subheader("User List")
    response = requests.get(API_URL)
    if response.status_code == 200:
        users = response.json()
        if users:
            user_data = []
            for user in users:
                user_data.append({
                    "ID": user['_id'], 
                    "Name": user['name'], 
                    "Email": user['email']
                })
            st.table(user_data) 
        else:
            st.write("No users found.")
    else:
        st.error("Error fetching users: " + response.json().get('error', 'Unknown error'))

elif options == "Update User":
    st.subheader("Update User")
    user_id = st.text_input("User ID to update")
    name = st.text_input("New Name")
    email = st.text_input("New Email")

    if st.button("Update User"):
        if user_id and (name or email):
            update_data = {}
            if name:
                update_data["name"] = name
            if email:
                update_data["email"] = email
            
            response = requests.put(f"{API_URL}/{user_id}", json=update_data)
            if response.status_code == 200:
                st.success("User updated successfully!")
            else:
                st.error("Error updating user: " + response.json().get('error', 'Unknown error'))
                
elif options == "Delete User":
    st.subheader("Delete User")
    user_id = st.text_input("User ID to delete")

    if st.button("Delete User"):
        if user_id:
            response = requests.delete(f"{API_URL}/{user_id}")
            if response.status_code == 200:
                st.success("User deleted successfully!")
            else:
                st.error("Error deleting user: " + response.json().get('error', 'Unknown error'))
