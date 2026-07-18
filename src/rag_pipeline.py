from src.loader import load_document
from src.splitter import split_documents
from src.embeddings import load_embeddings
from src.vector_db import create_vectorstore
from src.llm import load_llm
from src.language import detect_language
from src.medicine import MedicineDatabase
from src.report_reader import extract_report_text
from src.report_parser import parse_report
from src.report_analyzer import analyze_report
from src.report_classifier import classify_report


class MedicalChatbot:
    def __init__(self):
        self.embedding = load_embeddings()
        self.generator = load_llm()
        self.vectorstore = None
        self.medicine_db = MedicineDatabase()

    # ------------------------
    # Single Document Upload
    # ------------------------
    def ingest(self, file_path):
        docs = load_document(file_path)
        chunks = split_documents(docs)

        self.vectorstore = create_vectorstore(
            chunks,
            self.embedding
        )

    # ------------------------
    # Multiple Document Upload
    # ------------------------
    def ingest_multiple(self, file_paths):
        all_chunks = []

        for file_path in file_paths:
            docs = load_document(file_path)
            chunks = split_documents(docs)
            all_chunks.extend(chunks)

        self.vectorstore = create_vectorstore(
            all_chunks,
            self.embedding
        )

    # ------------------------
    # Ask Question
    # ------------------------
    def ask(self, question, language="Auto Detect"):

        if language == "Auto Detect":
            language = detect_language(question)

        # ------------------------
        # Medicine Database Search
        # ------------------------
        medicine = self.medicine_db.search_medicine(question)

        if medicine:
            prompt = f"""
You are an AI Medical Assistant.

Answer in {language}.

Medicine:
{medicine['medicine']}

Used For:
{medicine['used_for']}

Side Effects:
{medicine['side_effects']}

Drug Interactions:
{medicine['interactions']}

Contraindications:
{medicine['contraindications']}

Explain the medicine in a simple and easy-to-understand way.
"""

            response = self.generator.invoke(prompt)
            return response.content.strip()

        # ------------------------
        # RAG
        # ------------------------
        if self.vectorstore is None:
            return "Please upload a medical document first."

        docs = self.vectorstore.similarity_search(
            question,
            k=3
        )

        if not docs:
            return "I couldn't find any relevant information."

        context = "\n\n".join(
            doc.page_content for doc in docs
        )

        # Debug (remove later if you want)
        print("\n==========================")
        print("Detected Language:", language)
        print("==========================")

        print("\nRetrieved Context:\n")
        print(context)

        prompt = f"""
You are an expert AI Medical Assistant.

STRICT RULES:

1. Read the Context carefully.
2. Answer ONLY using the Context.
3. If the answer exists in the Context, NEVER say it is unavailable.
4. Explain the answer clearly.
5. Respond ONLY in {language}.
6. If the answer is not present in the Context, reply exactly:
I couldn't find that information in the uploaded document.

Context:
----------------------
{context}
----------------------

Question:
{question}

Answer:
"""

        print("\nPrompt Sent To LLM:\n")
        print(prompt)

        response = self.generator.invoke(prompt)

        return response.content.strip() 
    


        # ------------------------
    # Medical Report Analysis
    # ------------------------
    def analyze_report(self, uploaded_file):

        # Step 1: Extract text
        report_text = extract_report_text(uploaded_file)
        print("=" * 50)
        print(report_text)
        print("=" * 50)

        # Step 2: Extract medical values
        report_values = parse_report(report_text)
        if not report_values:
            return (
                "I couldn't identify any laboratory values in the uploaded report. "
                "Please upload a clearer report or a supported laboratory report."
            )
        print(report_values)
        # Step 3: Rule-based analysis
        report_type = classify_report(report_values)

        analysis = analyze_report(report_values)
        print(analysis)


        prompt = f"""
You are an expert AI Medical Assistant.

Medical Report Type:
{report_type}

Medical Report Analysis

Abnormal High Findings:
{chr(10).join(analysis["high"])}

Abnormal Low Findings:
{chr(10).join(analysis["low"])}

Normal Findings:
{chr(10).join(analysis["normal"])}

Generate the report using this format.

## 📋 Medical Report Summary

### 🔴 Abnormal Findings
Explain every abnormal value.

### 🟢 Normal Findings
Briefly mention normal values.

### 💡 Lifestyle Recommendations

### 🍎 Diet Suggestions

### 🏃 Exercise Advice

### ⚠ Follow-up Tests

### 👨‍⚕️ When to Consult a Doctor

### 📌 Disclaimer

Do not diagnose disease.
Educational purpose only.
"""

        response = self.generator.invoke(prompt)

        return response.content.strip()