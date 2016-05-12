import random

from chat import local
from chat.utils import get_client_ip


class UserCookieMiddleWare(object):
	"""
	Middleware to set user cookie
	If user is authenticated and there is no cookie, set the cookie,
	If the user is not authenticated and the cookie remains, delete it
	"""

	def process_request(self, request):
		try:
			local.random
		except AttributeError:
			local.random = str(random.randint(0, 10000)).rjust(4, '0')
			local.user = str(getattr(request.user, 'username', '')).rjust(8, ' ')
			local.client_ip = get_client_ip(request)
