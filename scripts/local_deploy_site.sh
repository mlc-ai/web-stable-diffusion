#!/bin/bash
set -euxo pipefail

scripts/build_site.sh web/local-config.json

echo "symlink parameter location to site.."

ln -s `pwd`/dist/params site/_site/web-sd-shards-v1-5
ln -s `pwd`/dist/params_xl site/_site/web-sd-shards-xl
cd site && jekyll serve  --skip-initial-build --host localhost --port 8889
