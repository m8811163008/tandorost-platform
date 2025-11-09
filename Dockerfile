# `docker-compose logs -f` for real time hot reload
# For Debug and DEVELOPE
# syntax=docker/dockerfile:1

FROM python:3.13.6

# Set environment variable for Poetry AND add its 'bin' directory to PATH
ENV POETRY_HOME="/etc/poetry"

# Set the working directory inside the container
WORKDIR /tandorost-platform

# 1. Install system dependencies and Poetry
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl build-essential \
    # Install Poetry via official method
    && curl -sSL https://install.python-poetry.org | POETRY_HOME=${POETRY_HOME} python3 -

# New Layer: Verify installation and Cleanup
RUN $POETRY_HOME/bin/poetry --version \
    # Clean up APT caches
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 2. Copy Poetry dependency files first (from root of build context)
COPY . .
# COPY poetry.lock ./ # Uncomment this when you generate the lock file locally!

# 3. Install project dependencies
# FIX: Use the explicit, reliable path for the Poetry executable in $POETRY_HOME.
RUN $POETRY_HOME/bin/poetry install --no-root


# 5. Expose the application port
EXPOSE 8001

# 6. Set the default command
# CMD will rely on the PATH environment variable set earlier, which should be stable here.
CMD ["$POETRY_HOME/bin/poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]



