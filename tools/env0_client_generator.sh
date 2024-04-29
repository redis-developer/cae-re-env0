#!/usr/bin/env bash

set -e

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
TARGET_DIR="${SCRIPT_DIR}/../deps/env0_client"


# This script generates the client code for the env0 API
rm -fr "${TARGET_DIR}" || true
openapi-generator generate -g python -i "${SCRIPT_DIR}/env0_spec.json" -o "${TARGET_DIR}" \
  --skip-validate-spec --additional-properties=packageName=env0_client