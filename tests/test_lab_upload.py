# SPDX-License-Identifier: Apache-2.0

# Standard
from unittest.mock import patch

# Third Party
from click.testing import CliRunner

# First Party
from instructlab import lab


class TestLabUpload:
    # When using `from X import Y` you need to understand that Y becomes part
    # of your module, so you should use `my_module.Y`` to patch.
    # When using `import X`, you should use `X.Y` to patch.
    # https://docs.python.org/3/library/unittest.mock.html#where-to-patch?
    @patch("instructlab.model.upload.HfApi.upload_file")
    def test_upload_gguf_hf(self, mock_upload_file, cli_runner: CliRunner):
        result = cli_runner.invoke(
            lab.ilab,
            [
                "--config=DEFAULT",
                "model",
                "upload",
                "--model=model.gguf",
                "--upload-desk=hf",
                "--hf-token=foo",
            ],
        )
        assert (
            result.exit_code == 0
        ), f"command finished with an unexpected exit code. {result.stdout}"
        assert mock_upload_file.call_count == 1

    # @patch(
    #     "instructlab.model.download.hf_hub_download",
    #     MagicMock(side_effect=HfHubHTTPError("Could not reach hugging face server")),
    # )
    # def test_download_error(self, cli_runner: CliRunner):
    #     result = cli_runner.invoke(
    #         lab.ilab,
    #         [
    #             "--config=DEFAULT",
    #             "model",
    #             "download",
    #         ],
    #     )
    #     assert result.exit_code == 1, "command finished with an unexpected exit code"
    #     assert "Could not reach hugging face server" in result.output

    # @patch("instructlab.model.download.OCIDownloader.download")
    # def test_oci_download(self, mock_oci_download, cli_runner: CliRunner):
    #     result = cli_runner.invoke(
    #         lab.ilab,
    #         [
    #             "--config=DEFAULT",
    #             "model",
    #             "download",
    #             "--repository=docker://quay.io/ai-lab/models/granite-7b-lab",
    #             "--release=latest",
    #         ],
    #     )
    #     assert result.exit_code == 0
    #     mock_oci_download.assert_called_once()

    # def test_oci_download_repository_error(self, cli_runner: CliRunner):
    #     result = cli_runner.invoke(
    #         lab.ilab,
    #         [
    #             "--config=DEFAULT",
    #             "model",
    #             "download",
    #             "--repository=docker://quay.io/ai-lab/models/granite-7b-lab:latest",
    #         ],
    #     )
    #     assert result.exit_code == 1
    #     assert (
    #         "\nInvalid repository supplied:\n    Please specify tag/version 'latest' via --release"
    #         in result.output
    #     )
