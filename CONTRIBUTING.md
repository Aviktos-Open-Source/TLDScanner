# Contributing to DomainScope
Thank you for considering contributing! Here's how you can help:

1. Fork the repository.
2. Create a branch for your changes: `git checkout -b feature-name`.
3. Make your changes and write tests.
4. Submit a pull request.

# Require signed commits

For security reasons, commits pushed to matching refs must have verified signatures.

## Sign Your Commits:

To Commit your changes with a gpg key. Follow the next steps:

### Install gnupg

For Debian-based systems:
```bash
sudo apt-get update
sudo apt-get install -y gnupg
```

For macOS:
```bash
brew install gnupg
```

For Red Hat-based systems
```bash
sudo dnf install gnupg
```

### Generate a GPG key:
Once gnupg is installed, you can generate a GPG key with the following command:

Suggestion: leave options as default
```bash
gpg --full-generate-key
```
Follow the prompts to create your GPG key. Once done, list your GPG keys:
```bash
gpg --list-secret-keys --keyid-format LONG
```
Example output:
```
[keyboxd]
---------
sec   ab12345/DFO34895SDFSD 2000-01-01 [SC] [expires: 2000-02-01]
      AAAAAAAAAAAA1234567890987654321BBBBBBBB
uid                 ... <example@gmail.com>
ssb   cd09876/DS3FDSFG23423 2000-01-01 [E] [expires: 2000-02-01]
```

### Add your GPG key to GitHub:
First, export your public key:
```bash
gpg --armor --export AAAAAAAAAAAA1234567890987654321BBBBBBBB
```
Then, copy the output and go to your GitHub account settings:
- Navigate to Settings > SSH and GPG keys > New GPG key.
- Paste the GPG key into the box and save.

### Configure Git to use your GPG key:
```bash
git config --global user.signingkey AAAAAAAAAAAA1234567890987654321BBBBBBBB
git config --global commit.gpgSign true
```

## Amend the Commit with a Signed Commit:
Once you have your GPG key configured and added to GitHub, you can amend your commit with a signed version:
```bash
git commit -m "Commit message"
git commit --amend --no-edit --gpg-sign=AAAAAAAAAAAA1234567890987654321BBBBBBBB
```

Then push your changes:
```bash
git push origin <YOUR BRANCH>
```