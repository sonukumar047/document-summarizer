import math
from typing import List, Dict

MAX_TOKENS = 5000
AVG_CHARS_PER_TOKEN = 4  # Approximation used by many LLMs


def estimate_tokens(text: str) -> int:
    """
    Estimate token count from character length.
    """
    return math.ceil(len(text) / AVG_CHARS_PER_TOKEN)


def split_into_chunks(text: str, max_tokens: int = MAX_TOKENS) -> List[str]:
    """
    Split text into chunks based on estimated token limit.
    """
    max_chars = max_tokens * AVG_CHARS_PER_TOKEN
    return [text[i:i + max_chars] for i in range(0, len(text), max_chars)]


def process_document(file_path: str) -> Dict:
    """
    Reads a text document, splits into chunks if token limit exceeds,
    and returns structured metadata.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read().strip()

    if not content:
        raise ValueError("Document is empty.")

    char_count = len(content)
    token_count = estimate_tokens(content)

    chunks = split_into_chunks(content) if token_count > MAX_TOKENS else [content]

    return {
        "file_path": file_path,
        "character_count": char_count,
        "estimated_tokens": token_count,
        "chunk_count": len(chunks),
        "chunks": chunks
    }


if __name__ == "__main__":
    result = process_document(f"E:\CompanyAssignments\document-summarizer\src\sample.txt")
    print(result)
    
