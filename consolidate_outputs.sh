#!/bin/bash

# 1. Update remote info
git fetch origin

# 2. Get REMOTE branches ( -r ), remove 'origin/' prefix, and filter out main/master/HEAD
# 'sed' removes the "origin/" part so we get just the name (e.g., "branch_A")
branches=$(git branch -r | grep -v "master" | grep -v "main" | grep -v "HEAD" | sed 's/origin\///g')

echo "Branches to process: $branches"

for branch in $branches; do
    # Trim whitespace just in case
    branch=$(echo "$branch" | xargs)
    
    echo "Processing $branch..."

    # Now we construct the path: origin/branch_A
    if git checkout "origin/$branch" -- "**/output*"; then
        
        # Check if anything was actually staged (avoid empty commits)
        if git diff --cached --quiet; then
            echo "  -> No 'output' files found in $branch. Skipping commit."
        else
            echo "  -> Files retrieved. Committing..."
            git add .
            git commit -m "Retrieved output files from $branch"
        fi
        
    else
        echo "  -> Error: Could not find branch 'origin/$branch'"
    fi
done