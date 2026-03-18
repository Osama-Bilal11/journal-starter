from datetime import UTC, datetime
import json
import os
from openai import OpenAI
from api.services.entry_service import EntryService

token = os.getenv("OPENAI_API_KEY")
endpoint = os.getenv("OPENAI_BASE_URL")
model = os.getenv("OPENAI_MODEL")


client = OpenAI(
    base_url=endpoint,
    api_key=token,
)


async def analyze_journal_entry(entry_id: str, entry_text: str) -> dict:

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": (
                    "should return sentiment, a 2-sentence summary, and 2-4 key topics. "
                    "return using the following json format: "
                    "{"
                    '"sentiment": "sentiment of the journal entry (positive, negative, neutral)", '
                    '"summary": "2-sentence summary of the journal entry", '
                    '"topics": ["2-4 key topics from the journal entry"], '
                    "}"
                )
            },
            {
                "role": "user",
                "content": entry_text
            }
        ],

        model=model
    )
    entry_data = json.loads(response.choices[0].message.content)
    now = datetime.now(UTC)

    analysis = {
        "entry_id": entry_id,
        **entry_data,
        "created_at": now.isoformat(),
    }

    print(analysis)
    return analysis
