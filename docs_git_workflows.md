# Git for Collaborative Security Workflows

## Objective
Use Git workflows to version detection logic, enable peer review, and support rollback.

## Practical Summary
```bash
git checkout -b dev
git commit -m "Tune brute force rule - reduce false positives"
git push origin dev
```

## Key Practices
- Branching isolates experimentation.
- Pull requests formalize review and testing evidence.
- Commit messages document detection changes.

## Theory
- GitFlow supports SOC teams with parallel detection development.
- CI/CD pipelines can validate rules before deployment.
