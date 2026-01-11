Title: My Blog Is Back
Date: 2026-01-10
Category: Blog
Tags: announcement
Slug: my-blog-is-back

## Why I'm Back

A few years ago, I had a blog but I was not actively writing, so I deleted my old blog and canceled my DigitalOcean account. Since I was not writing much, it felt like it was just sitting there collecting dust and costing money. But lately, I've been thinking about starting again. I want to share what I've learned, what I'm learning, and have a place to put my opinions on tech, open source, and everything in between.

I have been thinking about this for a while, and I'm finally ready to start writing again. But I did not want to pay for a VPS just to host a blog. So I decided to try something new. I'm really familiar with Markdown due to my heavy usage of GitHub, Obsidian, and Sphinx. So I decided to use a static site generator and host it on my profile GitHub Page.

I hope to post at least one article a week. Some articles will be shorter than others, but I hope it will be interesting.

## The Old Setup

My old blog was hosted on a DigitalOcean VPS with FreeBSD with the domain ericbsd.com. I do not recall if it was Drupal or WordPress. It worked, but maintaining a VPS for a simple blog felt like overkill, especially when I wasn't actively writing.

## The New Setup: GitHub Pages + Pelican

This time around, I decided to go with a static site generator. GitHub allows you to host static websites for free through [GitHub Pages](https://pages.github.com/). With my experience with Sphinx, I was looking for something like that, so I could write with Markdown.

Nowadays, I do my technical research with ChatGPT, Claude, or sometimes Grok. I get better results than traditional Google, though with Gemini integration Google has improved. I asked ChatGPT what Python framework I could use to do a blog on a GitHub Page, and [Pelican](https://getpelican.com/) came up in the list. ChatGPT did list it as a Blog Generator that can also build a website. The name Pelican sounded cool, so I gave it a try.

## Why Pelican?

Pelican felt natural to me because I'm already used to writing in Markdown and familiar with reStructuredText. I write notes with [**Obsidian**](https://obsidian.md/) and use [**Sphinx**](https://www.sphinx-doc.org/) for GhostBSD documentation, so Markdown is second nature. Pelican is written in Python (which I love), and it's simple enough to get started quickly.

How it works? Simple. You install Pelican with Markdown support and the Markdown package.

```shell
python -m pip install "pelican[markdown]" markdown
```
In the repository directory, you will have to run `pelican-quickstart`. This will create the skeleton project inside it. It will also ask you for some information like below:

```text
> Where do you want to create your new web site? [.] 
> What will be the title of this web site? EricBSD 
> Who will be the author of this web site? Eric Turgeon 
> What will be the default language of this web site? [en] 
> Do you want to specify a URL prefix? e.g., https://example.com (Y/n) y 
> What is your URL prefix? (see above example; no trailing slash) https://ericbsd.com 
> Do you want to enable article pagination? (Y/n) Yes 
> How many articles per page do you want? [10] 
> What is your time zone? [Europe/Rome] America/Moncton 
> Do you want to generate a tasks.py/Makefile to automate generation and publishing? (Y/n) y 
> Do you want to upload your website using FTP? (y/N) n 
> Do you want to upload your website using SSH? (y/N) n 
> Do you want to upload your website using Dropbox? (y/N) n 
> Do you want to upload your website using S3? (y/N) n 
> Do you want to upload your website using Rackspace Cloud Files? (y/N) n 
> Do you want to upload your website using GitHub Pages? (y/N) y 
> Is this your personal page (username.github.io)? (y/N) y Done. 
Your new project is available at ~/PycharmProjects/ericbsd
```
You can change most of the settings later in the `pelicanconf.py` and `publishconf.py` files.

From there you can create blog articles in the `content` directory and add pages in the content/pages directory. Pages should be added automatically to your navigation menu. If you have a theme like me that has multiple menus, you might have some tweaks to do in the `pelicanconf.py` file.

If you set up the Makefile like I did, you can use 'gmake html' (use 'make' on Linux) to generate the static site. Use 'gmake devserver' to run a local server that will update the site every time you save a file. Depending on your workflow, you might have to refresh the browser to see the changes.

## What's Next

I intend to post at least weekly, so I can improve my writing. As I am writing this, I have not set up anything on GitHub Pages yet, so that will most likely be the next article. This blog will be about whatever I feel like writing related to BSD, Linux, NAS, open source, programming, automation, and the occasional rant about tech industry trends. This blog's UX might change and improve over time. For now, it's functional, and I'm ready to start writing again.