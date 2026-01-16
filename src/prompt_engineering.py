def build_summarization_prompt(document_text: str) -> dict:
    """
    Dynamically constructs a summarization prompt based on document length.
    Handles edge cases and returns prompt + reasoning.
    """

    if not document_text or not document_text.strip():
        return {
            "prompt": None,
            "reasoning": "Empty document provided. No summary generated."
        }

    length = len(document_text)

    if length < 1000:
        summary_type = "short, high-level summary"
    elif length < 5000:
        summary_type = "concise paragraph-wise summary"
    else:
        summary_type = (
            "structured summary with bullet points, "
            "key insights, and a concluding paragraph"
        )

    prompt = (
        f"You are an AI assistant specialized in document summarization.\n\n"
        f"Task:\n"
        f"Generate a {summary_type} while preserving factual accuracy.\n"
        f"Do not introduce information not present in the document.\n\n"
        f"Document:\n"
        f"{document_text}\n\n"
        f"Summary:"
    )

    reasoning = (
        f"Prompt style selected based on document length ({length} characters). "
        f"This ensures optimal balance between brevity and completeness."
    )

    return {
        "prompt": prompt,
        "reasoning": reasoning
    }


if __name__ == "__main__":
    sample_text = "This is a sample document used to demonstrate prompt construction."
    result = build_summarization_prompt(sample_text)
    print(result)
