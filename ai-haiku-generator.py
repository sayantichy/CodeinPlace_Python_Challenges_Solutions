from ai import call_gpt

def main():
    # Prompt for user input
    name = input("Enter your name: ")
    topic = input("Enter a topic: ")

    print("Creating your haiku...\n")

    # Craft a creative prompt for GPT
    prompt = (
        f"Write a haiku in English about the topic '{topic}', incorporating the name '{name}'. "
        "The haiku should follow the 5-7-5 syllable structure, be poetic and thoughtful, "
        "and capture a moment or emotion related to the topic."
    )

    # Generate the haiku using call_gpt
    haiku = call_gpt(prompt)

    # Print the result
    print(haiku)

if __name__ == "__main__":
    main()
