# product_catalog.py

from product_data import products

# --- Collect Customer Preferences ---
customer_preferences = []
while True:
    pref = input("Input a preference: ").strip().lower()
    if pref:
        customer_preferences.append(pref)
    more = input("Do you want to add another preference? (Y/N): ").strip().upper()
    if more == "N":
        break

# Convert to set to remove duplicates
customer_preferences = set(customer_preferences)


# --- Helper Functions ---
def count_matches(product_tags, preferences):
    """Return number of overlapping tags between a product and customer preferences"""
    return len(product_tags & preferences)  # set intersection


def recommend_products(products, customer_preferences):
    """Return products with at least 1 matching tag, sorted by match score"""
    recommendations = []
    for product in products:
        matches = count_matches(product["tags"], customer_preferences)
        if matches > 0:
            recommendations.append((product["name"], matches))

    # Sort by number of matches (descending), then alphabetically
    recommendations.sort(key=lambda x: (-x[1], x[0]))
    return recommendations


# --- Main Execution ---
recommended = recommend_products(products, customer_preferences)

print("\nRecommended Products:")
for name, score in recommended:
    print(f"- {name} ({score} match(es))")
Design Memo

This recommendation tool uses lists to store the product catalog and customer input, 
and then converts the preferences and product tags into sets. The main advantage of 
sets here is the ability to perform fast intersection operations, which let us quickly 
count the number of matching tags between customer preferences and product attributes. 
The function `count_matches()` leverages set intersection (&) to return the number of 
overlapping tags, a core operation that is both efficient and easy to read.

Iteration (loops) is another key operation. We iterate over each product, compute matches, 
and store results in a list of tuples containing product names and match counts. Finally, 
we sort the recommendations by match score so customers see the strongest matches first.

If this program had to handle 1,000+ products**, the main changes would involve 
optimizations. Right now, the approach is still efficient, because set intersections 
scale well compared to nested loops. However, as the catalog grows, we might store products 
in a database rather than a list, and implement indexing on tags for faster lookups. 
Additionally, we could explore caching results for common preference combinations or 
use machine learning models for more advanced personalization. For now, though, this 
set-based logic balances readability with performance, making it ideal for a prototype.
 
