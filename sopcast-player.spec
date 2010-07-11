%define debug_package %{nil}

Summary:	A GUI front-end to SopCast
Name:		sopcast-player
Version:	0.3.3
Release:	%mkrel 1
License:	GPLv2+
Group:		Video
Url:		http://code.google.com/p/sopcast-player/
Source0:	http://sopcast-player.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	python-setuptools
BuildRequires:	gettext
BuildRequires:	vlc-devel
Requires:	vlc
Requires:	python
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
SopCast Player is designed to be an easy to use Linux GUI front-end for the p2p
streaming technology developed by SopCast. SopCast Player features an 
integrated video player, a channel guide, and bookmarks. Once SopCast Player is
installed it simply "just works" with no required configuration.

%prep
%setup -q

%build
sed -i -e 's/libvlc.so/libvlc.so.2/g' lib/vlc.py

%setup_compile_flags
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%post
%{update_menus}
%if %mdkversion >= 200700
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%postun
%{clean_menus}
%if %mdkversion >= 200700
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.svg
