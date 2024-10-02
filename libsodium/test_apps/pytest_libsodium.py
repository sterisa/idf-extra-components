# SPDX-FileCopyrightText: 2024 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: Apache-2.0
import pytest


@pytest.mark.generic
def test_libsodium(dut) -> None:
    dut.run_all_single_board_cases(timeout=120)