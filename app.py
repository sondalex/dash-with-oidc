from dash import Dash, html
from dash_auth import OIDCAuth
from werkzeug.middleware.proxy_fix import ProxyFix

import conf

app = Dash(__name__)


auth = OIDCAuth(
    app,
    secret_key=conf.SECRET_KEY,
    idp_selection_route="/login",
)

server = app.server  # reference for gunicorn

if not conf.DEBUG:
    server.wsgi_app = ProxyFix(server.wsgi_app, x_for=1, x_host=1)

auth.register_provider(
    "AzureEntra",
    token_endpoint_auth_method="client_secret_post",
    client_id=conf.OIDC_ID,
    client_secret=conf.OIDC_SECRET,
    server_metadata_url=conf.OIDC_METADATA_URL,
    force_https_callback=conf.OIDC_FORCE_HTTPS,
)

app.layout = [
    html.Nav(
        [
            html.Div(html.P("dash-with-auth")),
            html.Div(
                html.A("Logout", href="/oidc/logout")
            ),  # ISSUE: logout does not seem to be working
        ],
        style={
            "display": "flex",
            "flex-direction": "flex-row",
            "justify-content": "space-between",
        },
    ),
    html.H1("Dash With Authentication"),
    html.Div(
        [
            html.P(
                "dash-with-auth: Example of OIDC authentication in framework plotly dash"
            ),
        ]
    ),
]


if __name__ == "__main__":
    # If gunicorn is not used
    app.run(debug=conf.DEBUG, port=conf.PORT, host=conf.HOST)
