# 📄 Contract Note Processing System

AI-powered contract note extraction pipeline using Vision LLMs, PDF-to-image conversion, OCR-style document understanding, and structured JSON/Excel export.

---

# 🚀 Overview

This project processes broker contract notes and extracts structured financial data using Vision Language Models (VLMs).

The system:

- Converts PDF contract notes into images
- Merges multi-page documents
- Sends images to Vision LLM APIs
- Extracts structured JSON responses
- Cleans malformed LLM outputs
- Converts extracted data into Excel sheets

---

# 🏗️ Project Architecture

```text
PDF Contract Note
        ↓
PDF → Images
        ↓
Image Merge + Base64 Encoding
        ↓
Vision LLM API
        ↓
Structured JSON Extraction
        ↓
Sanitization & Parsing
        ↓
Excel Export
```

---

# 📁 Project Structure

```text
Contract_Processer/
│
├── agent.py
├── visionengine.py
├── utils.py
├── config.py
├── pdftoencodding.py
│
├── contract_note_system_prompt.txt
│
├── Decrypted_Document/
│   └── *.PDF
│
├── temp_image/
│
└── output/
    ├── Equity_Segment.xlsx
    ├── Trade_Annexure.xlsx
    └── Client_Detail.xlsx
```

---

# ⚙️ Features

- 📄 Multi-page PDF support
- 🖼️ Image merging for better VLM understanding
- 🤖 Vision LLM integration
- 🧹 LLM JSON sanitization
- 📊 Automatic Excel generation
- ⚡ Configurable DPI and image format
- 🔧 Modular architecture
- 📦 Easy API integration

---

# 🧠 Core Components

## 1. `agent.py`

Main orchestration script.

Responsibilities:

- Load prompt
- Load PDFs
- Call Vision Engine
- Parse response
- Convert structured data into Excel

---

## 2. `visionengine.py`

Handles:

- PDF image conversion
- Image merging
- Base64 encoding
- API payload generation
- Vision API communication

Contains:

### `VisionEngine`

Processes documents page-by-page.

### `VisionEngine_`

Processes merged images for better context understanding.

### `VisionPostEnging`

Post-processing using text LLM.

---

## 3. `utils.py`

Utility functions for:

- Cleaning malformed LLM responses
- Extracting JSON safely
- Converting text → Python dictionary

---

# 🔧 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/contract-note-processor.git

cd contract-note-processor
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Required Libraries

```text
openai
pandas
requests
pillow
pdf2image
openpyxl
```

---

# 🔑 Configuration

Create a `config.py` file.

```python
NVIDIA_API_KEY = "YOUR_API_KEY"

NVIDAI_VISION_INSTRUCT_MODEL = "your-model"

NVIDAI_VISION_INSTRUCT_URL = "https://your-api-endpoint"

DEFAULT_MODEL = "your-text-model"
```

---

# 📜 Prompt Engineering

The extraction logic is driven by:

```text
contract_note_system_prompt.txt
```

This prompt defines:

- Expected JSON structure
- Financial fields
- Extraction instructions
- Validation rules

---

# ▶️ Running the Project

```bash
python agent.py
```

---

# 📊 Output

The system generates Excel files automatically.

Example:

```text
Equity_Segment.xlsx
Trade_Annexure.xlsx
Client_Detail.xlsx
```

---

# 🧹 JSON Sanitization Logic

LLMs often return:

- Markdown
- Extra explanations
- Invalid JSON formatting

The utility function:

```python
sanitize_llm_response()
```

Extracts only the JSON object safely.

Example:

```python
text = re.sub(r'```(?:json)?',"",text).strip()
```

---

# 🖼️ Image Processing Pipeline

## PDF → Image

Uses:

```python
PDF2IMAGECONVERTER
```

## Multi-page Merge

Uses:

```python
ImageMerger
```

Benefits:

- Better contextual understanding
- Reduced fragmented extraction
- Improved VLM accuracy

---

# 🤖 Vision API Payload

Example request payload:

```python
payload = {
    "model": self.model,
    "messages": [
        {
            "role": "user",
            "content": content
        }
    ],
    "temperature": 0.1,
    "top_p": 0.7,
    "max_tokens": 3000,
    "stream": False
}
```

---

# 📈 Use Cases

- Contract note processing
- Financial document extraction
- Trade annexure parsing
- Broker statement analysis
- Automated backoffice workflows
- Structured finance data pipelines

---

# ⚠️ Common Issues

## 1. Timeout Errors

Increase request timeout:

```python
timeout=360
```

---

## 2. Invalid JSON

Handled using:

```python
json.loads()
ast.literal_eval()
```

---

## 3. Large PDF Issues

Reduce DPI:

```python
dpi=100
```

or switch:

```python
img_format="jpeg"
```

---

# 🔥 Future Improvements

- Async processing
- Batch PDF processing
- LangGraph integration
- Agentic workflows
- Database storage
- Vector search
- OCR fallback pipeline
- Human-in-the-loop validation

---

# 🧪 Sample Workflow

```python
extracteddocument = VisionEngine_(
    model=conf.NVIDAI_VISION_INSTRUCT_MODEL,
    API_URL=conf.NVIDAI_VISION_INSTRUCT_URL,
    dpi=200,
    img_format="jpeg",
    save_image=False,
    prompt=prompt,
    path=paths[1],
    API=conf.NVIDIA_API_KEY
)._extract_document()
```

---

# 📌 Example Output Structure

```json
{
  "Client_Detail": {
    "Client_Name": "ABC",
    "Client_Code": "12345"
  },

  "Equity_Segment": [
    {
      "Symbol": "RELIANCE",
      "Quantity": 10,
      "Price": 2500
    }
  ]
}
```

---

# 🛡️ Best Practices

- Keep DPI optimized
- Use merged images for large context
- Validate LLM responses
- Save raw responses for debugging
- Log API errors properly

---

# 📚 Tech Stack

- Python
- Vision LLMs
- OpenAI SDK
- Pandas
- Requests
- PDF Processing
- Excel Automation

---

# 👨‍💻 Author

Souman Jyoti

Interested in:

- Quantitative Finance
- Agentic AI
- Financial Data Engineering
- Vision Language Models
- AI Automation

---

# ⭐ Contributing

Pull requests are welcome.

For major changes:

1. Fork repository
2. Create feature branch
3. Commit changes
4. Push branch
5. Open PR

---

# 📄 License

MIT License

---

# 🙌 Acknowledgements

Special thanks to:

- Open-source AI community
- Vision LLM researchers
- Financial automation ecosystem

---
