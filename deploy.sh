#! /usr/bin/env bash
git add -f .secrets/
eb deploy --profile eb-seoulcontest --staged
git reset HEAD .secrets/