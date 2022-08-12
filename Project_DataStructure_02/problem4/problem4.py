class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    groups = group.get_groups()

    users = group.get_users()

    if recursive_user(user, users):
        return True

    if recursive_group(user, groups):
        return True

    return False


def recursive_user(user, users):
    if(len(users) == 0):
        return False
    first_element = users[0]
    if first_element == user:
        return True
    sub = user[1:]
    recursive_user(user, sub)


def recursive_group(user, groups):
    if(len(groups) == 0):
        return False

    first_element = groups[0]

    check_user = recursive_user(user, first_element.get_users())
    if check_user:
        return True

    check_group_sub = recursive_group(user, first_element.get_groups())
    if check_group_sub:
        return True

    sub = groups[1:]
    check_group = recursive_group(user, sub)
    if check_group:
        return True


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values
# Test Case 1

print(is_user_in_group('sub_child_user', parent))

# Test Case 2

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_sub_chil = Group("subsubchild")

sub_sub_chil_user = "test"
sub_sub_chil.add_user(sub_sub_chil_user)

sub_child_user = "sub_child_user"

sub_child.add_user(sub_child_user)
sub_child.add_group(sub_sub_chil)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group('sub_child_user', parent))

# Test Case 3

print(is_user_in_group("", parent))
