import logging

logging.basicConfig(level=logging.DEBUG)

requests_log = logging.getLogger("requests")
requests_log.setLevel(logging.WARNING)

urllib3_log = logging.getLogger("urllib3")
urllib3_log.setLevel(logging.WARNING)

elasticsearch_log = logging.getLogger("elasticsearch")
elasticsearch_log.setLevel(logging.WARNING)

stevedore_log = logging.getLogger("stevedore")
stevedore_log.setLevel(logging.WARNING)
