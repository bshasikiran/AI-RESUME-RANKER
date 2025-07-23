# 🧠 AI Resume Ranker – Match Resumes to Job Descriptions using LLMs + Vector Search

Sure! Here's your **full-fledged professional `README.md` file** for the **AI Resume Ranker** project, suitable for GitHub and project portfolios:

---

```markdown
# 🧠 AI Resume Ranker – Rank Resumes Based on Job Description using OpenAI + Pinecone

AI Resume Ranker is an AI-powered resume screening tool that matches and ranks resumes (PDFs) against a given job description using powerful embeddings from OpenAI and vector similarity search via Pinecone. This tool is designed to help HR professionals, recruiters, and job-seekers efficiently identify the best resume fits with ease.

---

## 🚀 Live Demo

> Coming soon (or replace this with Hugging Face/Streamlit Cloud link if deployed)

---

## 📸 Project Preview

![AI Resume Ranker UI Preview](https://via.placeholder.com/1000x500.png?text=Screenshot+Preview+Here)

---

## ✨ Features

- 📄 Upload multiple resumes in PDF format
- 📝 Paste a job description
- 🔍 Automatically compares resumes to the job description using semantic similarity
- 🧠 Uses OpenAI's `text-embedding-ada-002` for deep text understanding
- 📦 Stores and queries resume embeddings using **Pinecone** (or optionally FAISS)
- 📊 Displays ranked matches with similarity scores
- 📤 One-click CSV download of the results
- 🌐 Lightweight Streamlit UI – runs in-browser, no frontend code required

---

## 🧰 Tech Stack

| Tool/Library      | Purpose                                  |
|------------------|------------------------------------------|
| `Python 3.8+`     | Core language                           |
| `Streamlit`       | UI interface                            |
| `OpenAI API`      | Embedding generation                    |
| `Pinecone`        | Vector storage and similarity search    |
| `PyMuPDF`         | PDF text extraction                     |
| `pandas`          | Data manipulation & CSV export          |
| `dotenv`          | Managing environment variables          |

---

## 🧠 How It Works

1. **Extract Resume Text**  
   PDFs are parsed using `PyMuPDF` to extract clean text.

2. **Generate Embeddings**  
   The extracted resume text and the job description are converted into numerical embeddings using OpenAI’s `text-embedding-ada-002` model.

3. **Store in Pinecone**  
   Each resume embedding is stored in Pinecone with metadata like resume name.

4. **Similarity Search**  
   The job description embedding is compared with all stored embeddings using vector similarity.

5. **Ranking**  
   Top matches are sorted based on cosine similarity and shown with scores.

---

## 📁 Directory Structure

```

ai-resume-ranker/
│
├── app.py                  # Main Streamlit application
├── utils.py                # Core logic: embedding, PDF extraction, Pinecone ops
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not to be committed)
└── README.md               # Project documentation

````

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-resume-ranker.git
cd ai-resume-ranker
````

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Setup

Create a `.env` file in the root folder and add the following:

```env
OPENAI_API_KEY=your-openai-api-key
PINECONE_API_KEY=your-pinecone-api-key
PINECONE_INDEX=resume-index
PINECONE_ENV=us-west4-gcp   # (or your region)
```

> ⚠️ Make sure `.env` is in your `.gitignore`

---

## 🚀 Run the Application

```bash
streamlit run app.py
```

Then open your browser at: [http://localhost:8501](http://localhost:8501)

---

## 📤 Example Output

| Resume Name        | Similarity Score |
| ------------------ | ---------------- |
| anjali\_resume.pdf | 0.9271           |
| ravi\_cv.pdf       | 0.8934           |
| akash\_profile.pdf | 0.8711           |

You can download this as a CSV directly from the app.

---

## 💡 Use Cases

* 🔎 **Recruiters**: Quickly shortlist top applicants.
* 🎓 **Students**: Optimize resumes for specific job descriptions.
* 💼 **Hiring Platforms**: Embed resume matching functionality.

---

## 🛠 Optional: Use FAISS for Offline Mode (No Pinecone)

If you want to use local vector search instead of Pinecone, replace `query_top_k()` and `add_resume_to_pinecone()` functions in `utils.py` with [FAISS](https://github.com/facebookresearch/faiss).
Let me know if you want the code for that version too!

---

## 📋 requirements.txt

```txt
streamlit
openai
python-dotenv
PyMuPDF
pandas
pinecone-client
```

---

## 🌐 Deployment Options

* Streamlit Community Cloud
* Hugging Face Spaces
* Render / Vercel (with Streamlit)
* Local Server (for internal hiring teams)

Let me know if you want a one-click deployment guide.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Credits

* [OpenAI](https://openai.com/)
* [Pinecone](https://www.pinecone.io/)
* [Streamlit](https://streamlit.io/)
* [PyMuPDF](https://pymupdf.readthedocs.io/)

---

## 🤝 Contributing

Pull requests are welcome! If you want to suggest a feature or report a bug, feel free to open an issue.

---

## 💬 Contact

Created by **[BETALA SHASI KIRAN](https://github.com/bshasikiran)**
📧 Email: [bshasikiran@example.com](mailto:bshasikiran@example.com)


