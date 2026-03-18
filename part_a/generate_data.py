import json
import random

languages = ["hindi", "hinglish", "english"]
outcomes = ["payment_committed", "callback_scheduled", "escalated", "no_resolution"]

agent_lines = [
    "Sir aapka EMI due hai",
    "Please pay your EMI",
    "Aapka payment pending hai",
    "Kindly clear your dues"
]

customer_lines = [
    "Kal pay kar dunga",
    "I will pay tomorrow",
    "Thoda time chahiye",
    "Abhi paisa nahi hai"
]

def generate_turn(role):
    if role == "agent":
        return {"role": role, "text": random.choice(agent_lines)}
    else:
        return {"role": role, "text": random.choice(customer_lines)}

def inject_errors(conversation):
    error_type = random.choice([
        "empty_text",
        "duplicate_turn",
        "less_turns",
        "invalid_metadata",
        "wrong_language",
        "garbled_text",
        "none"
    ])

    if error_type == "empty_text":
        if conversation["turns"]:
            conversation["turns"][0]["text"] = ""

    elif error_type == "duplicate_turn":
        if len(conversation["turns"]) >= 2:
            conversation["turns"][1] = conversation["turns"][0]

    elif error_type == "less_turns":
        conversation["turns"] = conversation["turns"][:1]

    elif error_type == "invalid_metadata":
        conversation["metadata"]["call_duration_seconds"] = -100
        conversation["metadata"]["outcome"] = None

    elif error_type == "wrong_language":
        conversation["language"] = "hindi"
        conversation["turns"][0]["text"] = "I will pay tomorrow"

    elif error_type == "garbled_text":
        if conversation["turns"]:
            conversation["turns"][0]["text"] = "@@@###$$$"

    return conversation, error_type

def generate_conversation(i):
    num_turns = random.randint(2, 5)
    turns = []

    for j in range(num_turns):
        role = "agent" if j % 2 == 0 else "customer"
        turns.append(generate_turn(role))

    conversation = {
        "conversation_id": f"conv_{i:03}",
        "language": random.choice(languages),
        "turns": turns,
        "metadata": {
            "call_duration_seconds": random.randint(30, 300),
            "outcome": random.choice(outcomes)
        }
    }

    return conversation

def main():
    error_log = []

    with open("raw_conversations.jsonl", "w") as f:
        for i in range(100):
            conv = generate_conversation(i)

            # inject errors in ~35%
            if random.random() < 0.35:
                conv, error_type = inject_errors(conv)
                error_log.append((conv["conversation_id"], error_type))

            f.write(json.dumps(conv) + "\n")

    # save error log (important for writeup)
    with open("error_log.txt", "w") as log:
        for cid, err in error_log:
            log.write(f"{cid}: {err}\n")

if __name__ == "__main__":
    main()