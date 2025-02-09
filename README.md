# DevOps Infrastructure Repository (devops-infra)

## Overview
The **counter-service** repository is the core infrastructure repository for building the application container and pushing it to EKS. It contains the app Code,Dockerfile and automation appending the new commit hash the the image tag. The repository also includes CI/CD pipelines for seamless deployment and integration with GitHub Actions.

## Features
- **CI/CD Pipelines**: Implements GitHub Actions to validate, deploy, and destroy infrastructure.
- **Automated image tag update**: Includes GitHub Actions automation for image tag update in devops-infra repository.

## Deployment Workflow
1. **Deploy Application**:
   - GitHub Actions builds the application Docker image.
   - The image is pushed to Amazon ECR.
   - ArgoCD automatically syncs Kubernetes manifests and deploys the latest image.

## Prerequisites
To use this repository, ensure you have:
- AWS credentials with required permissions.
- Docker installed.
- YAML query installed.
- GitHub Actions secrets configured for OIDC authentication.

## Contributions
Feel free to submit pull requests and issues for improvements. Make sure to follow the branch naming conventions and create merge requests when modifying infrastructure components.