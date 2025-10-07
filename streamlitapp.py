import streamlit as st


st.set_page_config(page_title="My App", page_icon="📚", layout="wide")

# Hide only Streamlit default menu and footer

# Define the pages
st.sidebar.title("sidebar")
top_rated_book_page = st.Page("top_rated_books.py", title="📚Top Rated Books", icon="📚")
recommendation_system = st.Page("recommendation_book.py", title="📚 Recommendation System", icon="📖")
# Create navigation
pg = st.navigation([top_rated_book_page,recommendation_system])

# Run the selected page
pg.run()
