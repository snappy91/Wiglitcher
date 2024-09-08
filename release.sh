flet publish --app-name Wiglitcher --web-renderer html main.py
cd dist
git init . -b gh-pages
git add -A
git remote add origin git@github.com:we-art-o-nauts/Wiglitcher.git
git ca "IR"
git push origin gh-pages
