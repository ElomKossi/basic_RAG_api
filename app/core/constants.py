from enum import StrEnum

# on local we just need 1 worker, no need to spawn multiple threads
DEFAULT_NUMBER_OF_WORKERS_ON_LOCAL = 1  


# we could have any number of environments here, this is useful when
# defining settings/behavior per environment - eg on production
# you probably do not want debug enabled and so on.
class Environments(StrEnum):
    LOCAL = "local"
    PRODUCTION = "production"