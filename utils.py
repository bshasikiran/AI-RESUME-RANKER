# utils.py
import fitz  # PyMuPDF for PDF reading
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Load MiniLM model once
model = SentenceTransformer('all-MiniLM-L6-v2')
dimension = 384  # Dim of MiniLM vectors

# FAISS index & metadata
index = faiss.IndexFlatL2(dimension)
resume_metadata = []

# 📄 Extract text from PDF
def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text.strip()

# ✨ Get local embedding
def get_embedding(text):
    try:
        return model.encode([text])[0]
    except Exception as e:
        print("Embedding error:", e)
        return None

# ➕ Add to FAISS index
def add_resume_to_pinecone(resume_id, embedding, metadata):
    index.add(np.array([embedding]).astype("float32"))
    resume_metadata.append(metadata)

# 🔍 Query top K using FAISS
def query_top_k(job_desc_embedding, k=10):
    query_vector = np.array([job_desc_embedding]).astype("float32")
    distances, indices = index.search(query_vector, k)
    results = []

    for i, idx in enumerate(indices[0]):
        if idx < len(resume_metadata):
            results.append({
                "score": float(1 / (1 + distances[0][i])),  # Invert L2 distance
                "metadata": resume_metadata[idx]
            })
    return results
