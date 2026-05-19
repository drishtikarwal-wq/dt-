##
#social_tracker.py
#tracks your social activity
#drishti
#17
#11.05.26

##def view_items(items):
##    """functionality to view all items stored in list"""


menu = []
#while loop to repeat menu and functions
again = True

while again:

    print("Menu: ")
    print("1. All_posts")
    print("2. Add_a_post")
    print("3 Change_number_of_views")
    print("4. Delete_a_post")
    print("5. Generate_a_post")
    print("6. Exit")

    choice = input("enter your choice")
if choice == "1":
    add_posts(title, views, category)

def add_posts(title, views, category):
    """allows user to add a new item with title, views and category"""
    new_post = {"title": title, "category": category, "views": views}
    menu.append(new_post)
    print("posted") # confirmation message that item has been successfully added

item = input("enter the post title")
category = input("enter the post category")
views = input("enter the number of views")

add_posts("My food vlog", 150, "vlogs")


##    def all_posts():
##        """shows post title and content type"""
##        print("\n--- All Posts ---")
##        # loop over each post that is stored in the program
##        for item in items:
##            print(item)

 
        
    

###while loop to repeat menu and functions
##again = True
##
##while again:
##
##    print("Menu: ")
##    print("1. All_posts")
##    print("2. Add_a_post")
##    print("3 Change_number_of_views")
##    print("4. Delete_a_post")
##    print("5. Generate_a_post")
##    print("6. Exit")
##
##    choice = input("enter your choice")

        
        
        







    
    
    

