import streamlit as st
import pickle
st.set_page_config(page_title="Recommendation System", page_icon="📚", layout="wide")

# Hide hamburger menu and footer
hide_streamlit_style = """
<style>

footer {visibility: hidden;}

</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

books_list = pickle.load(open('book_list.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity.pkl', 'rb'))
pt = pickle.load(open('pivot_table.pkl','rb'))
st.title("Books Recommendation System")


def recommend(book_name):
    import numpy as np

    # book ka index fetch karo
    index = np.where(pt.index == book_name)[0][0]

    # top 5 similar books (excluding itself)
    similar_items = sorted(list(enumerate(similarity_scores[index])),
                           key=lambda x: x[1], reverse=True)[1:6]

    data = []
    for a in similar_items:
        data.append(books_list[books_list['Book-Title'] == pt.index[a[0]]].drop_duplicates('Book-Title')['Book-Title'].values[0])

    return data



selected_book = st.selectbox("Select a Book",pt.index.tolist())

Recommend_btn = st.button("Recommend")




if Recommend_btn:
    suggested_books = recommend(selected_book)

    cols = st.columns(5)

    for i, col in enumerate(cols):
        with col:
            book_row = books_list[books_list['Book-Title'] == suggested_books[i]].drop_duplicates('Book-Title')
            image_url = book_row['Image-URL-L'].values[0]

            st.image(image_url, use_container_width=True)
            st.write(suggested_books[i])




