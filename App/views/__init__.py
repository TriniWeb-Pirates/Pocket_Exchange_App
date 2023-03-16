from .user import user_views
from .index import index_views
from .trendingpage import trend_views
from .leaderboard import leaderboard_views
from .myitems import myitems_views
from .lendingOffer import lendingOffer_views
from .lendingRequest import lendingRequests_views
from .commentViews import comment_views
from .rating import rating_views
from .manager import manager_views

views = [user_views, index_views, trend_views, leaderboard_views, myitems_views, comment_views, lendingOffer_views,lendingRequests_views,rating_views,manager_views]