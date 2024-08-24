# HyprDots-Gruvbox

## Introductions

### Arch Linux ONLY

**Install `yay` and dependencies:**

```bash
sudo pacman -S base-devel
sudo pacman -S git
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si

yay -S brightnessctl mako btop neofetch
