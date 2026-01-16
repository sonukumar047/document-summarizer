import time
import random
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class TransientAPIError(Exception):
    """Simulates transient AWS API failure."""
    pass


def mock_aws_api_call():
    """
    Mock AWS API call that randomly fails.
    """
    if random.random() < 0.6:
        raise TransientAPIError("Simulated transient AWS service failure.")
    return "API call successful"


def call_with_retry(max_retries: int = 5, base_delay: float = 1.0) -> dict:
    """
    Calls a mock AWS API with exponential backoff retry logic.
    """

    attempt = 0

    while attempt < max_retries:
        try:
            logging.info(f"Attempt {attempt + 1} calling AWS API...")
            response = mock_aws_api_call()
            logging.info("API call succeeded.")
            return {
                "success": True,
                "attempts": attempt + 1,
                "response": response
            }

        except TransientAPIError as error:
            attempt += 1
            delay = base_delay * (2 ** attempt)
            logging.warning(f"Failure: {error}. Retrying in {delay:.1f}s...")
            time.sleep(delay)

    logging.error("Max retries exceeded. API call failed.")

    return {
        "success": False,
        "attempts": attempt,
        "error": "Max retries exceeded due to repeated transient failures."
    }


if __name__ == "__main__":
    result = call_with_retry()
    print(result)
