#!/usr/bin/env python3
#
# Copyright 2019 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# This script provides the main function for generating
# vulkan framework directly from the vulkan registry (vk.xml).

import generator_common as gencom
import api_generator as apigen
import driver_generator as drivergen

if __name__ == '__main__':
  gencom.parseVulkanRegistry()
  apigen.api_genh()
  apigen.api_gencpp()
  drivergen.driver_genh()
  drivergen.driver_gencpp()
