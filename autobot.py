# from topics import topics
# import random
# from datetime import datetime

# topic = random.choice(topics)

# content = f"""
# # {topic}

# Generated on: {datetime.now()}

# ## Overview

# This note covers {topic}.

# ## Key Points

# - Concept
# - Usage
# - Security Importance

# ## Practice

# Try researching tools related to this topic.
# """

# filename = f"generated_notes/{topic.replace(' ','_')}.md"

# with open(filename, "w") as f:
#     f.write(content)

# print(f"Created note: {filename}")

from topics import topics
import random
from datetime import datetime
import os

topic = random.choice(topics)

content = f"""
# {topic}

Generated on: {datetime.now()}

## Overview

This note covers {topic}.

## Key Points

- Concept
- Usage
- Security Importance

## Practice

Try researching tools related to this topic.
"""

filename = f"generated_notes/{topic.replace(' ','_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"

with open(filename, "w") as f:
    f.write(content)

print(f"Created note: {filename}")

os.system("git add .")
os.system(f'git commit -m "Added note: {topic}"')
os.system("git push")

print("Changes pushed to GitHub")