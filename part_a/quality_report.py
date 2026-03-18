import json
from collections import Counter

# ----------- LOAD FUNCTION -----------

def load_jsonl(file):
    data = []
    with open(file) as f:
        for line in f:
            data.append(json.loads(line))
    return data

# ----------- LOAD DATA -----------

raw = load_jsonl("raw_conversations.jsonl")
cleaned = load_jsonl("cleaned_conversations.jsonl")
rejected = load_jsonl("rejected_conversations.jsonl")

# ----------- BASIC COUNTS -----------

total_raw = len(raw)
total_cleaned = len(cleaned)
total_rejected = len(rejected)

print("📊 DATA SUMMARY")
print(f"Total Raw: {total_raw}")
print(f"Cleaned: {total_cleaned}")
print(f"Rejected: {total_rejected}")

# ----------- REJECTION REASONS -----------

reasons = Counter([r.get("rejection_reason", "unknown") for r in rejected])

print("\n📉 Rejection Breakdown:")
for reason, count in reasons.items():
    percent = (count / total_raw) * 100
    print(f"{reason}: {count} ({percent:.2f}%)")

# ----------- LANGUAGE DISTRIBUTION -----------

lang_raw = Counter([r.get("language", "unknown") for r in raw])
lang_clean = Counter([c.get("language", "unknown") for c in cleaned])

print("\n🌐 Language Distribution (Before Cleaning):")
for k, v in lang_raw.items():
    print(f"{k}: {v}")

print("\n🌐 Language Distribution (After Cleaning):")
for k, v in lang_clean.items():
    print(f"{k}: {v}")

# ----------- OUTCOME DISTRIBUTION -----------

def get_outcomes(data):
    outcomes = []
    for d in data:
        metadata = d.get("metadata", {})
        outcomes.append(metadata.get("outcome", "unknown"))
    return Counter(outcomes)

outcome_raw = get_outcomes(raw)
outcome_clean = get_outcomes(cleaned)

print("\n📌 Outcome Distribution (Before Cleaning):")
for k, v in outcome_raw.items():
    print(f"{k}: {v}")

print("\n📌 Outcome Distribution (After Cleaning):")
for k, v in outcome_clean.items():
    print(f"{k}: {v}")

# ----------- AVG TURNS -----------

def avg_turns(data):
    total_turns = sum(len(d.get("turns", [])) for d in data)
    return total_turns / len(data) if data else 0

print("\n🔁 Average Turns per Conversation:")
print(f"Before Cleaning: {avg_turns(raw):.2f}")
print(f"After Cleaning: {avg_turns(cleaned):.2f}")