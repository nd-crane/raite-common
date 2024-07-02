# RAITE Common

## Overview

Welcome to the RAITE Common repository. This repository provides the necessary tools and resources for both the Blue and Red teams to interact with the system control streams effectively. It includes code for handling video streams, tests for ensuring functionality, and configuration files for project management.

## Features

- **Stream Interaction**: Tools for Blue and Red teams to receive and send video streams.
- **Endpoint Configuration**: Easy setup for receiving attacked streams via the MediaMTX server.
- **Project Structure**: Organized codebase with separate directories for source code and tests.

## Folder Structure

- **src/raite**: Contains the source code for interacting with the streaming control system.
- **tests**: Contains unit tests to ensure the functionality of the source code.
- **pdm.lock**: Contains the exact versions of dependencies used in the project.
- **pyproject.toml**: Configuration file for project dependencies and settings.

## Getting Started

### Prerequisites

- Access to the MediaMTX server configured in the RAITE Infrastructure.
- Python and PDM (Python Development Master) installed on your system.

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/RAITE-Common.git
   ```
2. Navigate to the project directory:
   ```sh
   cd RAITE-Common
   ```
3. Install the project dependencies using PDM:
   ```sh
   pdm install
   ```

### Usage

#### Red Team

- Redirect video streams from security cameras to your endpoint.
- Send the attacked streams back to the MediaMTX server.

#### Blue Team

- Receive the attacked streams through the endpoint provided by the MediaMTX server.

### Running Tests

To run the unit tests, use the following command:

```sh
pdm run pytest
```
