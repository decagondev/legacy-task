## 🛠️ Architecture Specification: Legacy Customer Support Monolith
This blueprint details a 2015-era Python Flask application using raw SQLite queries. It establishes a highly coupled, unvalidated baseline designed for refactoring and AI augmentation.

```
legacy-support-app/
├── app.py                     # Monolithic route handlers and raw SQL queries
├── database.py                # Schema initialization script
├── requirements.txt           # Pin-pointed legacy dependencies
└── test_suite.py              # Incomplete and broken integration tests
```

# 🎯 Assignments

## 🔎 Assignment 1: Semantic Search

* Goal: Replace the vulnerable LIKE %string% query.
* Task: Install sqlite-vss or a vector database wrapper. Embed incoming descriptions into local vectors. Rewrite the search router to evaluate cosine similarity scores.

## 🏷️ Assignment 2: Zero-Shot Triage

* Goal: Eliminate manual categorization loops.
* Task: Integrate a local LLM runner (like Ollama) or an API endpoint. Drop the nested if-else block. Automatically categorize incoming user queries into Billing, Technical, or Account.

## 📋 Assignment 3: Schema Normalization

* Goal: Enforce reliable structure over messy user string inputs.
* Task: Replace the brittle string processing routines in /tickets/extract with a Structured Outputs API call. Enforce structural validation via a strict JSON data schema.

------------------------------
Would you like me to provide the solution code using a specific framework like LangChain, or would you prefer a Pydantic validation layer for the data normalization route?

