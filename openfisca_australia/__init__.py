"""Defines Australia's tax and benefit system.

A tax and benefit system is the higher-level instance in OpenFisca. It holds
the variables (source code) and legislation parameters (data) that model the
legislation.

See https://openfisca.org/doc/key-concepts/tax_and_benefit_system.html
"""

import os

from openfisca_core.taxbenefitsystems import TaxBenefitSystem

from openfisca_australia import entities
from openfisca_australia.situation_examples import single

COUNTRY_DIR = os.path.dirname(os.path.abspath(__file__))


# The name CountryTaxBenefitSystem must not be changed: all tools of the
# OpenFisca ecosystem expect this class to be exposed by a country package.
class CountryTaxBenefitSystem(TaxBenefitSystem):
    def __init__(self):
        """Initialize Australia's tax and benefit system."""
        super().__init__(entities.entities)

        self.add_variables_from_directory(os.path.join(COUNTRY_DIR, "variables"))
        self.load_parameters(os.path.join(COUNTRY_DIR, "parameters"))

        # Used in the OpenAPI specification. Update as real variables and
        # parameters are added.
        self.open_api_config = {
            "variable_example": "age",
            "simulation_example": single,
        }
