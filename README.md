# 📄 **Social Persona Mapping OSINT**

## 🧠 **Overview**

**Social Persona Mapping OSINT** is an automated AI-powered system that analyzes a target’s **online behavior, online presence, and online interactions** across digital platforms.
The goal is to detect **multi-account patterns**, map **supporter networks**, and visualize **influence ecosystems** using machine learning and graph intelligence.

The system collects public OSINT data, extracts behavioral features, applies ML models to compare accounts, and generates an interactive **persona graph** highlighting clusters, influence routes, and potential linked identities.

---

## 🔍 **Key Capabilities**

### ✅ **1. Online Behavior Analysis**

* Posting style & linguistic patterns
* Topic similarity & content themes
* Activity cycles (day/time patterns)
* Hashtag, keyword, and engagement habits

### ✅ **2. Online Presence Analysis**

* Username patterns
* Profile images & bio similarity
* Account creation patterns
* Cross-platform digital identity mapping

### ✅ **3. Online Interaction Analysis**

* Likes, replies, mentions, shares
* Who they follow & who follows them
* Interaction frequency and direction
* Group & cluster identification

---

## 🎯 **Project Goals**

1. **Multi-Account Detection**
   Identify accounts likely controlled by the same individual using ML similarity scoring.

2. **Supporter & Network Analysis**
   Detect engagement clusters, aligned communities, and influence groups.

3. **Persona Graph Visualization**
   Build an interactive graph showing relationships, clusters, and influence strength.

---

## 🏗️ **System Architecture**

```
                ┌─────────────────────────┐
                │  Public Social Platforms│
                └───────────┬─────────────┘
                            │ OSINT Scraper
                            ▼
                 ┌────────────────────────┐
                 │  Data Collection Layer │
                 └───────────┬────────────┘
                             │
                             ▼
                 ┌────────────────────────┐
                 │  Feature Extraction    │
                 │ (Text, Image, Behavior)│
                 └───────────┬────────────┘
                             │
                             ▼
                 ┌────────────────────────┐
                 │ ML Analysis Engine     │
                 │ - Stylometry           │
                 │ - Image Embedding      │
                 │ - Username similarity  │
                 │ - Behavior modeling    │
                 └───────────┬────────────┘
                             │
                             ▼
                 ┌────────────────────────┐
                 │ Graph Analysis Layer   │
                 │ - Clustering           │
                 │ - Influence scoring    │
                 └───────────┬────────────┘
                             │
                             ▼
                 ┌────────────────────────┐
                 │ Visualization Dashboard│
                 │ Persona Graph          │
                 └────────────────────────┘
```

---

## 🧬 **Machine Learning Components**

### **1. Username Similarity**

* Vector embeddings
* Edit distance & pattern matching

### **2. Profile Image Similarity**

* CLIP / FaceNet image embeddings
* Cosine similarity

### **3. Writing Style Similarity (Stylometry)**

* TF-IDF + Logistic Regression
* Sentence embeddings (SBERT)
* Sentence rhythm & punctuation features

### **4. Posting Pattern Modeling**

* Time-series clustering
* Behavioral fingerprints

### **5. Graph Intelligence**

* Louvain/Leiden community detection
* PageRank & betweenness centrality
* Edge weighting based on interaction frequency

---

## ⚙️ **Tech Stack**

| Layer              | Tools                               |
| ------------------ | ----------------------------------- |
| **Backend**        | Python, FastAPI / Flask             |
| **Scraping**       | SNScrape / custom scrapers          |
| **ML/NLP**         | PyTorch, Transformers, Scikit-Learn |
| **Image ML**       | CLIP / FaceNet                      |
| **Graph Analysis** | NetworkX, iGraph                    |
| **Database**       | PostgreSQL / MongoDB                |
| **Frontend**       | React / Next.js + Cytoscape.js      |
| **Visualization**  | D3.js, Plotly                       |

---

## 🚀 **Installation**

### **1. Clone the Repository**

```bash
git clone https://github.com/yourusername/social-persona-mapping-osint.git
cd social-persona-mapping-osint
```

### **2. Create a Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate   # linux/mac
venv\Scripts\activate      # windows
```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

---

## 🛠️ **Usage**

### **1. Run the Data Collector**

```bash
python run_collector.py --target <username> --platform twitter
```

### **2. Run the Multi-Account Detection**

```bash
python multi_account_detector.py --user <username>
```

### **3. Generate the Network Graph**

```bash
python graph_builder.py --user <username>
```

### **4. Start the Dashboard**

```bash
npm install
npm run dev
```

---

## 📊 **Output Examples**

### **1. Multi-Account Probability Scores**

```
user1 → user8     0.82 similarity
user1 → user22    0.67 similarity
user1 → user17    0.21 similarity
```

### **2. Supporter Network Graph**

* Nodes = accounts
* Edges = interactions
* Colors = clusters
* Size = influence score

### **3. Automated Report**

* Behavior summary
* Presence comparison
* Interaction analysis
* Multi-account findings
* Network visualization

---

## 📌 **Limitations**

* Only uses public data (no private APIs)
* Accuracy depends on data availability
* Face similarity not used as biometric ID (ethical restrictions)
* Works best on platforms with accessible metadata

---

## 🔐 **Ethical Use**

This project is intended for:

* Research
* Cyber safety
* OSINT investigations
* Digital behavior analysis

**Not intended for harassment, unauthorized tracking, or invasion of privacy.**
