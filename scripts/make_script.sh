#!/bin/bash

NOTEBOOKS_PATH=../notebooks
FILE=master
NOTEBOOK=${NOTEBOOKS_PATH}/${FILE}
PY_SCRIPT=${NOTEBOOKS_PATH}/${FILE}.py
TMP_FILE=tmp_file

jupyter nbconvert --to script "${NOTEBOOK}"

sed -e 's/^#.*$//g' "${PY_SCRIPT}" | \
  cat -s | \
  sed -e '1,3d;$d' | \
  sed -e '1 i\#!\/user\/bin\/env python3.6' | \
  sed -e '2 i \ ' | \
  sed -e '3 i \ ' \
  > ${TMP_FILE}

cat ${TMP_FILE} > ${PY_SCRIPT}

rm ${TMP_FILE}
