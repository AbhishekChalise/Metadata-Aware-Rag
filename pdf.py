from fpdf import FPDF

class SyllabusPDF(FPDF):
    def header(self):
        # Header with a subtle blue bar
        self.set_fill_color(41, 128, 185)  # Professional Blue
        self.rect(0, 0, 210, 20, 'F')
        self.set_font('Arial', 'B', 16)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, 'Enterprise Agentic RAG: Master Syllabus', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def phase_title(self, num, title, goal):
        self.set_font('Arial', 'B', 14)
        self.set_text_color(41, 128, 185)
        self.cell(0, 10, f'Phase {num}: {title}', 0, 1, 'L')
        self.set_font('Arial', 'I', 11)
        self.set_text_color(50, 50, 50)
        self.multi_cell(0, 7, f'Goal: {goal}')
        self.ln(2)

    def add_topics(self, topics):
        self.set_font('Arial', 'B', 11)
        self.set_text_color(0, 0, 0)
        self.cell(0, 7, 'Key Topics:', 0, 1)
        self.set_font('Arial', '', 11)
        for topic in topics:
            self.cell(10)
            self.cell(0, 7, f'- {topic}', 0, 1)
        self.ln(2)

    def add_project(self, project_title, description):
        self.set_fill_color(245, 247, 250)
        self.set_font('Arial', 'B', 11)
        self.set_text_color(192, 57, 43)  # Professional Red for Projects
        self.cell(0, 8, f'Capstone Project: {project_title}', 0, 1, 'L', fill=True)
        self.set_font('Arial', '', 10)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 6, description, fill=True)
        self.ln(8)

    def sub_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_text_color(0, 0, 0)
        self.cell(0, 8, title, 0, 1, 'L')
        self.ln(1)

    def body_text(self, text):
        self.set_font('Arial', '', 10)
        self.set_text_color(50, 50, 50)
        self.multi_cell(0, 6, text)
        self.ln(2)

# Initialize PDF
pdf = SyllabusPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Phase 1
pdf.phase_title(1, "Foundations & Structured Logic", "Move from chatting to building systems that exchange data.")
pdf.add_topics([
    "Async Python: Handling multiple LLM calls simultaneously.",
    "Pydantic & JSON Schemas: Forcing LLMs to output structured data.",
    "Token Economics: Context windows, cost optimization, and prompt caching.",
    "Vector DB Fundamentals: Qdrant/Pinecone basics and Metadata filtering."
])
pdf.add_project("The Metadata-Aware PDF Chatbot", 
                "Build a system that takes 20 PDFs, extracts metadata (Title, Author, Date), and allows users to search only within specific time ranges using metadata filters.")

# Phase 2
pdf.phase_title(2, "Advanced Data Engineering (The 'Raj' Layer)", "Solve the 'Garbage In, Garbage Out' problem.")
pdf.add_topics([
    "Intelligent Parsing: Mastering Docling or Unstructured.io for complex layouts.",
    "The Quality Scorer: Detecting blurry scans or bad OCR before ingestion.",
    "Table Extraction Mastery: Converting multi-page tables into clean Markdown.",
    "Hierarchical Chunking: Implementing Parent-Child strategies."
])
pdf.add_project("The Table-Heavy Financial Analyst", 
                "Build a RAG system that processes a 100-page Annual Report with 20+ tables. The AI must answer specific numerical questions with 100% accuracy.")

# Phase 3
pdf.phase_title(3, "Agentic Reasoning & Tool Orchestration", "Giving the AI 'hands' to use tools and 'brains' to plan.")
pdf.add_topics([
    "Function Calling: LLM triggering Python functions (Calculators, SQL, Search).",
    "The ReAct Pattern: Implementing 'Reason + Act' loops.",
    "Query Decomposition: Breaking one prompt into multiple search steps.",
    "Agentic Routing: Deciding between Vector DB, SQL, or Web Search."
])
pdf.add_project("The Multi-Tool Researcher", 
                "Build an agent that can answer: 'What was Tesla's revenue in 2023 and how does it compare to the current market cap on Google?' (Vector + Web + Math).")

# Phase 4
pdf.phase_title(4, "Cognitive Architecture (Context & State)", "Building 'Contextual Awareness' and Memory.")
pdf.add_topics([
    "State Management (LangGraph): Building cyclic graphs to fix mistakes.",
    "Memory Systems: Short-term thread history vs. Persistent long-term profiles.",
    "Contextual Compression: Summarizing history to save context space.",
    "Multi-Agent Orchestration: One agent 'Searches' and another agent 'Reviews'."
])
pdf.add_project("The Persistent Legal Assistant", 
                "Build an agent that remembers legal preferences across sessions and manages a 10-step discovery process without losing track.")

# Phase 5
pdf.phase_title(5, "Self-Correction & Evaluation", "Eliminating hallucinations and ensuring 'Enterprise Truth'.")
pdf.add_topics([
    "Corrective RAG (CRAG): Building a 'Grader' that rejects bad search results.",
    "Self-RAG: An agent that critiques its own output and searches again.",
    "RAGAS Framework: Using AI to grade Faithfulness and Relevance.",
    "Hallucination Filters: Fact verification against source text."
])
pdf.add_project("The Zero-Hallucination Pharma Bot", 
                "Build a clinical trial system where the agent refuses to answer unless it finds three matching citations in the source text.")

# Phase 6
pdf.phase_title(6, "Reinforcement Learning & Optimization", "Making the system get smarter every time it is used.")
pdf.add_topics([
    "Feedback Loops (RLAIF): User Upvote/Downvote UI for training data.",
    "Reward Modeling: Using a 'Judge LLM' to grade search strategies.",
    "Contextual Re-ranking: Fine-tuning ranking based on historical success.",
    "Self-Healing Pipelines: Learning to ignore low-quality document folders."
])
pdf.add_project("The Self-Improving Search Agent", 
                "Build an agent that logs failures, analyzes them with a 'Judge LLM', and automatically updates instructions to avoid future mistakes.")

# Phase 7
pdf.phase_title(7, "Production & Deployment", "Scaling and Securing the system for Banks and Pharma.")
pdf.add_topics([
    "Local Inference (Ollama/vLLM): Running 32B+ models on private hardware.",
    "Quantization: GGUF/EXL2 formats for smaller GPU footprints.",
    "Concurrency & Guardrails: Handling 50+ users without data leaks.",
    "ROI Calculation: Building the business case for $100k contracts."
])
pdf.add_project("The Private Enterprise 'Brain'", 
                "The Graduation Project: Deploy a local, Agentic RAG system on a private server handling 1,000+ docs with 95% RAGAS accuracy.")


# 1. Logic
pdf.phase_title(8, "1. The Core Language & Logic", "Master the foundational tools for deterministic, structured AI development.")
pdf.sub_title("Python (Expert Level)")
pdf.body_text("Master Asyncio for parallel AI calls and Pydantic for structured JSON outputs. This is how you force the AI to follow your rules.")
pdf.sub_title("SQL")
pdf.body_text("Many documents are actually database rows. You must build agents that can write and execute their own SQL queries.")

# 2. Data Layer
pdf.set_font('Arial', 'I', 10)
pdf.cell(0, 6, "This is the most important part. Poor parsing = Project failure.", 0, 1)
pdf.sub_title("Docling (by IBM)")
pdf.body_text("Currently the best tool for converting complex PDFs and tables into clean Markdown.")
pdf.sub_title("Unstructured.io")
pdf.body_text("The go-to for 'SharePoint hell' (handling .docx, .pptx, and .pdf simultaneously).")
pdf.sub_title("Marker")
pdf.body_text("High-speed, high-accuracy PDF-to-Markdown conversion for massive document sets.")

# 3. Orchestration
pdf.sub_title("LangGraph")
pdf.body_text("The industry standard for Agentic RAG. It allows stateful loops where the AI can 'go back' if a search fails.")
pdf.sub_title("LlamaIndex")
pdf.body_text("Specifically Workflows and Query Engines. Superior to LangChain for deep, technical data retrieval.")

# 4. Knowledge Vault
pdf.sub_title("Qdrant")
pdf.body_text("Highly recommended for enterprise metadata filtering and hybrid search capabilities.")
pdf.sub_title("PGVector (PostgreSQL)")
pdf.body_text("Ideal for banks that already use Postgres. Build AI on top of their existing, secure infrastructure.")

# 5. Inference
pdf.sub_title("Ollama & vLLM")
pdf.body_text("Essential for local development (Ollama) and production-grade local hosting (vLLM) for privacy-sensitive clients.")
pdf.sub_title("Models to Master")
pdf.body_text("Qwen 2.5 (32B/72B) for technical/math tasks. Llama 3.1 (70B) for high-level reasoning.")

# 6 & 7. Trust & UI
pdf.sub_title("RAGAS & DeepEval")
pdf.body_text("Frameworks to grade 'Faithfulness' and 'Answer Relevancy' to prove to clients the AI isn't lying.")


pdf.sub_title("Chainlit & Streamlit")
pdf.body_text("Rapidly build professional chat interfaces and data dashboards in pure Python.")

# Summary Checklist
pdf.ln(5)
pdf.set_fill_color(240, 240, 240)
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, "Summary Checklist: Your 'Start Today' Stack", 0, 1, 'C', fill=True)
pdf.set_font('Arial', '', 11)
pdf.cell(0, 7, "1. Framework: Learn LangGraph.", 0, 1, 'C')
pdf.cell(0, 7, "2. Data Extraction: Learn Docling.", 0, 1, 'C')
pdf.cell(0, 7, "3. Local LLM: Install Ollama and run Qwen 2.5.", 0, 1, 'C')
pdf.cell(0, 7, "4. Database: Start a local Qdrant instance via Docker.", 0, 1, 'C')

# Save the PDF
pdf.output("Agentic_RAG_Ultimate_Syllabus.pdf")
print("PDF Generated Successfully: Agentic_RAG_Ultimate_Syllabus.pdf")





