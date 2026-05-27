#!/bin/bash
# In the grand tapestry of the cosmos, this script is but a single thread,
# weaving the fabric of our SaaS landing page's destiny.

echo "🚀 Commencing the celestial deployment of the SaaS Landing Page"
echo "==============================================================="

# A touch of user interaction, a whisper from the mortal realm.
GITHUB_USER="kevin" # A placeholder for the user's GitHub username
REPO_NAME="saas-landing-page" # A name for our new star in the GitHub galaxy

echo "📦 Deploying to https://$GITHUB_USER.github.io/$REPO_NAME/"

# The birth of a new repository, a universe of its own.
if [ ! -d ".git" ]; then
  git init
  git branch -m main
fi

# With a flourish, we command the GitHub CLI to create our digital home.
echo "🔗 Forging a new repository in the fires of GitHub..."
gh repo create $REPO_NAME --public --source=. --remote=origin --push

# And now, we unfurl our creation for all the world to see.
echo "🛰️ Deploying to the GitHub Pages constellation..."
gh pages deploy --branch=main

echo "✅ The stars have aligned. Deployment is complete."
echo "🌐 Your SaaS Landing Page now resides at: https://$GITHUB_USER.github.io/$REPO_NAME/"
