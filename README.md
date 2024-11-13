# Diversity Channel

A local LLM-powered chat application with RAG capabilities, built using Streamlit and Ollama.

## Features

- 💬 Chat with multiple local LLM models through Ollama
- 📚 RAG (Retrieval-Augmented Generation) support for knowledge base enhancement
- 🔄 Dynamic model switching
- 💾 Chat history persistence
- 📝 Markdown and code syntax highlighting support
- 🌐 Multi-language support

## Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai/) installed and running locally
- At least one LLM model pulled in Ollama (e.g., llama2, mistral)

## Installation

1. Clone the repository
2. Install dependencies using `pip install -r requirements.txt`
3. Run the application with `streamlit run webMain.py`

## Usage

### Chat Interface
- Select a model from the available Ollama models
- Start chatting with the model
- Chat history is automatically saved
- Support for code highlighting and markdown rendering

### Knowledge Base Management
- Upload text documents to create a knowledge base
- Select embedding model for document processing
- RAG enhancement automatically applies relevant context from the knowledge base

## Configuration

The application uses default settings that can be modified in the respective files:

- Chat settings: `packages/chatMain.py`
- RAG settings: `packages/ragMain.py`
- UI settings: `pages/chat.py` and `pages/rag.py`

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/) for the web interface
- [Ollama](https://ollama.ai/) for local LLM support
- [LangChain](https://www.langchain.com/) for the RAG implementation