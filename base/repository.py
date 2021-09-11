"""リポジトリパターンに基づいてデータのやり取りを決める
"""
from django.db.models import Q

from .models import Friend


class UserRepository(object):

    @classmethod
    def filter_unselected_friends(cls, proposer, *selected_friend_ids):
        friends = Friend.objects.filter(followed_user=proposer)

        query = Q()
        for selected_friend_id in selected_friend_ids:
            query |= Q(id=selected_friend_id)
        filtered_friends = friends.exclude(query)

        return filter_unselected_friends
