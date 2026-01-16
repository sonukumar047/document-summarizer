import boto3
import json
from botocore.exceptions import NoCredentialsError, ClientError


def invoke_bedrock(prompt: str) -> str:
    """
    Invokes Amazon Bedrock (Claude 3 Sonnet) to generate a summary.
    Falls back to mock response if AWS credentials are not available.
    """

    try:
        client = boto3.client(
            service_name="bedrock-runtime",
            region_name="us-east-1"
        )

        response = client.invoke_model(
            modelId="anthropic.claude-3-sonnet-20240229-v1:0",
            contentType="application/json",
            accept="application/json",
            body=json.dumps({
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 300,
                "temperature": 0.2,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            })
        )

        response_body = json.loads(response["body"].read())
        return response_body["content"][0]["text"]

    except (NoCredentialsError, ClientError) as e:
        # Safe fallback for local execution
        return (
            "[MOCK RESPONSE]\n"
            "This is a simulated summary response from Amazon Bedrock.\n"
            "Reason: AWS credentials or Bedrock access not available locally."
        )



if __name__ == "__main__":
    sample_prompt = """
    Summarize the following document in 3 bullet points:

    Artificial Intelligence is transforming industries by enabling
    automation, data-driven decisions, and intelligent systems.
    """

    summary = invoke_bedrock(sample_prompt)
    print("\n=== Bedrock Response ===\n")
    print(summary)
