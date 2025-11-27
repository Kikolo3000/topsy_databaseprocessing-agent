# FTD Analysis System

TOPSY DATABASE. AI-powered systematic analysis of Formal Thought Disorder (FTD) in clinical interview transcripts using the TALD (Thought and Language Disorder) scale.

## Branch Consolidation Workflow

This project uses a custom workflow to harvest generated output files from multiple feature branches and merge them into `main` without performing full Git merges.

### Scripts

**1. `consolidate_outputs.sh`**
* **Purpose:** Iterates through all remote branches.
* **Action:** Extracts only files matching the pattern `**/output*` (preserving their subdirectory location) and commits them to the current branch.
* **Usage:** Run this while on `main` to gather results.

**2. `cleanup_branches.sh`**
* **Purpose:** repository hygiene after consolidation.
* **Action:** Deletes all local and remote branches, leaving only `main`.
* **⚠️ Warning:** This action is destructive and cannot be undone. Ensure `consolidate_outputs.sh` ran successfully before running this.

### How to Run

1.  **Ensure you are on main:**
    ```bash
    git checkout main
    git pull origin main
    ```

2.  **Harvest the files:**
    ```bash
    ./consolidate_outputs.sh
    ```
    *Check your file tree to ensure all "output" files are present.*

3.  **Clean up the repository:**
    ```bash
    ./cleanup_branches.sh
    ```
    *Follow the prompt (type `y`) to confirm deletion of remote branches.*