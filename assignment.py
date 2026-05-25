##
# social_tracker.py
# tracks your social activity
# drishti
# 17
# 11.05.26

def view_posts(posts):
    """functionality to view all posts stored in list"""
    print("All posts")

    for item in posts:
        print(item)


def add_posts(posts, title, category, views):
    """allows user to add a new item"""

    new_post = {
        "title": title,
        "category": category,
        "views": views
    }

    posts.append(new_post)
    print("Posted")


def update_views(posts, title, new_views):
    """updates number of views"""

    found = False

    for item in posts:
        if item["title"].lower() == title.lower():
            item["views"] = new_views
            print("Views updated")
            found = True

    if not found:
        print("Post not found")


def delete_posts(posts, title):
    """deletes a post"""

    for i in range(len(posts)):
        if posts[i]["title"].lower() == title.lower():
            del posts[i]
            print("Post deleted")
            return

    print("Post not found")

def show_trending(posts, min_views):
    """shows trending posts"""

    print("Trending posts")

    for item in posts:
        if item["views"] >= min_views:
            print(item)


if __name__ == "__main__":

    menu = [
        {"title": "hie", "category": "comments", "views": 120},
        {"title": "my food vlog", "category": "vlog", "views": 500},
        {"title": "cat", "category": "animals", "views": 98064},
        {"title": "recipe", "category": "food", "views": 6789},
        {"title": "nails!", "category": "fashion", "views": 700}
    ]

    running = True

    while running:

        print("\nMenu")
        print("1. View all posts")
        print("2. Add a post")
        print("3. Update views")
        print("4. Delete a post")
        print("5. Trending posts")
        print("6. Exit")

        choice = input("Enter a choice: ")

        if choice == "1":
            view_posts(menu)

        elif choice == "2":
            title = input("Enter post title: ")
            category = input("Enter category: ")
            views = int(input("Enter number of views: "))

            add_posts(menu, title, category, views)

        elif choice == "3":
            title = input("Enter post title to update: ")
            new_views = int(input("Enter new number of views: "))

            update_views(menu, title, new_views)

        elif choice == "4":
            title = input("Enter post title to delete: ")

            delete_posts(menu, title)

        elif choice == "5":
            min_views = int(input("Enter minimum views: "))

            show_trending(menu, min_views)

        elif choice == "6":
            running = False
            print("Goodbye!")

        else:
            print("Invalid choice, try again.")
        
        
        







    
    
    

