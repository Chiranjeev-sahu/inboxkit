"""Guard the field ambiguities found in the final repository review."""

import unittest

from scripts.check_submission import merge_issues
from scripts.prepare_export import normalize_accept_all


class SubmissionFieldsTest(unittest.TestCase):
    def test_provider_alias_preserves_risk(self):
        fields, rows = normalize_accept_all(["name", "is_accept_all"],
                                           [{"name": "Buyer", "is_accept_all": "true"}])
        self.assertEqual(fields, ["name", "verification_accept_all"])
        self.assertEqual(rows[0]["verification_accept_all"], "true")
        with self.assertRaises(ValueError):
            normalize_accept_all(["is_accept_all", "verification_accept_all"],
                                 [{"is_accept_all": "true", "verification_accept_all": "false"}])

    def test_blank_flag_is_not_false_and_missing_greeting_is_caught(self):
        _, rows = normalize_accept_all(["is_accept_all"], [{"is_accept_all": ""}])
        self.assertEqual(rows[0]["verification_accept_all"], "")
        good = {"company": "Example", "first_name": "Buyer", "email_variant": "A",
                "verification_accept_all": ""}
        self.assertEqual(merge_issues([good]), [])
        missing = dict(good, first_name="", email_variant="")
        self.assertEqual(len(merge_issues([missing])), 2)


if __name__ == "__main__":
    unittest.main()
