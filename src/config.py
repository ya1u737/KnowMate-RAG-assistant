import os

class Config:
    # ==================== 路径配置 ====================
    DATA_PATH = "data/"                     # PDF 文件存放目录
    VECTOR_DB_PATH = "vector_db/"           # 向量数据库保存路径（可选）

    # ==================== 本地 Ollama 聊天模型 ====================
    CHAT_MODEL = "qwen2.5-coder:7b"              # 推荐改成 14b 或更大模型，7b 可能偏弱
    # CHAT_MODEL = "deepseek-r1:8b"         # 如果你已下载也可以用这个

    # ==================== DeepSeek API 配置 ====================
    USE_API = True
    API_MODEL = "deepseek-reasoner"         # 推荐思考模式，适合考研复杂问题
    # API_MODEL = "deepseek-chat"           # 速度更快、成本更低时可切换
    API_KEY = "sk-a79795fbde894e0a95f6dde53210e1fa"   # ← 改成你真实的 Key
    API_BASE = "https://api.deepseek.com"

    # ==================== Embedding 模型配置（关键！新增） ====================
    # 本地 Ollama Embedding（强烈推荐目前使用）
    EMBEDDING_MODEL = "bge-m3"              # 2026年中文 RAG 最推荐的开源模型之一
    # 备选（任选其一）：
    # EMBEDDING_MODEL = "nomic-embed-text"
    # EMBEDDING_MODEL = "qwen3-embedding"     # 如果你已 pull

    # RAG 检索参数
    CHUNK_SIZE = 600                        # 建议调大一点，考研讲义单段通常较长
    CHUNK_OVERLAP = 100
    TOP_K = 4                               # 检索返回 4 个最相关片段（可调 3~6）

    # ==================== Prompt 模板（已优化） ====================
    PROMPT_TEMPLATE = """你是一位专业、严谨、有十年教学经验的 408 考研导师（涵盖数据结构、操作系统、计算机网络、计算机组成原理）。
请严格基于上下文信息回答问题，结合历史对话，重点突出核心考点、易混点、经典解题思路。
回答要逻辑清晰、条理分明，适当使用 Markdown 列表、加粗、编号。
如果上下文不足，可结合专业知识补充，但请注明“基于通用考研知识”。

【对话历史】
{chat_history}

【参考上下文】
{context}

【当前问题】
{question}

请直接开始回答，不要重复问题："""