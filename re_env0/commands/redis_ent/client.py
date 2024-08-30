import backoff
import enum
from backoff import on_predicate
import requests

from ...console import console


class CertificateType(str, enum.Enum):
    proxy = "proxy"
    api = "api"
    cm = "cm"
    ldap_client = "ldap_client"
    metrics_exporter = "metrics_exporter"
    syncer = "syncer"


class RedisEnterpriseClient:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password

    def create_bdb(self, bdb_config):
        url = f"{self.base_url}/v1/bdbs"
        response = requests.post(
            url, auth=(self.username, self.password), json=bdb_config, verify=False
        )
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        return response.json()

    def get_bdb(self, bdb_id):
        url = f"{self.base_url}/v1/bdbs/{bdb_id}"
        response = requests.get(url, auth=(self.username, self.password), verify=False)
        response.raise_for_status()
        return response.json()

    @on_predicate(
        backoff.constant,
        lambda b: b["status"] != "active",
        max_time=100,
        interval=10,
        jitter=None,
    )
    def wait_for_bdb(self, bdb_id):
        bdb = self.get_bdb(bdb_id)
        console.log(f"BDB {bdb_id} status: {bdb['status']}")
        return bdb

    def create_crdb(self, crdb_config, clusters):
        url = f"{self.base_url}/v1/crdbs"
        body = {
            "default_db_config": crdb_config,
            "instances": [{"cluster": c, "compression": 6} for c in clusters],
            "name": crdb_config["name"],
        }
        response = requests.post(
            url, auth=(self.username, self.password), json=body, verify=False
        )
        response.raise_for_status()
        return response.json()

    def get_crdb(self, crdb_id):
        url = f"{self.base_url}/v1/crdbs/{crdb_id}"
        response = requests.get(url, auth=(self.username, self.password), verify=False)
        response.raise_for_status()
        return response.json()

    def get_crdb_task(self, task_id):
        url = f"{self.base_url}/v1/crdb_tasks/{task_id}"
        response = requests.get(url, auth=(self.username, self.password), verify=False)
        response.raise_for_status()
        return response.json()

    @on_predicate(
        backoff.constant,
        lambda b: b["status"] != "finished",
        max_time=100,
        interval=10,
        jitter=None,
    )
    def wait_for_crdb_task(self, task_id):
        crdb_task = self.get_crdb_task(task_id)
        console.log(f"CRDB task {task_id} status: {crdb_task['status']}")
        return crdb_task

    def create_role(self, role_config):
        url = f"{self.base_url}/v1/roles"
        response = requests.post(
            url, auth=(self.username, self.password), json=role_config, verify=False
        )
        response.raise_for_status()
        return response.json()

    def get_roles(self):
        url = f"{self.base_url}/v1/roles"
        response = requests.get(url, auth=(self.username, self.password), verify=False)
        response.raise_for_status()
        return response.json()

    def create_user(self, user_config):
        url = f"{self.base_url}/v1/users"
        response = requests.post(
            url, auth=(self.username, self.password), json=user_config, verify=False
        )
        response.raise_for_status()
        return response.json()

    def create_acl(self, acl_config):
        url = f"{self.base_url}/v1/redis_acls"
        response = requests.post(
            url, auth=(self.username, self.password), json=acl_config, verify=False
        )
        response.raise_for_status()
        return response.json()

    def get_acls(self):
        url = f"{self.base_url}/v1/redis_acls"
        response = requests.get(url, auth=(self.username, self.password), verify=False)
        response.raise_for_status()
        return response.json()

    def update_tls_certificate(
        self,
        cert_type: CertificateType,
        cert_data: str,
        cert_pkey_data: str | None = None,
    ):
        url = f"{self.base_url}/v1/cluster/update_cert"
        payload = {
            "name": cert_type.value,
            "certificate": cert_data,
        }

        if cert_pkey_data:
            payload["key"] = cert_pkey_data

        response = requests.put(
            url,
            auth=(self.username, self.password),
            json=payload,
            verify=False,
        )
        response.raise_for_status()
        return response.json() if response.text else None
