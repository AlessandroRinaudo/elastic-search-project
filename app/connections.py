from elasticsearch import Elasticsearch
import logstash
import logging

# Logstash initialization
host = 'logs-container'
test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.LogstashHandler(host, 5959, version=1))

es = Elasticsearch([{'host': 'es-container', 'port': 9200}])
