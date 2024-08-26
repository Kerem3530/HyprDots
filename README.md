# HyprDots-Gruvbox

## Introductions

### Arch Linux ONLY

**Install `yay` and dependencies:**

```
sudo pacman -S base-devel
sudo pacman -S git
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si

yay -S brightnessctl mako btop neofetch fish gsimplecal wl-clipboard hyprpicker grimblast pavucontrol kitty xsensors nemo hyprpaper waybar qt5ct qt6ct playerctl ttf-code2000 hyprland playerctl wofi-calc wofi-wifi-menu gwenview cmatrix nyancat cowsay nwg-look kvantum-qt5 pamixer nodejs npm unimatrix sl gruvbox-dark-icons-gtk electron idle


```

### Installation
```
git clone https://github.com/Kerem3530/HyprDots-Gruvbox.git
cd HyprDots-Gruvbox/HyprDots/home/config
chmod -R +x ~/scripts
```

**And Copy The Files and Directories To .config Directory**

### Other Things
```
chsh -s /usr/bin/fish
chmod -R +x ~/scripts
```
**This will make fish the default shell app**

**Change your keyboard layout from Turkish to any keyboard layout you want**

```
cd .config/hypr
nano hyprland.conf
```

**Find the input section on the config file**
**And change the 'kb_layout' = tr line**
**You can also change your programs in the 'My Programs' section and keybindings**

# The config folder and icons folder is hidden !!!
