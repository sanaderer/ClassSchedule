# Contributing to ClassSchedule

>All types of contributions are encouraged and valued. Please make sure to read the relevant section before making your contribution. As it will make it a lot easier for the maintainers and improve the experience for all involved. The community looks forward to your contributions. 🎉
---
## Opening an Issue

Here's a few tips to keep in mind when creating an issue:
- Make sure to write a meaningful title that gives an idea of what your issue refers to.
- Make sure to provide a detailed description of the issue.
- Attach necessary attachments (screenshots, links, etc..) if possible.
---
## Creating a Pull Request (PR)

1. Fork this repository (Click the Fork button in the top right of this page --> click your Profile Image)
2. Clone your fork down to your local machine.

```bash
git clone https://github.com/your-username/hacktoberfest.git
```

**NOTE**: If tou already have a fork in your profile you may see that your fork is behind the original repository, just click the sync button and pull the changes to your local machine.

```bash
git pull
```

3. Create a branch for your work.

```bash
git checkout -b branch-name
```

4. Make your changes on the created branch.
5. Commit then push.

```bash
git add .
git commit -m 'Commit message'
git push origin branch-name
```

6. Create a new pull request from your forked repository (Click the `New Pull Request` button located at the top of your repo)
7. Wait for your PR review and merge approval!
---
## Commit Message Style Guide

### Format
```markdown
{type}({scope}): {subject}
<BLANK LINE>
{body}
<BLANK LINE>
{footer}
```

### Allowed Types - {type}
-   feat -> feature
-   fix -> bug fix
-   docs -> documentation
-   style -> formatting, lint stuff
-   refactor -> code restructure without changing behavior
-   test -> adding missing tests
-   chore -> maintenance
-   rearrange -> files moved, added, deleted etc..
-   update -> update code (versions, library compatibility)

### Subject - {subject}
Summary of the changes made.
	-   First letter is not capitalized
	-   Does not end with a '.'

### Scope - {scope}
Where the change was (i.e. the file, the component, the package).

### Message Body - {body}
This gives details about the commit, including:
	-   explanation for the change (broken code, new feature, etc)
	-  what is different now, additional things now needed, etc

### Footer - {footer}
Reference issues it fixes, Jira tasks, etc.
	- closes #14
	- closes #14, #15

----
## Example
```
feat(controller): add router component

This introduces a new router component to Deis, which proxies requests to Deis
components.

closes #123
```
---
