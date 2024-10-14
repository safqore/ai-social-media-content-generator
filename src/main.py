from src.nlp_model import analyze_posts

def main():
    posts = [
        "I love the weather today!",
        "I feel sad.",
        "I think my cat is not feeling well."
    ]
    analyze_posts(posts)

if __name__ == "__main__":
    main()