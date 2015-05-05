Name:		telepathy-idle
Version:	0.2.0
Release:	1
Summary:	A Telepathy connection manager implementation for the IRC protocol

Group:		Networking/Instant messaging
License:	LGPLv2
URL:		http://telepathy.freedesktop.org/wiki/
Source0:	http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(telepathy-glib)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	libxslt-proc
Requires:	telepathy-filesystem
Requires:	telepathy-glib

%description
A Telepathy connection manager implementation for the IRC protocol.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%files
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.idle.service
%{_datadir}/telepathy/managers/idle.manager
%{_libdir}/telepathy-idle
%{_mandir}/man8/telepathy-idle.8*
