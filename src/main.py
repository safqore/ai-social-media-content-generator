from src.nlp-model import analyze_posts

def main():
    posts = [
        "I love the weather today!",
        "I feel sad.",
        "I think my cat is not feeling well."
    ]
    trends = analyze_posts(posts)

if __name__ == "__main__":
    main()