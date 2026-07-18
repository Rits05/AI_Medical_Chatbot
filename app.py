import os
import tempfile
import streamlit as st

from src.rag_pipeline import MedicalChatbot
from src.report_export import create_report_pdf


# ------------------------
# Streamlit Configuration
# ------------------------

st.set_page_config(
    page_title="Medical Chatbot",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 AI Medical Chatbot")


# ------------------------
# Load Chatbot
# ------------------------

@st.cache_resource
def load_chatbot():
    return MedicalChatbot()


chatbot = load_chatbot()


# ------------------------
# Chat History
# ------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# ------------------------
# Upload Multiple Documents
# ------------------------

uploaded_files = st.file_uploader(
    "📄 Upload Medical Documents",
    type=["pdf", "txt", "docx"],
    accept_multiple_files=True
)

# ------------------------
# Upload Medical Report
# ------------------------

uploaded_report = st.file_uploader(
    "🩺 Upload Medical Report",
    type=["pdf", "png", "jpg", "jpeg"],
    key="medical_report"
)

# ------------------------
# Sidebar
# ------------------------

with st.sidebar:
    st.title("🏥 Medical RAG Assistant")

    st.markdown("---")

    st.subheader("📖 About")
    st.write(
        """
        This AI Medical Chatbot can:

        ✅ Answer questions from uploaded medical documents using RAG.

        ✅ Analyze blood reports, lab reports, prescriptions and medical reports.

        ✅ Provide educational explanations of medical findings.
        """
    )

    st.markdown("---")

    st.subheader("🛠 Tech Stack")
    st.write("✅ LangChain")
    st.write("✅ Ollama (Llama 3.2)")
    st.write("✅ HuggingFace Embeddings")
    st.write("✅ FAISS")
    st.write("✅ Streamlit")

    st.markdown("---")

    st.subheader("📂 Supported Files")

    st.write("📄 PDF")
    st.write("📝 TXT")
    st.write("📘 DOCX")
    st.write("🖼 PNG")
    st.write("🖼 JPG")
    st.write("🖼 JPEG")

    st.markdown("---")

    # ------------------------
    # Language Selection
    # ------------------------

    st.subheader("🌐 Response Language")

    language = st.selectbox(
        "Choose Language",
        [
            "Auto Detect",
            "English",
            "Hindi",
            "Hinglish"
        ]
    )

    st.markdown("---")

    st.subheader("📊 Upload Status")

    if uploaded_files:
        st.success(f"✅ {len(uploaded_files)} knowledge document(s) uploaded")
    else:
        st.info("📂 No knowledge documents uploaded")

    if uploaded_report:
        st.success("🩺 Medical report uploaded")
    else:
        st.info("🩺 No medical report uploaded")

    st.markdown("---")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    st.caption("Version 2.0")
    st.caption("Made with ❤️ using LangChain + Ollama")


# ------------------------
# Index Documents
# ------------------------

if uploaded_files:
    file_paths = []

    for uploaded_file in uploaded_files:
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=os.path.splitext(uploaded_file.name)[1]
        ) as tmp:
            tmp.write(uploaded_file.read())
            file_paths.append(tmp.name)

    with st.spinner("📚 Indexing documents..."):
        chatbot.ingest_multiple(file_paths)

    st.success(
        f"✅ {len(uploaded_files)} document(s) indexed successfully!"
    )
# ------------------------
# Analyze Medical Report
# ------------------------

if uploaded_report:

    st.markdown("---")
    st.subheader("🩺 Medical Report Analysis")

    if st.button("🔍 Analyze Report"):

        with st.spinner("Analyzing report..."):

            report_result = chatbot.analyze_report(uploaded_report)

        # Display Analysis
        st.subheader("📋 Medical Report Analysis")
        st.success(report_result)

        # Create PDF
        pdf_file = create_report_pdf(report_result)

        # Download Button
        with open(pdf_file, "rb") as file:

            st.download_button(
                label="📄 Download AI Analysis",
                data=file,
                file_name="Medical_Report_Analysis.pdf",
                mime="application/pdf"
            )

# ------------------------
# Display Chat History
# ------------------------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ------------------------
# Chat Input
# ------------------------

question = st.chat_input("Ask a medical question...")

if question:
    # User message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Bot response
    with st.chat_message("assistant"):
        with st.spinner("🤖 Thinking..."):
            answer = chatbot.ask(
                question,
                language
            )

        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )