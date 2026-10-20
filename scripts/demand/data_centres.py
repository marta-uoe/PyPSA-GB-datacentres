'''
Draft the full desxription of what's happening in the workflow:

1. Three allocation types
2. Two different ways for predicting peak demand for Data Centres speciically
3. Three flexibility options:
    a. Temporal
    b. Spatial
    c. Spatio-temporal
4. Offsetting CO2 (CFE):
    a. On its own 
    b. CFE + spatio-temporal
'''

import pandas as pd
import pypsa
import logging
import numpy as np
import xarray as xr
from pathlib import Path
import sys
from typing import Optional, Dict, Any

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.utilities.logging_config import setup_logging
from scripts.utilities.network_io import load_network
from scripts.demand.load import load_spatial_mapping_data, aggregate_demand_to_network_topology