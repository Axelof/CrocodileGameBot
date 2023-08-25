from collections import defaultdict

from database.models import User
from utils.dotdict import DotDict

context_storage: defaultdict[User, DotDict] = defaultdict(DotDict)
