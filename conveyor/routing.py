from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import receiver.routing

application = ProtocolTypeRouter({
    # (http->django views are added by default)

    'websocket': AuthMiddlewareStack(
        URLRouter(
             receiver.routing.websocket_urlpatterns
        )
    ),

})
