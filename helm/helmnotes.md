# 📦 HELM REPO, SEARCH, INSTALL & RELEASE COMMANDS — NOTES
  # 🔹 List Helm Repositories
    helm repo list
### ✅ Meaning:
    * Displays all Helm repositories configured locally
### 📌 Use:
    * Verify repo is added before installing charts
# 🔹 Add Helm Repository
    helm repo add <DESIRED-NAME> <HELM-REPO-URL>
### ✅ Example:
    helm repo add mybitnami https://charts.bitnami.com/bitnami
### 📌 Meaning:
    * Registers a remote chart repository with a local name
### ⚠️ Note:
    * Only adds reference (does NOT download charts)
# 🔹 Update Helm Repositories
    helm repo update
### ✅ Meaning:
    * Fetches the latest chart metadata from all added repos
### 📌 Use:
    * Always run before search/install to avoid outdated charts
# 🔹 Search Helm Repository
    helm search repo <KEY-WORD>
### ✅ Examples:
    helm search repo nginx
    helm search repo apache
    helm search repo wildfly
### 📌 Meaning:
    * Searches charts available in added repositories
### 🔍 Output Includes:
    * Chart name (`repo/chart`)
    * Chart version
    * App version
    * Description
# 🔹 Install Helm Chart
    helm install <RELEASE-NAME> <repo_name/chart_name>
### ✅ Example:
    helm install mynginx mybitnami/nginx
### 📌 Meaning:
    * Deploys a chart into Kubernetes as a **release**
### 🔑 Key Points:
    * `<RELEASE-NAME>` = unique identifier of deployment
    * `<repo/chart>` = chart source
# 🔹 List Helm Releases
    helm list
    helm ls
### ✅ Meaning:
    * Shows all deployed Helm releases
## 🔍 Output Formats
### YAML:
    helm list --output=yaml
### JSON:
    helm list --output=json
### 📌 Use:
    * YAML/JSON → automation, scripting, CI/CD
## 🔍 Namespace Specific
    helm list -n default
### 📌 Meaning:
    * Lists releases only in specified namespace
# 🔹 Uninstall Helm Release
    helm uninstall <RELEASE-NAME>
### ✅ Example:
    helm uninstall mynginx
### 📌 Meaning:
    * Deletes the deployed release and its Kubernetes resources

# 🔁 End-to-End Flow
    helm repo add mybitnami https://charts.bitnami.com/bitnami
    helm repo update
    helm search repo nginx
    helm install mynginx mybitnami/nginx
    helm ls
    helm uninstall mynginx

# ⚠️ Important Notes

* Repo must be added before install
* Always run `helm repo update` before search/install
* Release name must be unique in a namespace
* Use correct `repo/chart` format while installing

## Helm Upgrade with --set option
    helm search repo mychart2 --versions - to see the versions of the chart