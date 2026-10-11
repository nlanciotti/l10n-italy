#  Copyright 2024 Simone Rubino - Aion Tech
#  License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests import tagged

from odoo.addons.account.tests.common import AccountTestInvoicingCommon


@tagged("post_install", "-at_install")
class TestAccount(AccountTestInvoicingCommon):
    def test_type_prepayments(self):
        prepayment_account = self.env["account.account"].create(
            {
                "code": "TESTPREPAY",
                "name": "Test prepayments",
                "account_type": "asset_prepayments",
            }
        )
        self.assertEqual(
            prepayment_account.financial_statements_report_section, "assets"
        )
