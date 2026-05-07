
# Helm: The Kubernetes Package Manager

Helm is the essential tool for managing Kubernetes applications. It allows you to manage complexity by using templates instead of static files.

## Why Use Helm?

|**Aspect**|**Without Helm (Manual YAML)**|**With Helm**|
|---|---|---|
|**Effort**|Write separate YAMLs for Deployment, Service, and Ingress.|Create one reusable template for all resources.|
|**Environments**|Manual Copy-Paste for Dev/Stage/Prod.|Use one Chart; change behavior via `values.yaml`.|
|**Management**|Manually update images, replicas, and ports.|Dynamic updates via variables and flags.|
|**Versioning**|Hard to track what changed in a cluster.|Deployments are managed as versioned **Releases**.|

---

## Core Components: The Chart Structure

A Helm "Chart" is a bundle of files that organize your Kubernetes resources.

- **`Chart.yaml`**: The "Identity Card." Contains metadata like the chart name, version, and description.
    
- **`values.yaml`**: The "Default Settings." Contains the default configuration values (e.g., image name, replica count). If a user doesn't provide custom input, Helm defaults to these.
    
- **`templates/`**: The "Engine Room." This directory contains Kubernetes YAML files with placeholders. Helm replaces these placeholders with data from the values files.
    

> **The Logic**: `Templates` + `Values` = **Final Kubernetes Manifest**

---

## Helm Repository Management

Repositories are remote locations where packaged charts are stored and shared.

- `helm repo add <name> <url>`: Registers a remote repository on your local system.
    
- `helm repo update`: Synchronizes your local cache with the remote repository to get the latest chart metadata (`index.yaml`).
    
- `helm search repo <keyword>`: Finds charts matching the keyword within your added repositories.
    

---

## Essential Helm Commands

### Installation & Deployment

- `helm install <release-name> <repo/chart>`: Deploys a chart and creates a **Release** in the cluster.
    
- `helm upgrade <release-name> <repo/chart> --set "key=value"`: Updates an existing release (e.g., changing an image tag).
    

### Observation & History

- `helm list` (or `helm ls`): Lists all deployed releases.
    
    - `--superseded`: Shows older versions of releases.
        
    - `--deployed`: Filters for currently active releases.
        
- `helm status <release-name>`: Displays the current state of a release.
    
    - `--show-resources`: Lists every Kubernetes object (Pods, Services) created by the release.
        
- `helm history <release-name>`: Shows the revision history of the specific release.
    

### Cleanup & Discovery

- `helm uninstall <release-name>`: Removes the release and all associated Kubernetes resources.
    
- `helm search repo <chart-name> --versions`: Lists all available versions of a specific chart in the repository.
    

---

## The Priority Order (Value Precedence)

When Helm builds your YAML, it decides which value to use based on this hierarchy (from highest priority to lowest):

1. **Command Line Flags**: Values defined during runtime using `--set key=value`.
    
2. **Custom Files**: Values provided via a specific file using `-f custom-values.yaml`.
    
3. **Default Values**: The standard `values.yaml` packaged inside the chart.
    

## Upgrades & Version Control

Helm allows you to manage specific versions of your application to ensure consistency across environments.

- **Upgrade with Specific Version**:
    
    `helm upgrade <release-name> <repo/chartname> --version <version-number>`
    
    > **Note**: If you omit the `--version` flag, Helm will automatically upgrade the release to the **latest** version available in the repository.
    

---

## Rollbacks: The Undo Button

One of Helm's most powerful features is the ability to quickly revert to a previous state if a deployment fails.
### 1. View Deployment History

Before rolling back, check the revision history to identify which version you want to return to:

`helm history <release-name>`

- This command lists all revisions, their status, and when they were deployed.
### 2. Perform a Rollback

- **Rollback to Previous Version**:
    
    `helm rollback <release-name>`
    
    > **Note**: This will jump back exactly one revision (e.g., from Revision 5 to Revision 4).
    
- **Rollback to a Specific Revision**:
    
    `helm rollback <release-name> <revision-number>`
    
    > **Example**: `helm rollback my-app 2` will force the application back to the exact state it was in during Revision 2.
    
---
## Uninstalling & Cleanup

When removing an application, you have two choices depending on whether you want to leave a trail behind.

### . Standard Uninstall

`helm uninstall <release-name>`

- **Result**: Removes all Kubernetes resources (Pods, Services, etc.) and wipes the release history.
    
- **Warning**: Once this is done, the release data is gone. You cannot rollback.
    
### . Uninstall with History Retention

`helm uninstall <release-name> --keep-history`

- **Result**: Removes all associated resources and marks the release as `uninstalled` (deleted), but **retains the revision history**.
    
- **Why use this?**: It allows you to **rollback to a deleted release**. If you accidentally uninstall the wrong app, you can bring it back to its exact previous state using `helm rollback <release-name> <revision>`.
---
## Advanced Automation & Safety Flags

When implementing DevOps pipelines (e.g., Jenkins, GitHub Actions, or GitLab CI), these flags ensure your deployments are resilient and conflict-free.

### 1. Handling Release Names in Pipelines

`helm install <repo/chartname> --generate-name`

- **The Problem**: Pipelines often fail if you try to install a release with a name that already exists (`Error: cannot re-use a name that is still in use`).
    
- **The Solution**: This flag automatically creates a unique name for the release. This is ideal for dynamic "Preview Environments" or "Ephemeral Clusters" where the specific name matters less than avoiding duplicate errors.
    
### 2. The "Atomic" Safety Net

`helm install <release-name> <repo/chartname> --atomic`

- **Behavior**: If the installation fails (e.g., a Pod stays in `ImagePullBackOff`), Helm will automatically **delete the release** and clean up all resources.
    
- **Included Logic**:
    
    - **Implicit `--wait`**: Setting `--atomic` automatically enables the `--wait` flag.
        
    - **Ready State**: Helm will not mark the release as "Successful" until every Kubernetes resource is in a **Ready** state.
        
### 3. Timeouts & Waiting

`--wait` (enabled by default with `--atomic`)

- Helm monitors the deployment and waits for resources (Pods, Services, etc.) to be fully operational before exiting.
    
- **`--timeout <duration>`**: Defines how long Helm should wait for Kubernetes operations.
    
    - **Default**: `5m0s` (5 minutes).
        
    - If the resources aren't ready within this window, the operation fails (and triggers the rollback/deletion if `--atomic` is used).
 

 Namespaces, Overrides, Debugging
---
## 🔹 Namespace Handling

```bash
helm install <release-name> <chart> \
  --namespace <namespace> \
  --create-namespace
```

- Default namespace = `default`
    
- `--create-namespace` → creates namespace if not exists
    
- Best practice:
    
    - ❌ Avoid `default`
        
    - ✅ Use `dev / staging / prod`
        

---
## 🔹 Override Values

```bash
helm install <release> <chart> --set key=value
```

Example:

```bash
helm install myapp repo/chart --set service.nodePort=31240
```

- Overrides `values.yaml`
    
- Useful for quick changes (not for large configs)
    
---

## 🔹 Dry Run (Simulation Mode)

```bash
helm install <release> <chart> --dry-run
helm upgrade <release> <chart> --dry-run
helm uninstall <release> --dry-run
helm template <release> <chart>
```

- Does NOT create resources
    
- Shows what Helm will generate
    
- `helm template` → outputs YAML manifests

---

## 🔹 Debug Mode

```bash
helm install <release> <chart> --debug
```

- Shows detailed logs
    
- Helps in troubleshooting
    
---
## 🔹 Dry Run + Debug (Best Combo)

```bash
helm install <release> <chart> --dry-run --debug
```

- See full rendered manifests + logs
    
---
## 🔹 Helm Get Commands (Inspect Release)

```bash
helm get values <release>
helm get manifest <release>
helm get notes <release>
helm get all <release>
helm get hooks <release>
```

- `values` → current values used
    
- `manifest` → generated Kubernetes YAML
    
- `notes` → post-install instructions
    
- `all` → everything
    
- `hooks` → lifecycle hooks (pre/post install etc.)
    

---
## 🔹 Values Hierarchy (VERY IMPORTANT 🔥)

Priority (low → high):

1. Chart `values.yaml`
    
2. Parent chart `values.yaml`
    
3. User file → `-f values.yaml`
    
4. CLI → `--set`
    

👉 Highest wins = `--set`

---
## 🔹 Deleting Default Values (Null Override)

```bash
helm install <release> <chart> \
  --set service.nodePort=null
```

- Removes the key from final config
    
- Kubernetes may assign default value automatically

⚠️ Important:

- Not always “assign port automatically”
    
- Depends on resource type (e.g., Service behavior)
        
---

Helm Chart Folder Structure Notes

---

# 🔹 Create Helm Chart
```bash
helm create <chart-folder-name>
```
Example:

```bash
helm create myapp
```
This generates the default Helm chart structure.

---
# 📂 Helm Chart Structure

```text
myapp/
├── .helmignore
├── Chart.yaml
├── values.yaml
├── charts/
└── templates/
    ├── deployment.yaml
    ├── service.yaml
    ├── serviceaccount.yaml
    ├── ingress.yaml
    ├── hpa.yaml
    ├── httproute.yaml
    ├── NOTES.txt
    ├── _helpers.tpl
    └── tests/
        └── test-connection.yaml
```

---
# 🔹 .helmignore

Similar to `.gitignore`

Used to ignore files when packaging charts.

Example:

```text
.git/
README.md
```

---
# 🔹 Chart.yaml

Contains chart metadata.

Example fields:

```yaml
apiVersion: v2
name: myapp
description: Helm chart for Kubernetes
type: application
version: 0.1.0
appVersion: "1.0"
```

### Important Fields

| Field         | Meaning                          |
| ------------- | -------------------------------- |
| `apiVersion`  | Helm chart API version           |
| `name`        | Chart name                       |
| `description` | Information about chart          |
| `type`        | `application` or `library`       |
| `version`     | Helm chart version               |
| `appVersion`  | Application/Docker image version |

---
# 🔹 application vs library

## application

- Deployable chart
- Creates Kubernetes resources
Example:

- nginx app
- springboot app
## library

- Reusable helper chart
- Cannot be deployed directly
- Used for shared templates/functions

---
# 🔹 values.yaml

Contains default configuration values.

Example:

```yaml
replicaCount: 2

image:
  repository: nginx
  tag: latest

service:
  type: ClusterIP
  port: 80
```

Used to customize deployment without editing templates.

Override using:

```bash
--set
-f values.yaml
```

---
# 🔹 charts/ Folder

Contains dependent/sub charts.

Example:

```text
Parent Chart → UMS Application
Sub Chart → MySQL Chart
```

Used for:

- databases
- redis
- rabbitmq
- shared services
---
# 🔹 templates/ Folder

Contains Kubernetes manifest templates.

Helm processes these files using:

- GO templating engine
- values from `values.yaml`

Generates final Kubernetes YAML manifests.

Common files:
- deployment.yaml
- service.yaml
- ingress.yaml
- hpa.yaml

---
# 🔹 Existing Kubernetes YAML → Helm

If Kubernetes manifests already exist:

1. Move YAML files into `templates/`
2. Replace hardcoded values with Helm variables
Example:
Before:

```yaml
replicas: 2
```

After:

```yaml
replicas: {{ .Values.replicaCount }}
```

Then deploy using:

```bash
helm install
```

---
# 🔹 templates/_helpers.tpl

Used for reusable template helpers.

Files beginning with `_`  
DO NOT generate Kubernetes manifests.

Used for:

- reusable labels
- naming conventions
- selectors
- common template logic
Example:

```yaml
{{- define "myapp.labels" -}}
app: nginx
env: prod
{{- end }}
```

Use helper:

```yaml
{{ include "myapp.labels" . }}
```

---
# 🔹 NOTES.txt
Displayed after successful install.
Usually contains:
- access URLs
- kubectl commands
- login instructions

---
# 🔹 tests/ Folder

Contains Helm test manifests.

Example:

```text
test-connection.yaml
```

Run tests:

```bash
helm test <release-name>
```

Used to verify:

- app connectivity
- service availability
- deployment success
---
# 🧠 Important Real-World Understanding

## Helm Flow

```text
values.yaml
      ↓
templates/*.yaml
      ↓
GO template rendering
      ↓
Final Kubernetes manifests
      ↓
kubectl applies resources
```

---
# 🔥 Most Important Files in Real Projects

|File|Importance|
|---|---|
|Chart.yaml|Chart metadata|
|values.yaml|Environment configs|
|templates/deployment.yaml|Main workload|
|templates/service.yaml|Networking|
|_helpers.tpl|Reusable logic|

---
## NOTES
- Why do we need templates/NOTES.txt?
	- This is an optional file which provide important information about our helm chart.
		- EX:How to access the application deployed using this Helm chart
- How does template/NOTES.txt work?
	- Notes.txt file is rendered same as regular template file by HELM.
	- The main difference is after NOTES.txt rendered its not sent to Kubernetes cluster but the output is displayed in the command line.
	- As it behaves same as regular Helm Templates we can fetch values from the values.yaml file we can fetch values from the built-in objects. Chart.Release, add if condition blocks use flow control function pipelines and so on.
- tests folder
	- We write tests that validate our chart works as expected when it is installed.
	- These tests also help chart consumer understand what this helm chart is supposed to do.
- README.md
	- We will document on how to use this HELM chart in this file.
- LICENSE
	- LICENSE file about usage of helm chart.