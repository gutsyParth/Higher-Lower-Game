import random
from data import data
import art

a = random.randint(0, len(data) - 1)

score = 0
print(art.logo)


def verdict(choice, follower_a, follower_b):
    if choice == "A" and follower_a > follower_b:
        return True
    elif choice == "B" and follower_a < follower_b:
        return True
    return False


def format_data(data):
    return f"""{data["name"]}, a {data["description"]}, from {data["country"]}"""


while True:
    b = random.randint(0, len(data) - 1)
    while b == a:
        b = random.randint(0, len(data) - 1)

    print(f"""Compare A: {format_data(data[a])}.""")
    print(art.vs)
    print(f"""Compare B: {format_data(data[b])}.""")
    choice = input("Who has more followers? Type 'A' or 'B': ")

    print("\n" * 20)
    print(art.logo)

    if verdict(choice, data[a]["follower_count"], data[b]["follower_count"]):
        score += 1
        print(f"You're right! Current score: {score}")
        a = b
    else:
        print(f"Sorry that's wrong. Final score: {score}")
        break
