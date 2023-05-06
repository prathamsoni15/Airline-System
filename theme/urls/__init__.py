#from .auth import authUrls
from .category import categoryURL
from .airline import airlineURL
from .status import statusURL
from .cargo import cargoURL
from .booking import bookingURL
from .car import carURL
from .cancel import cancelURL
from .branch import branchURL
from .passenger import passengerURL
from .ticket import ticketURL
from .route import routeURL
from .fare import fareURL
from .concession import concessionURL
from .feedback import FeedbackURL
from .signup import SIGNUPURL

urlpatterns=categoryURL+airlineURL+statusURL+cargoURL+bookingURL+carURL+cancelURL+branchURL+passengerURL+ticketURL+routeURL+fareURL+concessionURL+FeedbackURL+SIGNUPURL

#authUrls