# Force delete (-D) all branches except "main" and "master"
git branch | grep -v "main" | grep -v "master" | xargs git branch -D

#!/bin/bash

# 1. Update remote info
git fetch origin

# 2. Get REMOTE branches ( -r ), remove 'origin/' prefix, and filter out main/master/HEAD
# 'sed' removes the "origin/" part so we get just the name (e.g., "branch_A")
branches=$(git branch -r | grep -v "master" | grep -v "main" | grep -v "HEAD" | sed 's/origin\///g')
#!/bin/bash

# 1. Update list of remotes
git fetch origin --prune

# 2. Get list of REMOTE branches, stripping 'origin/' and excluding main/master/HEAD
branches=$(git branch -r | grep -v "master" | grep -v "main" | grep -v "HEAD" | sed 's/origin\///g')

echo "Branches to be DELETED: $branches"
echo "--------------------------------"
read -p "Are you sure you want to delete these remote branches? (y/n) " -n 1 -r
echo    # move to a new line

if [[ $REPLY =~ ^[Yy]$ ]]; then
    for branch in $branches; do
        # Clean whitespace
        branch=$(echo "$branch" | xargs)
        
        echo "Deleting remote branch: $branch"
        # The standard command to delete a branch on the server
        git push origin --delete "$branch"
    done
    echo "Done! All branches deleted."
else
    echo "Operation cancelled."
fi

git fetch --prune