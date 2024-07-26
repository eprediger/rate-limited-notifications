class RateLimitExceededError(Exception):
    def __init__(self):
        self.code = "RATE_LIMIT_EXCEEDED_ERROR"
        self.message = 'Rate limit exceeded'
