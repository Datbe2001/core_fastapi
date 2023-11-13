from enum import Enum


class NotificationTemplate(Enum):
    CRUD_PRODUCT_NOTIFICATION_MSG = lambda product_type, product_name, action, user_name: f"The {product_name} {product_type} has just been {action} by {user_name}"

class ActivityTemplate(Enum):
    Activity_MSG = lambda username, action, entity, entity_name, children_name: f"{username} has {action} the {entity} {children_name} - <span style=\"background: linear-gradient(to right, #7AF4AE 0%, #3262DD 100%);\
    -webkit-background-clip: text; background-clip: text; color: transparent; font-weight: bold;\">{entity_name}</span>"

    Activity_Purchase_MSG = lambda action, entity, entity_name, owner: f"You {action}d the {entity} from {owner} - {entity_name}"

class CommentTemplate(Enum):
    Comment_MSG = lambda username, action, entity_name: f"{username} {action} on your post - {entity_name}"
