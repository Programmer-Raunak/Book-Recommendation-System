# 📚 Book Recommendation System  

> A Machine Learning based project that recommends similar books to users based on their interests and preferences.  

---

## 🧠 Overview  
The **Book Recommendation System** suggests books similar to the one selected by the user.  
It uses **Cosine Similarity** and a **Content-Based Filtering Algorithm** to recommend books from a dataset of popular titles.  
The project includes a simple and interactive **Streamlit** web app for better user experience.  

---

## 🚀 Features  
✅ Recommends top similar books instantly  
✅ Uses pre-trained similarity model for fast results  
✅ Clean and interactive Streamlit UI  
✅ Data preprocessed for accurate recommendations  
✅ Easy to deploy on any platform (Render, Streamlit Cloud, etc.)

---

## 🧩 Technologies Used  
- **Python 3**  
- **Pandas**  
- **NumPy**  
- **Scikit-Learn**  
- **Streamlit**  
- **Joblib**

---


---

## ⚙️ Steps Followed to Build the Project  

### 🔹 Step 1: Data Collection  
- Collected **Books Dataset** (from Kaggle / Book-Crossing).  
- Cleaned and merged book, rating, and user datasets.  

### 🔹 Step 2: Data Preprocessing  
- Created a **pivot table** (users vs books).  
- Filtered active users and popular books for better quality data.  

### 🔹 Step 3: Model Building  
- Calculated **Cosine Similarity** between books.  
- Created a function to fetch top N similar books.  

### 🔹 Step 4: Model Saving  
- Used **Pickle** to save processed data and similarity matrix.  

### 🔹 Step 5: Streamlit UI Development  
- Built an app with:
  - Dropdown for selecting a book  
  - Display section for top recommended books  
  - (Optional) Book cover images  

### 🔹 Step 6: Deployment  
- Added all dependencies in `requirements.txt`.  
- Deployed the app on **Render / Streamlit Cloud**.

---

## 🧑‍💻 How to Run Locally  

```bash
# Clone the repository
git clone https://github.com/Programmer-Raunak/Book-Recommendation-System.git

# Navigate to folder
cd Book-Recommendation-System

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run streamlitapp.py
