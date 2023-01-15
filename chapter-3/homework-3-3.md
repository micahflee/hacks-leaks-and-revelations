# Homework 3-3 for Windows and Linux Users: Manage Packages with Apt

Different Linux distributions come with different [package managers](https://en.wikipedia.org/wiki/Package_manager). Assuming you're using Ubuntu or Windows with WSL, you'll use `apt` to install neofetch.

Update available packages:

```sh
sudo apt update
```

Install [neofetch](https://github.com/dylanaraps/neofetch):

```sh
sudo apt install neofetch
```

And then run it:

```sh
neofetch
```

Uninstall it:

```sh
sudo apt remove neofetch
```

Update all packages:

```sh
sudo apt update
sudo apt upgrade
```
