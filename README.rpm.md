RPM packages
============

Currently RPM packaging is only available for:
- *megaclisas-status*
- *sas2ircu*
- *sas2ircu-status*

To build execute from the top level directory:
```bash
rpmbuild  --define "_sourcedir $PWD" \
  -bb packaging/rpm/megaclisas-status/RPM/SPEC

# sas2ircu has to be downloaded from:
# https://docs.broadcom.com/docs/SAS2IRCU_P20.zip
unzip SAS2IRCU_P20.zip
rpmbuild  --define "_sourcedir $PWD" \
  -bb packaging/rpm/sas2ircu/RPM/SPEC

rpmbuild  --define "_sourcedir $PWD" \
  -bb packaging/rpm/sas2ircu-status/RPM/SPEC
```
