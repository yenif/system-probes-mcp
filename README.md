# System Probes MCP

`system-probes-mcp` is a collection of lightweight, special-purpose MCP (Model Context Protocol) tools designed to provide a large language model with contextual information about a system's filesystem and running processes.

## Overview

These tools are designed to be run as separate processes, allowing the main agent to query them for information without blocking its primary terminal. They communicate over standard I/O using a simple JSON-based protocol.

## Probes

### Filesystem Probe (`fs_mcp`)

Provides tools for inspecting the filesystem.

**Commands:**

*   `ls(path)`: Lists the contents of a directory.
*   `cat(path, start_line=None, end_line=None)`: Reads the content of a file.
*   `stat(path)`: Retrieves detailed metadata about a file or directory.
*   `find(path, name_pattern)`: Searches for files and directories.

### Process Probe (`proc_mcp`)

Provides tools for inspecting running processes.

**Commands:**

*   `ps(session_id=None)`: Lists running processes.
*   `status(pid)`: Gets the detailed status of a specific process.
*   `get_proc_output(pid)`: (Not yet implemented) Retrieves the output of a running process.

## Getting Started

This project is in its early stages. More documentation and features will be added over time.
