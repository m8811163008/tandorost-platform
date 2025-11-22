FROM python:3.13.6

# Set the working directory inside the container
WORKDIR /tandorost-platform

# Set a consistent POETRY_HOME where the executable will live, e.g., /usr/local/bin/poetry
ENV POETRY_HOME="/usr/local"
# Add the POETRY_HOME/bin to the PATH for convenience
ENV PATH="$POETRY_HOME/bin:$PATH"

# 1. Install system dependencies and Poetry
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl build-essential \
    # Install Poetry via official method. It installs into POETRY_HOME/bin
    && curl -sSL https://install.python-poetry.org | python3 -

# New Layer: Verify installation and Cleanup
# The executable is now reliably at /usr/local/bin/poetry
# Let's check:
# RUN $POETRY_HOME/bin/poetry --version \ # This path may vary.

# Use a clean, explicit check after the installation script runs, which should place
# the executable in a PATH-accessible location if POETRY_HOME is set correctly.
# If using the standard script and POETRY_HOME is set to a PATH location like /usr/local,
# the executable usually ends up at /usr/local/bin/poetry.

RUN poetry --version \
    # Clean up APT caches
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 2. Copy Poetry dependency files first (from root of build context)
COPY . .

# 3. Install project dependencies
# FIX: Now that `poetry` is in the PATH, we can just call `poetry`
RUN poetry install --no-root

# ... (rest of the file)

# 6. Set the default command
# FIX: We can call `poetry` directly because it's in the PATH
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
