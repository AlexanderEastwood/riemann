"""Keep incomplete model output out of the proposal-review queue."""
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch
import unittest

from tools.geometry_swarm.__main__ import FIELDS, extract_candidate, run_swarm
from tools.geometry_swarm.models import Endpoint


class PipelineTests(unittest.TestCase):
    def test_http_success_is_not_a_complete_proposal(self) -> None:
        self.assertIsNone(extract_candidate({'status': 'success', 'response': 'RH is proved!'}))
        self.assertIsNone(extract_candidate({'status': 'success', 'response': '{"title":"new shape"}'}))

    def test_schema_is_only_a_format_check(self) -> None:
        import json
        candidate = {field: 'missing' for field in FIELDS}
        self.assertEqual(extract_candidate({'status': 'success', 'response': json.dumps(candidate)}), candidate)

    def test_failed_proposals_do_not_spawn_review_requests(self) -> None:
        with TemporaryDirectory() as directory:
            output = Path(directory) / 'fresh'
            with patch('tools.geometry_swarm.__main__.run_jobs', return_value=[
                {'job_id': 'symplectic_0', 'status': 'failed', 'response': None},
                {'job_id': 'arithmetic_geometry_0', 'status': 'success', 'response': '{}'},
                {'job_id': 'spectral_0', 'status': 'success', 'response': 'bad JSON'},
            ]) as client:
                ep = Endpoint('http://127.0.0.1:8000/v1', 'test')
                result = run_swarm(ep, ep, output, 'context', 1, 100, 10)
                self.assertEqual(result['complete_structured_candidates'], 0)
                self.assertEqual(result['review_requests'], 0)
                self.assertEqual(result['rh_claims_admitted'], 0)
                self.assertEqual(client.call_count, 1)
                with self.assertRaises(FileExistsError):
                    run_swarm(ep, ep, output, 'context', 1, 100, 10)


if __name__ == '__main__':
    unittest.main()
