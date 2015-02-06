Name:		telepathy-idle
Version:	0.1.14
Release:	2
Summary:	A Telepathy connection manager implementation for the IRC protocol

Group:		Networking/Instant messaging
License:	LGPLv2
URL:		http://telepathy.freedesktop.org/wiki/
Source0:	http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	glib2-devel
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(openssl)

BuildRequires:	pkgconfig(telepathy-glib)
BuildRequires:	pkgconfig(libxslt) libxslt-proc
BuildRequires:	python-pyxml
Requires:	telepathy-filesystem
Requires:	telepathy-glib

%description
A Telepathy connection manager implementation for the IRC protocol.

%prep
%setup -q

%build
autoreconf -fi
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.idle.service
%{_datadir}/telepathy/managers/idle.manager
%{_libdir}/telepathy-idle
%{_mandir}/man8/telepathy-idle.8*
