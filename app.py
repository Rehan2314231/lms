# from LMS_Logic import *
# import streamlit as st
# st.title("LMS app")

# menu = ["Add Member","Add Book","View Data"]
# choice = st.sidebar.selectbox("Menu", menu)
# if choice == "Add Member":
#     st.subheader("Add Member Form")
#     member_name = st.text_input("Enter Name")
#     if st.button("Add Member"):
#         st.success(f"Added Member: {member_name}")
#         # Adding Member to the DataBase
# if choice == "Add Book":
#     st.subheader("Add Book Form")
#     book_title = st.text_input("Enter Book")
#     author_name = st.text_input("Author Name")
#     publication_year = st.text_input("Publication Year")
#     num_copies = st.number_input("Number of Copies")
#     if st.button("Add Book"):
#         book = Book(book_title,author_name,publication_year,num_copies)
#         book.addToDB()
#         st.success(f"Added Book: {book_title}")
#         # Adding Book to the DataBase
# if choice == "View Data":
#     st.subheader("View Data")
#     st.success(f"Data:")
#     # Add logic to retreive data from the DB and show it in the UI
from LMS_Logic import *
import streamlit as st

st.title("LMS app")

menu = ["Members", "Books", "View Data"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Members":
    st.subheader("Member Management")
    # member_name = st.text_input("Enter Name")
    member_type = st.sidebar.radio(
    "Select Member Type",
    ["Add Member", "Update Member", "Show Members", "Delete a member"]
)
    # if st.button("Member"):
    #     st.success(f"Added Member: {member_name}")
    #     # Display radio buttons in the sidebar for member type selection

    #     st.sidebar.info(f"Member Type Selected: {member_type}")
    #     # Additional logic to process the member type can be added here

elif choice == "Add Book":
    st.subheader("Add Book Form")
    book_title = st.text_input("Enter Book")
    author_name = st.text_input("Author Name")
    publication_year = st.text_input("Publication Year")
    num_copies = st.number_input("Number of Copies")
    if st.button("Add Book"):
        book = Book(book_title, author_name, publication_year, num_copies)
        book.addToDB()
        st.success(f"Added Book: {book_title}")

elif choice == "View Data":
    st.subheader("View Data")
    st.success("Data:")
    # Add logic to retrieve and display data from the database



# show 4 diffrent forms for 4 diffrent radio buttons inside members