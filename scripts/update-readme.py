import re
from datetime import datetime

def update_readme():
    try:
        with open("README.md", "r", encoding="utf-8") as file:
            content = file.read()

        # Update Last Updated Date
        now = datetime.now()
        date_str = now.strftime("%B %d, %Y")
        
        # Replace the Last Updated comment or placeholder
        updated_content = re.sub(
            r"<!-- LAST_UPDATED_START -->.*?<!-- LAST_UPDATED_END -->",
            f"<!-- LAST_UPDATED_START -->{date_str}<!-- LAST_UPDATED_END -->",
            content
        )

        with open("README.md", "w", encoding="utf-8") as file:
            file.write(updated_content)
        
        print("README.md successfully updated with timestamp.")
    except Exception as e:
        print(f"Error updating README.md: {e}")

if __name__ == "__main__":
    update_readme()
