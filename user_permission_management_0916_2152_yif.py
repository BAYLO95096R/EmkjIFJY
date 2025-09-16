# 代码生成时间: 2025-09-16 21:52:13
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.exceptions import DropItem
from scrapy.item import Field, Item

# Define the User item structure
class UserItem(Item):
    username = Field()
    permissions = Field()

# Define the UserPermissionManager class
class UserPermissionManager:
    # Initialize the UserPermissionManager with a dictionary of users and their permissions
    def __init__(self, user_permissions):
        self.user_permissions = user_permissions

    # Check if a user has a specific permission
    def has_permission(self, username, permission):
        # Error handling for unknown user
        if username not in self.user_permissions:
            raise ValueError(f"User {username} not found.")
        # Check if the user has the permission
        return permission in self.user_permissions[username]

    # Add a new user with permissions
    def add_user(self, username, permissions):
        if username in self.user_permissions:
            raise ValueError(f"User {username} already exists.")
        self.user_permissions[username] = permissions

    # Remove a user
    def remove_user(self, username):
        if username not in self.user_permissions:
            raise ValueError(f"User {username} not found.")
        del self.user_permissions[username]

    # Update a user's permissions
    def update_permissions(self, username, new_permissions):
        if username not in self.user_permissions:
            raise ValueError(f"User {username} not found.")
        self.user_permissions[username] = new_permissions

# Example usage of the UserPermissionManager
if __name__ == '__main__':
    # Create a dictionary of users and their permissions
    users = {
        "alice": ["read", "write"],
        "bob": ["read"]
    }

    # Initialize the UserPermissionManager
    manager = UserPermissionManager(users)

    # Check permissions
    try:
        print("Alice has write permission: ", manager.has_permission("alice", "write"))
        print("Bob has write permission: ", manager.has_permission("bob", "write"))
    except ValueError as e:
        print(e)

    # Add a new user
    try:
        manager.add_user("charlie", ["read"])
    except ValueError as e:
        print(e)

    # Update a user's permissions
    try:
        manager.update_permissions("alice", ["read", "write", "delete"])
    except ValueError as e:
        print(e)

    # Remove a user
    try:
        manager.remove_user("bob")
    except ValueError as e:
        print(e)