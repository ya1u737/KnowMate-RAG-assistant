# RAG-Bot — Local-First Knowledge Base Assistant

> 🎓 基于本地大模型的 RAG 知识库助手，隐私优先，支持 408 考研 / 医疗 / 法律等强知识检索场景。

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Streamlit](https://img.shields.io/badge/frontend-streamlit-red.svg)](https://streamlit.io/)
[![Powered by Ollama](https://img.shields.io/badge/LLM-Ollama-orange.svg)](https://ollama.com/)

<div align="center">
  <img src="docs/demo.png" alt="Demo Screenshot" width="800">
  <p><em>（截图待补充）</em></p>
</div>

---

## ✨ 功能特点

- 🏠 **完全本地**：所有模型运行在本地，无需联网，保护隐私
- 🔄 **云端可选**：支持 DeepSeek API 云端模式，一键切换
- 🧠 **智能检索**：向量检索 + Cross Encoder Rerank，精准匹配
- 📚 **多格式支持**：PDF / TXT / DOCX 文档解析
- 🎨 **现代 UI**：Streamlit 聊天界面，暗色主题
- 🔌 **可扩展**：支持接入不同领域知识库（408 考研 / 医疗 / 法律）

---

## 🏗️ 技术架构

```
用户提问
  ↓
Streamlit 前端
  ↓
┌──────────── RAG Pipeline ────────────┐
│  ① 文档解析（PyMuPDF + TextSplitter）│
│  ② 向量检索（Chroma + bge-m3）       │
│  ③ Rerank（bge-reranker-v2-m3）      │
│  ④ LLM 生成（deepseek-r1:14b）       │
└──────────────────────────────────────┘
  ↓
Ollama 本地模型 / DeepSeek 云端 API
```

### 技术栈

| 层 | 技术 |
|---|------|
| UI | Streamlit |
| 文档解析 | PyMuPDF / langchain-text-splitters |
| 向量检索 | Chroma + bge-m3 (Ollama) |
| 重排序 | bge-reranker-v2-m3 (sentence-transformers) |
| LLM | qwen2.5:7b / deepseek-r1:14b (Ollama) |

---

## 🚀 快速启动

### 前置条件

- Python 3.11+
- [Ollama](https://ollama.com/)（本地模型运行环境）

### 安装

```bash
git clone https://github.com/ya1u737/408-RAG-PRO.git
cd 408-RAG-PRO
pip install -r requirements.txt
```

### 下载模型

```bash
# 1. 聊天模型（任选一个）
ollama pull qwen2.5:7b
# 或：
ollama pull deepseek-r1:14b  # 需要 9GB+ 显存

# 2. Embedding 模型
ollama pull bge-m3

# 3. Reranker 模型（自动下载到用户目录）
# 代码首次运行时会自动从 HuggingFace 缓存
# 或在启动时设置环境变量：
# export RERANKER_MODEL=/path/to/bge-reranker-v2-m3
```

### 启动

```bash
streamlit run app.py
```

浏览器打开 `http://localhost:8501`

---

## 📦 环境配置

```bash
# 创建 .env 文件
cp .env.example .env

# 编辑 .env，填入你的 API Key（可选）
DEEPSEEK_API_KEY=sk-your-key-here  # 留空则使用本地 Ollama
USE_API=false                       # 设为 true 时使用 DeepSeek API
```

### 配置项

| 配置项 | 默认值 | 说明 |
|--------|--------|------|
| `CHAT_MODEL` | `qwen2.5:7b` | Ollama 聊天模型 |
| `EMBEDDING_MODEL` | `bge-m3` | Ollama Embedding 模型 |
| `RERANKER_MODEL` | `bge-reranker-v2-m3` | Cross Encoder 模型 |
| `RETRIEVAL_TOP_K` | 5 | 向量召回候选数 |
| `FINAL_TOP_K` | 3 | Rerank 后返回数 |

---

## 🔮 后续规划

- [ ] 知识库持久化存储（Chroma 持久化）
- [ ] Hybrid Search（BM25 + 向量）
- [ ] 引用增强（标记文档来源）
- [ ] 多知识库隔离切换
- [ ] 医疗 / 法律领域适配模板
- [ ] Docker 一键部署
- [ ] 单元测试覆盖

---

## 📄 License

MIT License. 详见 [LICENSE](LICENSE)

---

*Made with ❤️ for privacy-first RAG.*