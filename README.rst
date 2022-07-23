========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |github-actions| |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/freesurfer_analyses/badge/?style=flat
    :target: https://freesurfer_analyses.readthedocs.io/
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.com/niparser/freesurfer_analyses.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com/github/niparser/freesurfer_analyses

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/niparser/freesurfer_analyses?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/niparser/freesurfer_analyses

.. |github-actions| image:: https://github.com/niparser/freesurfer_analyses/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/niparser/freesurfer_analyses/actions

.. |requires| image:: https://requires.io/github/niparser/freesurfer_analyses/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/niparser/freesurfer_analyses/requirements/?branch=master

.. |codecov| image:: https://codecov.io/gh/niparser/freesurfer_analyses/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/niparser/freesurfer_analyses

.. |commits-since| image:: https://img.shields.io/github/commits-since/niparser/freesurfer_analyses/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/niparser/freesurfer_analyses/compare/v0.0.0...master



.. end-badges

A package to process data derived from qsiprep pipeline

* Free software: Apache Software License 2.0

Installation
============

::

    pip install freesurfer_analyses

You can also install the in-development version with::

    pip install https://github.com/niparser/freesurfer_analyses/archive/master.zip


Documentation
=============


https://freesurfer_analyses.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
