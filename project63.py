import random

# Define basic categories
industries = ["healthcare", "education", "finance", "gaming", "agriculture", "fashion", "mental wellness", "AI"]
tech_stack = ["mobile app", "web platform", "AI tool", "IoT device", "blockchain solution", "SaaS"]
target_audience = ["freelancers", "small businesses", "college students", "remote workers", "parents", "seniors"]

# Ask user for input to customize the idea
user_name = input("What's your name? ")
user_interest = input("What industry are you interested in? (e.g., education, health, finance): ").lower()
user_problem = input("What's a problem you'd like to solve? ")

# Generate startup idea
selected_industry = user_interest if user_interest in industries else random.choice(industries)
selected_tech = random.choice(tech_stack)
selected_audience = random.choice(target_audience)

# Output the startup idea
print("\n🚀 Startup Idea Generator")
print(f"{user_name}, here's a startup idea for you:")
print(f"Build a {selected_tech} in the {selected_industry} space that helps {selected_audience} solve the problem of '{user_problem}'.")
