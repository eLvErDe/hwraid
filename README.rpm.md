RPM packages
============

Currently RPM packaging is only available for *megaclisas-status*.

To build execute from the top level directory:
```
rpmbuild  --define "_sourcedir $PWD" \
  -bb packaging/rpm/megaclisas-status/RPM/SPEC
```
