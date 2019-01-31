Name:		telepathy-idle
Version:	0.2.0
Release:	3
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
BuildRequires:	pkgconfig(python2)
BuildRequires:	libxslt-proc
Requires:	telepathy-filesystem
Requires:	telepathy-glib

%description
A Telepathy connection manager implementation for the IRC protocol.

%prep
%autosetup -p1

%build
export PYTHON=%__python2
%configure
%make_build

%install
%make_install

%files
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.idle.service
%{_datadir}/telepathy/managers/idle.manager
%{_libexecdir}/telepathy-idle
%{_mandir}/man8/telepathy-idle.8*
