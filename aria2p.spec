Summary:	Command-line tool and library to interact with an aria2c daemon process with JSON-RPC. 
Name:		aria2p
Version:	0.12.0
Release:	1
License:	ISC
Group:		Development/Python
Url:		https://github.com/pawamoy/aria2p
Source0:	https://github.com/pawamoy/aria2p/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python-setuptools
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pip)
%rename python-aria2p

%description
To avoid confusion:

- aria2 is a lightweight multi-protocol & multi-source, cross platform download utility operated in command-line. 
It supports HTTP/HTTPS, FTP, SFTP, BitTorrent and Metalink.
- aria2c is the name of the command-line executable provided by aria2. It can act as a daemon.
- aria2p (p for Python) is a command-line client that can interact with an aria2c daemon. It is not an official client. 
There are other Python packages allowing you to interact with an aria2c daemon. 
These other packages do not offer enough usability (in my opinion), this is why I'm developing aria2p.

Purpose: aria2c can run in the foreground, for one-time downloads, or in the background, as a daemon. This is where aria2p intervenes: 
when an instance of aria2c is running in the background, aria2p will be able to communicate with it to add downloads to the queue, remove, 
pause or resume them, etc.

In order for aria2p to be able to communicate with the aria2c process, RPC mode must be enabled with the --enable-rpc option of aria2c. 
RPC stands for Remote Procedure Call. Although aria2c supports both JSON-RPC and XML-RPC protocols, aria2p works with JSON only (not XML). 
More information about how to configure aria2c to run as a daemon with RPC mode enabled can be found in the Configuration section of the documentation.

%autosetup -p1 -n %{name}-%{version}

%build
%py_build
#python -m build --wheel --no-isolation

%install
%py_install

%files
