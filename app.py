import streamlit as st
from utils import extract_text_from_pdf, get_embedding, add_resume_to_pinecone, query_top_k
import uuid
import pandas as pd

st.set_page_config(page_title="AI Resume Ranker", layout="centered")
st.title("📄 AI Resume Ranker")
st.caption("Upload resumes + job description → Get ranked matches with AI ✨")

# Input
jd = st.text_area("Paste the Job Description here 👇", height=200)
uploaded_files = st.file_uploader("Upload Resumes (PDF only)", type=["pdf"], accept_multiple_files=True)

# Button click
if st.button("🔍 Rank Resumes"):
    if not jd:
        st.warning("⚠️ Please enter the job description!")
    elif not uploaded_files:
        st.warning("⚠️ Please upload at least one resume.")
    else:
        with st.spinner("⚙️ Generating embeddings and ranking resumes..."):
            jd_embedding = get_embedding(jd)

            if jd_embedding is None:
                st.error("❌ Failed to generate embedding for job description.")
            else:
                results = []

                for file in uploaded_files:
                    resume_text = extract_text_from_pdf(file)
                    emb = get_embedding(resume_text)

                    if emb is not None:
                        resume_id = str(uuid.uuid4())
                        add_resume_to_pinecone(resume_id, emb, {"name": file.name})
                    else:
                        st.warning(f"⚠️ Failed to embed: {file.name}")

                matches = query_top_k(jd_embedding)

                for match in matches:
                    results.append({
                        "Resume": match['metadata']['name'],
                        "Score": round(match['score'], 4)
                    })

                if results:
                    df = pd.DataFrame(results)
                    st.success("🎉 Ranking complete!")
                    st.dataframe(df)

                    csv = df.to_csv(index=False).encode('utf-8')
                    st.download_button("📥 Download Ranked Resumes CSV", csv, "ranked_resumes.csv", "text/csv")
                else:
                    st.info("No resumes matched or embedding failed for all resumes.")
