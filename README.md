# dt-
##
#social_tracker.py
#tracks your social activity
#drishti
#17
#11.05.26

def all_posts():
    """shows post title and content type"""
    

#while loop to repeat menu and functions
again = True

while again:

    print("Menu: ")
    print("1. Print_all_posts")
    print("2. Add_a_post")
    print("3 Change_number_of_views")
    print("4. Delete_a_post")
    print("5. generate_a_post")
    print("6. Exit")

    choice = input("enter your choice")

    if choice == "1":
