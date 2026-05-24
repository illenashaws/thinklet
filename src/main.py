from datetime import datetime
import json
import os

BASE_DIR = os.path.dirname(__file__)
MEMORY_FILE = os.path.join(BASE_DIR, "memory.json")


def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    return {}


def save_memory(data):
    with open(MEMORY_FILE, "w") as file:
        json.dump(data, file, indent=2)
        file.flush()
        os.fsync(file.fileno())


def suggest_choice(choice1, choice2, stress, importance):

    if stress >= 8 and importance >= 8:

        if "sleep" in choice1.lower():
            suggestion = choice1
        elif "sleep" in choice2.lower():
            suggestion = choice2
        else:
            suggestion = choice1

        reason = (
            f"your stress level is high ({stress}/10), "
            f"and your energy deserves care too."
        )

    elif stress >= 8:

        if "sleep" in choice1.lower():
            suggestion = choice1
        elif "sleep" in choice2.lower():
            suggestion = choice2
        else:
            suggestion = choice1

        reason = (
            f"your stress level is high ({stress}/10). "
            "Rest may help you think more clearly."
        )

    elif importance >= 8:

        suggestion = choice2

        reason = (
            f"importance feels high ({importance}/10), "
            "so focusing on responsibility first may help."
        )

    else:

        if "jog" in choice1.lower():
            suggestion = choice1
        elif "jog" in choice2.lower():
            suggestion = choice2
        else:
            suggestion = choice1

        reason = (
            f"your stress level is manageable ({stress}/10), "
            "so this feels like a good time to build momentum."
        )

    return suggestion, reason


def main():

    print("Thinklet is waking up... 🌤️")

    memory = load_memory()

    if "name" in memory:

        print(
            f"Welcome back, {memory['name']}! "
            "I was hoping it was you. 🌱"
        )

    else:

        name = input("What should I call you? ").strip()

        memory["name"] = name

        print(
            f"Hello, {name}. Nice to meet you!"
        )

    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    memory["last_seen"] = now

    save_memory(memory)

    print("Thinklet is listening..\n")

    decision = input(
        "What decision are you trying to make?\n> "
    )

    stress = int(
        input("Stress level (1-10): ")
    )

    importance = int(
        input("Importance level (1-10): ")
    )

    choices = decision.split(" or ")

    print("\nThinklet thinks:\n")

    if len(choices) == 2:

        choice1 = choices[0].strip()
        choice2 = choices[1].strip()

        suggestion, reason = suggest_choice(
            choice1,
            choice2,
            stress,
            importance
        )

        print(
            f"It might be better if you choose:\n"
        )

        print(
            f"→ {suggestion}\n"
        )

        print(
            f"Because {reason}"
        )

    else:

        print(
            "I understand your situation."
        )

        print(
            f"Stress level: {stress}/10"
        )

        print(
            f"Importance level: {importance}/10"
        )

        print(
            "Can you separate the options using 'or'?"
        )

    print("\n🌱 Thinklet is still learning.")


if __name__ == "__main__":
    main()