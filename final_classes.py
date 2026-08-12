from typing import final

@final
class SecurityManager:
    """This class handles critical security operations
    and shouldn't be subclassed to prevent security bypasses."""
    def authenticate(self, username: str, password: str) -> bool:
        # Authentication logic
        return True

    @final
    def validate_token(self, token: str) -> bool:
        # Token validation logic that shouldn't be overridden
        return len(token) > 10

# This would trigger a type error:
class EnhancedSecurityManager(SecurityManager): # Error!
    pass