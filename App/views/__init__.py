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
from .lendingNotifications import lendingNotification_views
from .report import report_views
from .reportNotification import reportingNotification_views
from .myLendingOffers import myLendingOffers_views

views = [user_views, index_views, trend_views, leaderboard_views, myitems_views,report_views, comment_views, lendingOffer_views,lendingRequests_views,rating_views,manager_views,lendingNotification_views,reportingNotification_views, myLendingOffers_views]