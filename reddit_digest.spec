# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec file for Reddit Digest Generator

This bundles the Python script with all dependencies into a single executable.

Usage:
    pyinstaller reddit_digest.spec
"""

import sys
from pathlib import Path

# Get the workspace directory
workspace_dir = Path.cwd()

# Analysis: Scan the script and collect all dependencies
a = Analysis(
    ['summarize_subreddit.py'],
    pathex=[str(workspace_dir)],
    binaries=[],
    datas=[
        # Include the reddit_summarizer package
        ('reddit_summarizer', 'reddit_summarizer'),
        # Include tiktoken data files (required by LiteLLM)
        (f'{workspace_dir}/.venv/lib/python3.12/site-packages/tiktoken_ext', 'tiktoken_ext'),
        # Include ALL LiteLLM data files (JSON configs, tokenizers, etc.)
        (f'{workspace_dir}/.venv/lib/python3.12/site-packages/litellm/*.json', 'litellm'),
        (f'{workspace_dir}/.venv/lib/python3.12/site-packages/litellm/litellm_core_utils/tokenizers', 'litellm/litellm_core_utils/tokenizers'),
        (f'{workspace_dir}/.venv/lib/python3.12/site-packages/litellm/containers', 'litellm/containers'),
        (f'{workspace_dir}/.venv/lib/python3.12/site-packages/litellm/llms/openai_like/*.json', 'litellm/llms/openai_like'),
    ],
    hiddenimports=[
        # Core dependencies
        'ace',
        'ace.skillbook',
        'ace.roles',
        'ace.prompts',
        'ace.prompts_v2',
        'ace.prompts_v2_1',
        'ace.llm',
        'ace.llm_providers',
        'ace.llm_providers.litellm_client',
        'ace.llm_providers.instructor_client',

        # LLM providers
        'litellm',
        'litellm.llms',
        'litellm.llms.openai',
        'litellm.litellm_core_utils',
        'litellm.litellm_core_utils.token_counter',
        'litellm.litellm_core_utils.default_encoding',
        'litellm.containers',
        'litellm.containers.main',
        'litellm.containers.utils',
        'instructor',
        'instructor.client',
        'instructor.patch',
        # Tiktoken (tokenizer used by LiteLLM)
        'tiktoken',
        'tiktoken.core',
        'tiktoken.registry',
        'tiktoken_ext',
        'tiktoken_ext.openai_public',

        # HTTP and API
        'requests',
        'requests.adapters',
        'requests.exceptions',
        'urllib3',

        # CLI and utilities
        'click',
        'dotenv',
        'tqdm',

        # JSON and data handling
        'json',
        'pydantic',
        'pydantic.json',

        # Standard library (sometimes needs explicit inclusion)
        'datetime',
        'pathlib',
        'os',
        'sys',
        'time',
        'typing',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # Exclude unnecessary packages to reduce size
        'matplotlib',
        'numpy',
        'pandas',
        'scipy',
        'PIL',
        'tkinter',
    ],
    noarchive=False,
)

# PYZ: Create archive of Python modules
pyz = PYZ(a.pure)

# EXE: Create the executable
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='reddit-digest',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,  # Compress with UPX (if available)
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # CLI application
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
