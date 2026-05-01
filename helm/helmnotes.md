
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
    

