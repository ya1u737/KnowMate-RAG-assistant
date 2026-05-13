# 408-RAG-PRO

**🎓 基于本地 LLM 的计算机考研 408 智能辅导助手**

一个专为**数据结构、操作系统、计算机组成原理、计算机网络**四门考研核心课程打造的本地 RAG 系统。

---

## ✨ 项目介绍

本项目旨在帮助 408 考研学生通过本地大模型 + 向量检索，实现对教材、真题、笔记的高效问答。  
支持上传 PDF 资料，结合专为 408 优化的 Prompt，提供准确、专业、结构化的回答。

**核心优势**：
- 完全本地运行，保护隐私
- 针对 408 考纲进行深度优化
- 模块化设计，易于扩展
- 支持自定义知识库

---

## 🛠️ 技术栈

- **大语言模型**：Ollama (Qwen2.5 / Llama3)
- **框架**：LangChain
- **向量数据库**：ChromaDB
- **PDF 解析**：PyMuPDF + RecursiveCharacterTextSplitter
- **前端界面**：Streamlit
- **Python 版本**：3.10+

---

## 🚀 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/ya1u737/408-RAG-PRO.git
cd 408-RAG-PRO
2. 安装依赖
Bashpip install -r requirements.txt
3. 启动 Ollama
Bash# 推荐使用 Qwen2.5
ollama pull qwen2.5:7b
# 或使用 Llama3
ollama pull llama3.2
4. 运行项目
Bashstreamlit run app.py
打开浏览器访问 http://localhost:8501 即可使用。

📁 项目结构
text408-RAG-PRO/
├── config.py                 # 配置管理
├── app.py                    # Streamlit 主界面
├── requirements.txt
├── README.md
├── LICENSE
└── src/
    ├── pdf_parser.py         # PDF 解析与分段
    ├── vector_store.py       # 向量存储与检索
    └── generator.py          # 回答生成模块（含 408 专用 Prompt）

🗺️ 开发计划

 在回答中显示知识来源页码
 支持多轮对话记忆
 引入 BM25 + 向量混合检索
 添加更多使用示例和截图
 支持 Docker 一键部署


📄 开源协议
本项目基于 MIT License 开源。

欢迎各位 408 考研的同学使用和反馈！
有任何问题或建议，欢迎在 Issues 中提出。

Made with ❤️ for 408 考研人
