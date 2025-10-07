import streamlit as st
import pickle

# Load DataFrame
top_books = pickle.load(open('top_books.pkl', 'rb'))

st.set_page_config(page_title="Top Rated Books", layout="wide")

# Hide hamburger menu and footer

# Page Title
st.title("📚 Top Rated Books")
st.subheader("Explore the top 50 books based on ratings and popularity")

# Columns from your dataset
title_col = "Book-Title"
author_col = "Book-Author"
img_col = "Image-URL-L"
rating_count_col = "num_ratings"
avg_rating_col = "avg_rating"

# Take top 50 books
top_books = top_books.head(50)

# Grid settings
cols_per_row = 5

# Styling for better UI
st.markdown("""
<style>

.book-card:hover {
    transform: scale(1.03);
}
.book-title {
    font-weight: bold;
    color: #ffffff;
}
.book-author {
    color: #555;
    font-size: 14px;
}
.book-rating {
    color: #e3b341;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# Display books in grid format
for i in range(0, len(top_books), cols_per_row):
    cols = st.columns(cols_per_row)
    for j in range(cols_per_row):
        if i + j < len(top_books):
            book = top_books.iloc[i + j]
            with cols[j]:

                st.image(book[img_col], width=120)
                st.markdown(f"<div class='book-title'>{book[title_col]}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='book-author'>👨‍💻 {book[author_col]}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='book-rating'>⭐ {round(book[avg_rating_col], 2)} | {book[rating_count_col]} ratings</div>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
