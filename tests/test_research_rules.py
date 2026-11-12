import unittest
from pathlib import Path

SKILL = Path(__file__).parents[1] / "SKILL.md"


class NIPResearchContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = SKILL.read_text(encoding="utf-8")
        cls.lower = cls.text.lower()

    def test_canonical_upstream_repository_is_explicit(self):
        self.assertIn("https://github.com/nostr-protocol/nips", self.lower)
        self.assertIn("authoritative public repository", self.lower)

    def test_current_research_fetches_registry_and_individual_nip(self):
        self.assertIn("repository readme", self.lower)
        self.assertIn("individual nip file", self.lower)
        self.assertIn("from the same repository revision", self.lower)

    def test_provenance_is_required_for_each_research_task(self):
        self.assertIn("record the commit sha and commit timestamp", self.lower)
        self.assertIn("retrieval provenance", self.lower)
        self.assertIn("not a claim that the branch will remain unchanged", self.lower)

    def test_nip_number_and_event_kind_are_separate_namespaces(self):
        self.assertIn("nip number and event kind are different namespaces", self.lower)
        self.assertIn("never infer an event kind from the nip number", self.lower)

    def test_status_vocabulary_preserves_compatibility_context(self):
        for phrase in (
            "draft",
            "final",
            "optional",
            "unrecommended",
            "deprecated/replaced",
            "not listed",
            "compatibility implications",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.lower)

    def test_missing_registry_entry_is_not_treated_as_nonexistence(self):
        self.assertIn(
            "not listed” is not proof that no implementation exists",
            self.text,
        )

    def test_normative_strength_and_implementation_status_are_preserved(self):
        self.assertIn("must/should/may", self.lower)
        self.assertIn("do not upgrade recommendations to requirements", self.lower)
        self.assertIn("implementation-specific or experimental", self.lower)

    def test_implementation_handoff_uses_nostr_skill_with_verified_clauses(self):
        self.assertIn("pass implementation tasks to the nostr skill", self.lower)
        self.assertIn("exact relevant normative clauses", self.lower)


if __name__ == "__main__":
    unittest.main()
