# 1. Users Database
users = [
    {"name": "Alice", "interest": "data_science", "engagement": "high"},
    {"name": "Bob", "interest": "web-dev", "engagement": "low"},
    {"name": "Charlie", "interest": "ai-ethics", "engagement": "medium"}
]

# 2. Content library
content_blocks = {
    "data_science": "Check out our new predictive modeling whitepaper!",
    "web-dev": "Learn how to optimize your React components for speed.",
    "ai-ethics": "Join our webinar on responsible AI implementation.",
    "default": "Explore the latest tech insights."
}

def generate_m2m_email(user):
    interest = user.get("interest", "default")
    subject_prefix = "Exclusive for you: " if user["engagement"] == "high" else "New update: "
    body_content = content_blocks.get(interest, content_blocks["default"])
    
    email_template = f"""Subject: {subject_prefix} {interest.replace('_', ' ').title()} Insight

Hi {user['name']},

Based on your interest in {interest.replace('_', ' ')}, we thought you'd love this:
{body_content}

Best,
The M2M Team"""

    return email_template

# 3. Execution
for user in users:
    print(f"-- Sending to {user['name']} --")
    print(generate_m2m_email(user))
    print()
