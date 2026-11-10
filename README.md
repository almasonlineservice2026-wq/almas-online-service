# ALMAS ONLINE SERVICE

A static, responsive website ready for GitHub Pages.

## Deploy

1. Create a GitHub repository and upload the contents of this project (keep the `.github` folder).
2. Set the default branch to `main`.
3. Open **Settings → Pages** and choose **GitHub Actions** as the build and deployment source.
4. Push to `main`. The workflow builds the asset manifest and deploys the site.

## Add images without editing code

Upload image files directly into `assets/` and push them to GitHub. Give files descriptive names, for example:

- `tiktok-account.jpg`
- `facebook-account.png`
- `youtube-channel.webp`
- `chatgpt-subscription.png`
- `pubg-account.jpg`

The deployment workflow scans the folder and creates `assets/manifest.json`; the page matches filenames to product names automatically. You do not need to edit image URLs in HTML.

## Important hosting note

GitHub Pages is static hosting. Image files committed to this repository are published for every visitor. A browser-only upload cannot permanently publish files to GitHub; to publish new images, add them to `assets/` and commit/push them. The website itself requires no server or database.

All internal links and asset URLs are relative, so the site works both at a repository URL (`username.github.io/repository/`) and a custom domain.