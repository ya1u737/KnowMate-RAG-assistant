import fitz
import os
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.config import Config


class PDFParser:
    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=Config.CHUNK_SIZE,
            chunk_overlap=Config.CHUNK_OVERLAP,
            separators=["\n\n", "\n", "。", " "]
        )

    # ===== PDF解析（支持路径 + 上传）=====
    def parse(self, file):
        if isinstance(file, str):
            doc = fitz.open(file)
            file_name = os.path.basename(file)
        else:
            doc = fitz.open(stream=file.read(), filetype="pdf")
            file_name = file.name

        documents = []

        for page_num, page in enumerate(doc):
            text = page.get_text().strip()
            if text:
                documents.append(
                    Document(
                        page_content=text,
                        metadata={
                            "source": file_name,
                            "page": page_num + 1
                        }
                    )
                )

        return self.splitter.split_documents(documents)

    # ===== TXT解析 =====
    def parse_txt(self, file):
        text = file.read().decode("utf-8")

        return self.splitter.create_documents(
            [text],
            metadatas=[{"source": file.name, "page": 1}]
        )