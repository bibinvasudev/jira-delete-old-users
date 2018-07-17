FROM dockerregistry:<port>/fedora:25

RUN dnf install -y python2 python2-dnf libselinux-python

RUN pip install -i \
  http://<pypi.com>:<port>/repository/pypi-proxy-registry/simple \
  requests==2.14.2 --trusted-host <pypi>

RUN pip install -i \
  http://<pypi>:<port>/repository/pypi-group-public/simple \
  jira==0.1.0 --trusted-host <pypi>