class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    ENV = "Staging"
    EXPLAIN_TEMPLATE_LOADING = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    ENV = "Development"
    EXPLAIN_TEMPLATE_LOADING = True