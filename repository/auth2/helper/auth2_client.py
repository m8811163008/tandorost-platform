import secrets
import token
from authlib.oauth2.rfc6749 import ClientMixin
from authlib.oauth2.rfc6749 import list_to_scope
from authlib.oauth2.rfc6749 import scope_to_list
from authlib.common.encoding import json_dumps
from authlib.common.encoding import json_loads

# A client is an application making protected resource requests
# on behalf of the resource owner and with its authorization.
# It contains at least three information:
class Auth2Client(ClientMixin):
    client_id: str
    client_secret: str
    #     * authorization_code
    # * implicit
    # * client_credentials
    # * password
    allowed_grant_types : list[str]
    allowed_redirect_uris : list[str]
    # code and token
    allowed_response_types :  list[str]
    #     “none”: The client is a public client as defined in OAuth 2.0,
    # and does not have a client secret.

    # “client_secret_post”: The client uses the HTTP POST parameters
    # as defined in OAuth 2.0

    # “client_secret_basic”: The client uses HTTP Basic as defined in
    # OAuth 2.0
    token_endpoint_auth_method: str #add enum
    scope : set[str]
    default_redirect_uri : str

    def get_client_id(self) -> str:
        """A method to return client_id of the client. For instance, the value
        in database is saved in a column called ``client_id``::

            def get_client_id(self):
                return self.client_id

        :return: string
        """
        return self.client_id

    def get_default_redirect_uri(self):
        """A method to get client default redirect_uri. For instance, the
        database table for client has a column called ``default_redirect_uri``::

            def get_default_redirect_uri(self):
                return self.default_redirect_uri

        :return: A URL string
        """
        return self.default_redirect_uri

    def get_allowed_scope(self, scope) -> str:
        """A method to return a list of requested scopes which are supported by
        this client. For instance, there is a ``scope`` column::

            def get_allowed_scope(self, scope):
                if not scope:
                    return ""
                allowed = set(scope_to_list(self.scope))
                return list_to_scope([s for s in scope.split() if s in allowed])

        :param scope: the requested scope.
        :return: string of scope
        """
        if not scope:
            return ""
        allowed = set(scope_to_list(self.scope))
        return list_to_scope([s for s in scope.split() if s in allowed])

    def check_redirect_uri(self, redirect_uri) -> bool:
        """Validate redirect_uri parameter in Authorization Endpoints. For
        instance, in the client table, there is an ``allowed_redirect_uris``
        column::

            def check_redirect_uri(self, redirect_uri):
                return redirect_uri in self.allowed_redirect_uris

        :param redirect_uri: A URL string for redirecting.
        :return: bool
        """
        return redirect_uri in self.allowed_redirect_uris

    def check_client_secret(self, client_secret) -> bool:
        """Check client_secret matching with the client. For instance, in
        the client table, the column is called ``client_secret``::

            import secrets


            def check_client_secret(self, client_secret):
                return secrets.compare_digest(self.client_secret, client_secret)

        :param client_secret: A string of client secret
        :return: bool
        """
        return secrets.compare_digest(self.client_secret, client_secret)
        

    def check_endpoint_auth_method(self, method, endpoint) -> bool:
        """Check if client support the given method for the given endpoint.
        There is a ``token_endpoint_auth_method`` defined via `RFC7591`_.
        Developers MAY re-implement this method with::

            def check_endpoint_auth_method(self, method, endpoint):
                if endpoint == "token":
                    # if client table has ``token_endpoint_auth_method``
                    return self.token_endpoint_auth_method == method
                return True

        Method values defined by this specification are:

        *  "none": The client is a public client as defined in OAuth 2.0,
            and does not have a client secret.

        *  "client_secret_post": The client uses the HTTP POST parameters
            as defined in OAuth 2.0

        *  "client_secret_basic": The client uses HTTP Basic as defined in
            OAuth 2.0

        .. _`RFC7591`: https://tools.ietf.org/html/rfc7591
        """
        if endpoint == "token":
                    # if client table has ``token_endpoint_auth_method``
                    return self.token_endpoint_auth_method == method
        return True

    def check_token_endpoint_auth_method(self, method):
        # deprecate("Please implement ``check_endpoint_auth_method`` instead.")
        return self.check_endpoint_auth_method(method, "token")

    def check_response_type(self, response_type) -> bool:
        """Validate if the client can handle the given response_type. There
        are two response types defined by RFC6749: code and token. For
        instance, there is a ``allowed_response_types`` column in your client::

            def check_response_type(self, response_type):
                return response_type in self.response_types

        :param response_type: the requested response_type string.
        :return: bool
        """
        return response_type in self.response_types

    def check_grant_type(self, grant_type) -> bool:
        """Validate if the client can handle the given grant_type. There are
        four grant types defined by RFC6749:

        * authorization_code
        * implicit
        * client_credentials
        * password

        For instance, there is a ``allowed_grant_types`` column in your client::

            def check_grant_type(self, grant_type):
                return grant_type in self.grant_types

        :param grant_type: the requested grant_type string.
        :return: bool
        """
        return grant_type in self.grant_types
        