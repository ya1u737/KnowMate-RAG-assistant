from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings, ChatOllama
from src.config import Config


class KnowledgeBase:
    def __init__(self):
        # 向量模型
        self.embedding = OllamaEmbeddings(
            model=Config.EMBEDDING_MODEL
        )

        # 向量库
        self.db = None

        # 用于 Query 改写
        self.llm = ChatOllama(
            model=Config.CHAT_MODEL,
            temperature=0
        )

    # ==================== 添加文档 ====================
    def add_documents(self, docs):
        if self.db is None:
            self.db = FAISS.from_documents(docs, self.embedding)
        else:
            self.db.add_documents(docs)

    # ==================== Query 改写 ====================
    def rewrite_query(self, query):
        prompt = f"""
请将用户问题改写为更适合知识检索的形式，使其更完整、明确：

用户问题：
{query}

改写后的检索问题：
"""
        try:
            res = self.llm.invoke(prompt)
            return res.content.strip()
        except:
            return query  # 出错就用原问题

    # ==================== 简单 rerank ====================
    def rerank(self, query, docs):
        scored = []

        for doc in docs:
            text = doc.page_content

            prompt = f"""
请判断以下内容与问题的相关性，给出0-10分：

问题：
{query}

内容：
{text[:300]}

只输出一个数字分数：
"""
            try:
                res = self.llm.invoke(prompt)
                score = float(res.content.strip())
            except:
                score = 0

            scored.append((score, doc))

        scored.sort(key=lambda x: x[0], reverse=True)

        return [doc for score, doc in scored[:Config.FINAL_TOP_K]]

    # ==================== 搜索（核心） ====================
    def search(self, query):
        if self.db is None:
            return []

        # 1️⃣ Query 改写
        new_query = self.rewrite_query(query)

        # 2️⃣ 向量召回（多取一点）
        docs = self.db.similarity_search(
            new_query,
            k=Config.RETRIEVAL_TOP_K
        )

        # 3️⃣ rerank
        docs = self.rerank(query, docs)

        return docs