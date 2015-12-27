# In fact, it's noarch package but it depends on 32 bit only sp-auth
# So keep sopcast-player 32 bit only too
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	A GUI front-end to SopCast
Name:		sopcast-player
Version:	0.8.5
Release:	4
License:	GPLv2+
Group:		Video
Url:		http://code.google.com/p/sopcast-player/
Source0:	http://sopcast-player.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	python2-setuptools
BuildRequires:	gettext
BuildRequires:	vlc-devel
Requires:	sp-auth
Requires:	pygtk2
Requires:	python2
Requires:	vlc
ExclusiveArch:	%{ix86}

%description
SopCast Player is designed to be an easy to use Linux GUI front-end for the p2p
streaming technology developed by SopCast. SopCast Player features an 
integrated video player, a channel guide, and bookmarks. Once SopCast Player is
installed it simply "just works" with no required configuration.

%prep
%setup -qn %{name}

%build
export PYTHON=%__python2
%setup_compile_flags
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.svg

