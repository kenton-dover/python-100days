import itertools
'''
Write a function called friends_teams that takes a list of friends, a team_size (type int, default=2) and order_does_matter (type bool, default False).

Return all possible teams. Hint: if order matters (order_does_matter=True), the number of teams would be greater.

See the tests for more details. Enjoy :)
'''


def friends_teams(listOfFriends, team_size=2, order_does_matter=False):
    if order_does_matter:
        return itertools.permutations(listOfFriends, team_size)
    else:
        return itertools.combinations(listOfFriends, team_size)
