#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    # Create instances for testing
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")
    magazine1 = Magazine("Tech Today", "Technology")
    magazine2 = Magazine("Health Weekly", "Health")

    # Create articles
    article1 = Article(author1, magazine1, "AI in 2024")
    article2 = Article(author1, magazine2, "Healthy Living Tips")
    article3 = Article(author2, magazine1, "Future of Robotics")
    article4 = Article(author1, magazine1, "Quantum Computing Explained")

    # Test methods
    print(author1.name)  # John Doe
    print(author1.articles())  # [article1, article2, article4]
    print(author1.magazines())  # [magazine1, magazine2]
    print(author1.topic_areas())  # ["Technology", "Health"]

    print(magazine1.name)  # Tech Today
    print(magazine1.category)  # Technology
    print(magazine1.articles())  # [article1, article3, article4]
    print(magazine1.contributors())  # [author1, author2]
    print(magazine1.article_titles())  # ["AI in 2024", "Future of Robotics", "Quantum Computing Explained"]
    print(magazine1.contributing_authors())  # None

    print(Magazine.top_publisher().name)  # Tech Today

    # don't remove this line, it's for debugging!
    ipdb.set_trace()
