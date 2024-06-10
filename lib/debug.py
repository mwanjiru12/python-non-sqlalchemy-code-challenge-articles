from author import Author
from magazine import Magazine
from article import Article

# Create instances
author1 = Author("John Doe")
author2 = Author("Jane Smith")
magazine1 = Magazine("Tech Today", "Technology")
magazine2 = Magazine("Health Weekly", "Health")

# Add articles
article1 = author1.add_article(magazine1, "The Rise of AI")
article2 = author1.add_article(magazine2, "Health Tips for 2024")
article3 = author2.add_article(magazine1, "Quantum Computing Explained")
article4 = author1.add_article(magazine1, "Blockchain Technology")

# Debugging
import ipdb; ipdb.set_trace()
