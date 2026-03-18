import json
import re
from collections import Counter

# ----------- VALIDATION FUNCTIONS -----------

def has_min_turns(conv):
    return len(conv.get("turns", [])) >= 2

def has_no_empty_turns(conv):
    for turn in conv.get("turns", []):
        if not turn.get("text", "").strip():
            return False
    return True

def has_no_duplicate_turns(conv):
    turns = conv.get("turns", [])
    for i in range(1, len(turns)):
        if turns[i].get("text") == turns[i-1].get("text") and turns[i].get("role") == turns[i-1].get("role"):
            return False
    return True

def has_valid_metadata(conv):
    metadata = conv.get("metadata", {})
    
    if metadata.get("call_duration_seconds", 0) < 0:
        return False
    
    if metadata.get("outcome") is None:
        return False

    return True

def has_no_garbled_text(conv):
    pattern = re.compile(r"[^\w\s.,!?]")
    for turn in conv.get("turns", []):
        if pattern.search(turn.get("text", "")):
            return False
    return True

def language_matches(conv):
    lang = conv.get("language", "").lower()
    text = " ".join([t.get("text", "") for t in conv.get("turns", [])]).lower()

    if lang == "hindi":
        return any(word in text for word in ["hai", "nahi", "kar", "aap"])
    elif lang == "english":
        return any(word in text for word in ["pay", "please", "tomorrow"])
    elif lang == "hinglish":
        return True
    return False

# ----------- MAIN VALIDATION -----------

def validate_conversation(conv):
    if not has_min_turns(conv):
        return False, "less_than_2_turns"

    if not has_no_empty_turns(conv):
        return False, "empty_turn"

    if not has_no_duplicate_turns(conv):
        return False, "duplicate_turn"

    if not has_valid_metadata(conv):
        return False, "invalid_metadata"

    if not has_no_garbled_text(conv):
        return False, "garbled_text"

    if not language_matches(conv):
        return False, "language_mismatch"

    return True, None


# ----------- PROCESS FILE -----------

cleaned = []
rejected = []
error_count = Counter()

with open("raw_conversations.jsonl") as f:
    for line in f:
        try:
            conv = json.loads(line)

            valid, reason = validate_conversation(conv)

            if valid:
                cleaned.append(conv)
            else:
                conv["rejection_reason"] = reason
                rejected.append(conv)
                error_count[reason] += 1

        except Exception as e:
            rejected.append({
                "raw_line": line,
                "rejection_reason": f"parse_error: {str(e)}"
            })
            error_count["parse_error"] += 1


# ----------- SAVE OUTPUT -----------

with open("cleaned_conversations.jsonl", "w") as f:
    for c in cleaned:
        f.write(json.dumps(c) + "\n")

with open("rejected_conversations.jsonl", "w") as f:
    for r in rejected:
        f.write(json.dumps(r) + "\n")


# ----------- PRINT SUMMARY -----------

print("Cleaning Complete ✅")
print(f"Total Cleaned: {len(cleaned)}")
print(f"Total Rejected: {len(rejected)}")

print("\nRejection Breakdown:")
for reason, count in error_count.items():
    print(f"{reason}: {count}")