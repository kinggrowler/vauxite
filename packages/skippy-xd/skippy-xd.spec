Name:           skippy-xd
Version:        2025.2.0
Release:        1%{?dist}
Summary:        A window selector for X11 with Exposé and live preview Alt-Tab effects and more

URL:            https://github.com/felixfung/skippy-xd
Source:         https://github.com/felixfung/skippy-xd/archive/c167f2af9d25164b5fc7e67b5ecf174b56e07d01.zip
License:        GPL-2.0

#Patch0:         buffer-overrun.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libXft-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXext-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  giflib-devel

%description
Skippy-xd is a lightweight, window-manager-agnostic window selector on X server. With skippy, you get live-preview on your alt-tab motions; you get the much coveted expose feature from Mac; you get a handy overview of all your virtual desktops in one glance with paging mode.

%prep
%autosetup -n %{name}-c167f2af9d25164b5fc7e67b5ecf174b56e07d01 -p1

%build
make

%install
make DESTDIR=%{buildroot} install

%files
%{_bindir}/skippy-xd
%{_sysconfdir}/xdg/skippy-xd.rc

%changelog
%autochangelog
