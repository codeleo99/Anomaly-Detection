from datetime import datetime, timedelta
from elasticsearch import Elasticsearch

client = Elasticsearch("http://192.168.0.11:9200/")

def adjustQuery():
  # Eine stunde abziehen, da die API hinterher läuft
  currentTime = datetime.now() - timedelta(hours=1)
  time = currentTime.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'
  time15MinAgo = currentTime - timedelta(minutes=15)
  time15MinAgo = time15MinAgo.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'
  requestQuery = {
    "aggs": {
      "0": {
        "date_histogram": {
          "field": "@timestamp",
          "fixed_interval": "15s",
          "time_zone": "Europe/Berlin"
        },
        "aggs": {
          "1": {
            "percentiles": {
              "field": "system.memory.actual.used.pct",
              "percents": [
                50
              ]
            }
          }
        }
      }
    },
    "size": 0,
    "fields": [
      {
        "field": "@timestamp",
        "format": "date_time"
      },
      {
        "field": "azure.app_insights.end_date",
        "format": "date_time"
      },
      {
        "field": "azure.app_insights.start_date",
        "format": "date_time"
      },
      {
        "field": "azure.app_state.end_date",
        "format": "date_time"
      },
      {
        "field": "azure.app_state.start_date",
        "format": "date_time"
      },
      {
        "field": "azure.billing.usage_date",
        "format": "date_time"
      },
      {
        "field": "azure.billing.usage_end",
        "format": "date_time"
      },
      {
        "field": "azure.billing.usage_start",
        "format": "date_time"
      },
      {
        "field": "ceph.monitor_health.last_updated",
        "format": "date_time"
      },
      {
        "field": "docker.container.created",
        "format": "date_time"
      },
      {
        "field": "docker.healthcheck.event.end_date",
        "format": "date_time"
      },
      {
        "field": "docker.healthcheck.event.start_date",
        "format": "date_time"
      },
      {
        "field": "docker.image.created",
        "format": "date_time"
      },
      {
        "field": "elf.creation_date",
        "format": "date_time"
      },
      {
        "field": "event.created",
        "format": "date_time"
      },
      {
        "field": "event.end",
        "format": "date_time"
      },
      {
        "field": "event.ingested",
        "format": "date_time"
      },
      {
        "field": "event.start",
        "format": "date_time"
      },
      {
        "field": "file.accessed",
        "format": "date_time"
      },
      {
        "field": "file.created",
        "format": "date_time"
      },
      {
        "field": "file.ctime",
        "format": "date_time"
      },
      {
        "field": "file.elf.creation_date",
        "format": "date_time"
      },
      {
        "field": "file.mtime",
        "format": "date_time"
      },
      {
        "field": "file.x509.not_after",
        "format": "date_time"
      },
      {
        "field": "file.x509.not_before",
        "format": "date_time"
      },
      {
        "field": "kubernetes.container.start_time",
        "format": "date_time"
      },
      {
        "field": "kubernetes.event.metadata.timestamp.created",
        "format": "date_time"
      },
      {
        "field": "kubernetes.event.timestamp.first_occurrence",
        "format": "date_time"
      },
      {
        "field": "kubernetes.event.timestamp.last_occurrence",
        "format": "date_time"
      },
      {
        "field": "kubernetes.job.time.completed",
        "format": "date_time"
      },
      {
        "field": "kubernetes.job.time.created",
        "format": "date_time"
      },
      {
        "field": "kubernetes.node.start_time",
        "format": "date_time"
      },
      {
        "field": "kubernetes.pod.start_time",
        "format": "date_time"
      },
      {
        "field": "kubernetes.service.created",
        "format": "date_time"
      },
      {
        "field": "kubernetes.storageclass.created",
        "format": "date_time"
      },
      {
        "field": "kubernetes.system.start_time",
        "format": "date_time"
      },
      {
        "field": "mongodb.replstatus.server_date",
        "format": "date_time"
      },
      {
        "field": "mongodb.status.background_flushing.last_finished",
        "format": "date_time"
      },
      {
        "field": "mongodb.status.local_time",
        "format": "date_time"
      },
      {
        "field": "mssql.transaction_log.stats.backup_time",
        "format": "date_time"
      },
      {
        "field": "mysql.performance.events_statements.last.seen",
        "format": "date_time"
      },
      {
        "field": "nats.server.time",
        "format": "date_time"
      },
      {
        "field": "package.installed",
        "format": "date_time"
      },
      {
        "field": "php_fpm.pool.start_time",
        "format": "date_time"
      },
      {
        "field": "php_fpm.process.start_time",
        "format": "date_time"
      },
      {
        "field": "postgresql.activity.backend_start",
        "format": "date_time"
      },
      {
        "field": "postgresql.activity.query_start",
        "format": "date_time"
      },
      {
        "field": "postgresql.activity.state_change",
        "format": "date_time"
      },
      {
        "field": "postgresql.activity.transaction_start",
        "format": "date_time"
      },
      {
        "field": "postgresql.bgwriter.stats_reset",
        "format": "date_time"
      },
      {
        "field": "postgresql.database.stats_reset",
        "format": "date_time"
      },
      {
        "field": "process.cpu.start_time",
        "format": "date_time"
      },
      {
        "field": "process.elf.creation_date",
        "format": "date_time"
      },
      {
        "field": "process.parent.elf.creation_date",
        "format": "date_time"
      },
      {
        "field": "process.parent.start",
        "format": "date_time"
      },
      {
        "field": "process.start",
        "format": "date_time"
      },
      {
        "field": "system.process.cpu.start_time",
        "format": "date_time"
      },
      {
        "field": "system.service.state_since",
        "format": "date_time"
      },
      {
        "field": "threat.enrichments.indicator.file.accessed",
        "format": "date_time"
      },
      {
        "field": "threat.enrichments.indicator.file.created",
        "format": "date_time"
      },
      {
        "field": "threat.enrichments.indicator.file.ctime",
        "format": "date_time"
      },
      {
        "field": "threat.enrichments.indicator.file.elf.creation_date",
        "format": "date_time"
      },
      {
        "field": "threat.enrichments.indicator.file.mtime",
        "format": "date_time"
      },
      {
        "field": "threat.enrichments.indicator.first_seen",
        "format": "date_time"
      },
      {
        "field": "threat.enrichments.indicator.last_seen",
        "format": "date_time"
      },
      {
        "field": "threat.enrichments.indicator.modified_at",
        "format": "date_time"
      },
      {
        "field": "threat.enrichments.indicator.x509.not_after",
        "format": "date_time"
      },
      {
        "field": "threat.enrichments.indicator.x509.not_before",
        "format": "date_time"
      },
      {
        "field": "threat.indicator.file.accessed",
        "format": "date_time"
      },
      {
        "field": "threat.indicator.file.created",
        "format": "date_time"
      },
      {
        "field": "threat.indicator.file.ctime",
        "format": "date_time"
      },
      {
        "field": "threat.indicator.file.elf.creation_date",
        "format": "date_time"
      },
      {
        "field": "threat.indicator.file.mtime",
        "format": "date_time"
      },
      {
        "field": "threat.indicator.first_seen",
        "format": "date_time"
      },
      {
        "field": "threat.indicator.last_seen",
        "format": "date_time"
      },
      {
        "field": "threat.indicator.modified_at",
        "format": "date_time"
      },
      {
        "field": "threat.indicator.x509.not_after",
        "format": "date_time"
      },
      {
        "field": "threat.indicator.x509.not_before",
        "format": "date_time"
      },
      {
        "field": "tls.client.not_after",
        "format": "date_time"
      },
      {
        "field": "tls.client.not_before",
        "format": "date_time"
      },
      {
        "field": "tls.client.x509.not_after",
        "format": "date_time"
      },
      {
        "field": "tls.client.x509.not_before",
        "format": "date_time"
      },
      {
        "field": "tls.server.not_after",
        "format": "date_time"
      },
      {
        "field": "tls.server.not_before",
        "format": "date_time"
      },
      {
        "field": "tls.server.x509.not_after",
        "format": "date_time"
      },
      {
        "field": "tls.server.x509.not_before",
        "format": "date_time"
      },
      {
        "field": "x509.not_after",
        "format": "date_time"
      },
      {
        "field": "x509.not_before",
        "format": "date_time"
      },
      {
        "field": "zookeeper.server.version_date",
        "format": "date_time"
      }
    ],
    "script_fields": {},
    "stored_fields": [
      "*"
    ],
    "runtime_mappings": {},
    "_source": {
      "excludes": []
    },
    "query": {
      "bool": {
        "must": [],
        "filter": [
          {
            "range": {
              "@timestamp": {
                "format": "strict_date_optional_time",
                "gte": time15MinAgo,
                "lte": time
              }
            }
          }
        ],
        "should": [],
        "must_not": []
      }
    }
  }
  return requestQuery

def elasticRequest():
  query = adjustQuery()
  tempResult = client.search(index="metricbeat*", body=query)
  result = tempResult["aggregations"]["0"]["buckets"]
  firstTime = result[0]["key"]
  dataList = []
  for x in result:
    time = (((x["key"] - firstTime) / 1000 / 15) - 60) / 4
    memoryUsage = x["1"]["values"]["50.0"]
    if (isinstance(memoryUsage, float)):
      memoryUsage = memoryUsage*100
      memoryUsage = round(memoryUsage, 1)
      dataList.append([time, memoryUsage])
  return dataList
