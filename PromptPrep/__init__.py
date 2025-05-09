from .aggregator import CodeAggregator, DirectoryTreeGenerator

# Conditionally import TUI components based on platform
import platform

# Don't attempt to import TUI on Windows
if platform.system() != "Windows":
    try:
        from .tui import select_files_interactive, FileSelector
    except ImportError:
        # Define empty placeholders if import fails
        def select_files_interactive(*args, **kwargs):
            raise NotImplementedError("TUI not available on this platform")

        class FileSelector:
            def __init__(self, *args, **kwargs):
                raise NotImplementedError("TUI not available on this platform")

else:
    # Define empty placeholders for Windows
    def select_files_interactive(*args, **kwargs):
        raise NotImplementedError("TUI not supported on Windows")

    class FileSelector:
        def __init__(self, *args, **kwargs):
            raise NotImplementedError("TUI not supported on Windows")


from .formatters import (
    BaseFormatter,
    PlainTextFormatter,
    MarkdownFormatter,
    HtmlFormatter,
    HighlightedFormatter,
    get_formatter,
)
from .config import ConfigManager

import importlib.metadata

try:
    __version__ = importlib.metadata.version("promptprep")
except importlib.metadata.PackageNotFoundError:
    # Handle case where package is not installed (e.g., running from source)
    __version__ = "0.0.0-dev"

__all__ = [
    "CodeAggregator",
    "DirectoryTreeGenerator",
    "select_files_interactive",
    "FileSelector",
    "BaseFormatter",
    "PlainTextFormatter",
    "MarkdownFormatter",
    "HtmlFormatter",
    "HighlightedFormatter",
    "get_formatter",
    "ConfigManager",
]
